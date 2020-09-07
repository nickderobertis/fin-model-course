import datetime
import hashlib
import os
import pathlib
from typing import Optional, Dict, List, Type, cast, Callable

from pydantic import BaseModel, Field

from build_tools.config import DOCSRC_STATIC_PATH
from build_tools.ext_rst import header_rst
from lectures.model import LectureResource

CONTENT_TYPE_CODES_TO_NAMES = {
    "C": "Course Materials",
    "S": "Slides",
    "LN": "Lecture Notes",
    "PR": "Practice Problems",
    "PJ": "Project Descriptions",
}

EXAMPLE_SECTION_ORDER = [
    "Introduction",
    "Visualization",
    "Sensitivity Analysis",
    "Scenario Analysis",
    "Internal Randomness",
    "Connecting Python and Excel",
    "Monte Carlo",
    "DCF",
]

STATIC_CONTENT_ORDER = [
    "Project Materials",
    "Practice Problem Solutions",
    "Materials for Lab Exercises",
    "Examples",
    "Extra Examples",
]

CONTENT_BASE_PATH = DOCSRC_STATIC_PATH


class ContentMetadata(BaseModel):
    name: str
    file_hash: str
    hashed_extension: str = "tex"
    output_extension: str = "pdf"
    last_modified: datetime.datetime = Field(
        default_factory=lambda: datetime.datetime.now()
    )

    def __eq__(self, other):
        try:
            return all([self.file_hash == other.file_hash, self.name == other.name,])
        except AttributeError:
            return False

    @classmethod
    def generate_from_file(
        cls,
        file_path: pathlib.Path,
        file_name: str,
        hashed_extension: str = "tex",
        output_extension: str = "pdf",
    ) -> "ContentMetadata":
        raise NotImplementedError


class GeneratedContentMetadata(ContentMetadata):
    content_type_code: Optional[str] = None
    content_index: Optional[int] = None

    def __eq__(self, other):
        try:
            return all(
                [
                    self.file_hash == other.file_hash,
                    self.name == other.name,
                    self.content_type_code == other.content_type_code,
                    self.content_index == other.content_index,
                ]
            )
        except AttributeError:
            return False

    @classmethod
    def generate_from_file(
        cls,
        file_path: pathlib.Path,
        file_name: str,
        hashed_extension: str = "tex",
        output_extension: str = "pdf",
    ) -> "GeneratedContentMetadata":
        name_parts = str(file_name).split()
        content_type_code_and_index = name_parts[0]
        content_type = ""
        content_index = ""
        for i, char in enumerate(content_type_code_and_index):
            if char.isdigit():
                content_index = content_type_code_and_index[i:]
                break
            else:
                content_type += char

        name = " ".join(name_parts[1:])

        contents = file_path.read_bytes()
        hashed = hashlib.md5(contents).hexdigest()
        return cls(
            name=name,
            file_hash=hashed,
            hashed_extension=hashed_extension,
            output_extension=output_extension,
            content_type_code=content_type,
            content_index=int(content_index),
        )


class StaticContentMetadata(ContentMetadata):
    @classmethod
    def generate_from_file(
        cls,
        file_path: pathlib.Path,
        file_name: str,
        hashed_extension: str = "xlsx",
        output_extension: str = "xlsx",
    ) -> "StaticContentMetadata":
        name = file_path.stem
        contents = file_path.read_bytes()
        hashed = hashlib.md5(contents).hexdigest()
        return cls(
            name=name,
            file_hash=hashed,
            hashed_extension=hashed_extension,
            output_extension=output_extension,
        )


