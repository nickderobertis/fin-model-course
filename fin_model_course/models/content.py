import datetime
import hashlib
import pathlib
from typing import Optional, Dict, List, Type

from pydantic import BaseModel, Field

from build_tools.config import DOCSRC_STATIC_PATH
from lectures.model import LectureResource

CONTENT_TYPE_CODES_TO_NAMES = {
    "C": "Course Materials",
    "S": "Slides",
    "LN": "Lecture Notes",
    "PJ": "Project Descriptions",
    "PR": "Practice Problems",
}

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
            return all(
                [
                    self.file_hash == other.file_hash,
                    self.name == other.name,
                ]
            )
        except AttributeError:
            return False

    @classmethod
    def generate_from_file(
        cls,
        folder: pathlib.Path,
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
        folder: pathlib.Path,
        file_name: str,
        hashed_extension: str = "tex",
        output_extension: str = "pdf",
    ) -> "ContentMetadata":
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

        full_file_name = f"{file_name}.{hashed_extension}"
        path = folder / full_file_name
        contents = path.read_bytes()
        hashed = hashlib.md5(contents).hexdigest()
        return cls(
            name=name,
            file_hash=hashed,
            hashed_extension=hashed_extension,
            output_extension=output_extension,
            content_type_code=content_type,
            content_index=int(content_index),
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
        for file in folder.glob(f"*.{hashed_extension}"):
            file_name = file.stem
            metadata = cls._metadata_cls.generate_from_file(
                folder,
                file_name,
                hashed_extension=hashed_extension,
                output_extension=output_extension,
            )
            relative_path = file.relative_to(base_path)
            items[str(relative_path)] = metadata
        return cls(items=items)

    def merge(self, other: "CollectionMetadata") -> "CollectionMetadata":
        items: Dict[str, ContentMetadata] = {**self.items}
        for name, md in other.items.items():
            if name not in items:
                items[name] = md
                continue
            # Metadata is in both collections. If hash and details are the same,
            # keep the old metadata, otherwise take the new metadata
            current_md = items[name]
            if current_md == md:
                continue
            items[name] = md
        return self.__class__(items=items)

    def to_rst(self) -> str:
        raise NotImplementedError


class GeneratedCollectionMetadata(CollectionMetadata):
    items: Dict[str, GeneratedContentMetadata]
    _metadata_cls: Type[ContentMetadata] = GeneratedContentMetadata

    def to_rst(self) -> str:
        out_str = f"""
Downloads
************************************************************************************************************************
"""
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
            out_str += f"""
{category}
=======================================================================================================================
            """
            for resource in items:
                out_str += resource.to_rst()
        return out_str
