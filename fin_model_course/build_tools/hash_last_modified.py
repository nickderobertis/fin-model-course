"""
Takes hashes of all the generated content and determines whether the hash
has changed to update a JSON file with modified times
"""
import datetime
import hashlib
import pathlib
from typing import Dict, Optional

from pydantic import Field
from pydantic.main import BaseModel

from build_tools.config import GENERATED_PDFS_OUT_PATH, BUILD_TOOLS_ROOT

IN_FOLDER = GENERATED_PDFS_OUT_PATH
OUT_PATH = BUILD_TOOLS_ROOT / "generated-content-metadata.json"


class ContentMetadata(BaseModel):
    file_hash: str
    hashed_extension: str = "pdf"
    last_modified: datetime.datetime = Field(
        default_factory=lambda: datetime.datetime.now()
    )

    @classmethod
    def generate_from_file(
        cls, folder: pathlib.Path, name: str, extension: str = "pdf"
    ) -> "ContentMetadata":
        file_name = f"{name}.{extension}"
        path = folder / file_name
        contents = path.read_bytes()
        hashed = hashlib.md5(contents).hexdigest()
        return cls(file_hash=hashed, hashed_extension=extension)


class CollectionMetadata(BaseModel):
    items: Dict[str, ContentMetadata]

    @classmethod
    def generate_from_folder(
        cls, folder: pathlib.Path, extension: str = "pdf"
    ) -> "CollectionMetadata":
        items: Dict[str, ContentMetadata] = {}
        for file in folder.glob(f"*.{extension}"):
            file_path = folder / file
            file_name = file_path.stem
            metadata = ContentMetadata.generate_from_file(
                folder, file_name, extension=extension
            )
            items[file_name] = metadata
        return cls(items=items)

    def merge(self, other: 'CollectionMetadata') -> 'CollectionMetadata':
        items: Dict[str, ContentMetadata] = {**self.items}
        for name, md in other.items.items():
            if name not in items:
                items[name] = md
                continue
            # Metadata is in both collections. If hash is the same,
            # keep the old metadata, otherwise take the new metadata
            current_md = items[name]
            if current_md.file_hash == md.file_hash:
                continue
            items[name] = md
        return self.__class__(items=items)


def generate_content_metadata_json(
    in_folder: pathlib.Path = IN_FOLDER, out_path: pathlib.Path = OUT_PATH
):
    print(f'Analyzing metadata for folder {in_folder}')
    current_metadata: Optional[CollectionMetadata] = None
    if out_path.exists():
        current_metadata = CollectionMetadata.parse_raw(out_path.read_text())
        print(f'Got existing metadata with {len(current_metadata.items)} items')
    print(f'Generating new metadata for folder {in_folder}')
    metadata = CollectionMetadata.generate_from_folder(in_folder)
    if current_metadata is not None:
        print(f'Merging metadata')
        metadata = current_metadata.merge(metadata)
    print(f'Writing content metadata to {out_path}')
    out_path.write_text(metadata.json(indent=2))


if __name__ == "__main__":
    generate_content_metadata_json()