class CollectionMetadata(BaseModel):
    items: Dict[str, ContentMetadata]
    _metadata_cls: Type[ContentMetadata] = ContentMetadata

    @classmethod
    def generate_from_folder(
        cls,
        folder: pathlib.Path,
        hashed_extension: str = "tex",
        output_extension: str = "pdf",
        base_path: pathlib.Path = CONTENT_BASE_PATH,
    ) -> "CollectionMetadata":
        items: Dict[str, ContentMetadata] = {}
        for file in folder.rglob(f"*.{hashed_extension}"):
            if ".ipynb_checkpoints" in str(file):
                continue
            file_name = file.stem
            metadata = cls._metadata_cls.generate_from_file(
                file,
                file_name,
                hashed_extension=hashed_extension,
                output_extension=output_extension,
            )
            relative_path = file.relative_to(base_path)
            items[str(relative_path)] = metadata
        return cls(items=items)

    def merge(
        self, other: "CollectionMetadata", drop_unique_old: bool = False
    ) -> "CollectionMetadata":
        items: Dict[str, ContentMetadata] = {}
        if not drop_unique_old:
            items = {**self.items}

        for name, md in other.items.items():
            if name not in self.items:
                items[name] = md
                continue
            # Metadata is in both collections. If hash and details are the same,
            # keep the old metadata, otherwise take the new metadata
            current_md = self.items[name]
            if current_md == md:
                items[name] = current_md
                continue
            items[name] = md
        return self.__class__(items=items)

    def sort(self, key: Callable = lambda tup: tup[0], reverse: bool = False):
        sorted_items = dict(sorted(self.items.items(), key=key, reverse=reverse))
        self.items = sorted_items

    @property
    def last_modified(self) -> datetime.datetime:
        lms = [item.last_modified for item in self.items.values()]
        valid_lms = [lm for lm in lms if lm is not None]
        return max(valid_lms)

    def to_rst(self) -> str:
        raise NotImplementedError


class GeneratedCollectionMetadata(CollectionMetadata):
    items: Dict[str, GeneratedContentMetadata]
    _metadata_cls: Type[ContentMetadata] = GeneratedContentMetadata

    def to_rst(self) -> str:
        out_str = ""
        items_categories: Dict[str, List[LectureResource]] = {
            name: [] for name in CONTENT_TYPE_CODES_TO_NAMES.values()
        }
        items_categories["Other"] = []
        for file_name, md in self.items.items():
            resource = LectureResource.from_metadata(md)
            if md.content_type_code:
                category = CONTENT_TYPE_CODES_TO_NAMES[md.content_type_code]
            else:
                category = "Other"
            items_categories[category].append(resource)
        for items in items_categories.values():
            items.sort(key=lambda res: res.index if res.index is not None else -1)
        for category, items in items_categories.items():
            if not items:
                continue
            out_str += header_rst(category, 3)
            for resource in items:
                out_str += resource.to_rst()
        return out_str


class StaticCollectionMetadata(CollectionMetadata):
    items: Dict[str, GeneratedContentMetadata]
    _metadata_cls: Type[ContentMetadata] = StaticContentMetadata

    def to_rst(self) -> str:
        sections_dict = {"_items": [], "_description": ""}
        for file_path, md in self.items.items():
            file_parts = file_path.split(os.path.sep)
            folders = file_parts[:-1]
            file_name = file_parts[-1]
            resource = LectureResource.from_metadata(md, url=file_path)
            this_section_dict = sections_dict
            for folder in folders:
                if folder not in this_section_dict:
                    this_section_dict[folder] = {"_items": [], "_description": ""}
                this_section_dict = this_section_dict[folder]
            if file_name == "README.rst":
                this_section_dict["_description"] = (
                    DOCSRC_STATIC_PATH / file_path
                ).read_text()
            else:
                this_section_dict["_items"].append(resource)
            # TODO [#20]: static resource sorting would be more efficient in a separate loop after all items are created
            this_section_dict["_items"].sort(
                key=lambda res: res.index if res.index is not None else -1
            )

        sections_dict = dict(
            sorted(
                sections_dict.items(),
                key=lambda tup: f"aaa{STATIC_CONTENT_ORDER.index(tup[0])}"
                if tup[0] in STATIC_CONTENT_ORDER
                else tup[0],
            )
        )

        for section_name, section in sections_dict.items():
            if section_name in ["_items", "_description"]:
                continue
            sorted_section = dict(
                sorted(
                    section.items(),
                    key=lambda tup: f"aaa{EXAMPLE_SECTION_ORDER.index(tup[0])}"
                    if tup[0] in EXAMPLE_SECTION_ORDER
                    else tup[0],
                )
            )
            sections_dict[section_name] = sorted_section

        out_str = _static_sections_rst(sections_dict, 3)
        return out_str


def _static_sections_rst(sections_dict: dict, level: int) -> str:
    this_section_contents = sections_dict["_description"] + "\n\n"
    sub_section_contents = ""
    for section_name, section_content in sections_dict.items():
        if section_name == "_description":
            continue
        if section_name == "_items":
            # Content for this section, not another subsection
            section_content = cast(List[LectureResource], section_content)
            for res in section_content:
                this_section_contents += res.to_rst()
            continue

        # Content for sub-section
        section_content = cast(dict, section_content)
        sub_section_contents += header_rst(section_name, level)
        sub_section_contents += _static_sections_rst(section_content, level + 1)

    all_contents = this_section_contents + sub_section_contents
    return all_contents
