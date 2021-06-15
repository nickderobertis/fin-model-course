"""
Takes hashes of all the generated content and determines whether the hash
has changed to update a JSON file with modified times
"""
import pathlib
from typing import Optional, Type

from build_tools.config import (
    GENERATED_PDFS_OUT_PATH,
    GENERATED_CONTENT_METADATA_PATH,
    EXAMPLE_PATHS,
    STATIC_CONTENT_METADATA_PATH, LECTURE_YOUTUBE_DESCRIPTIONS_METADATA_PATH,
)
from lectures.config import get_lecture_groups
from models.content import (
    GeneratedCollectionMetadata,
    FileCollectionMetadata,
    StaticCollectionMetadata,
    LectureYouTubeDescriptionCollectionMetadata
)
from resources.models import RESOURCES


def generate_content_metadata_json(
    in_folder: pathlib.Path = GENERATED_PDFS_OUT_PATH,
    out_path: pathlib.Path = GENERATED_CONTENT_METADATA_PATH,
    collection_cls: Type[FileCollectionMetadata] = GeneratedCollectionMetadata,
    hashed_extension: str = "tex",
    output_extension: str = "pdf",
    drop_unique_old: bool = False,
):
    print(f"Analyzing metadata for folder {in_folder}")
    current_metadata: Optional[collection_cls] = None
    if out_path.exists():
        current_metadata = collection_cls.parse_raw(out_path.read_text())
        print(f"Got existing metadata with {len(current_metadata.items)} items")
    print(f"Generating new metadata for folder {in_folder}")
    metadata = collection_cls.generate_from_folder(
        in_folder, hashed_extension=hashed_extension, output_extension=output_extension
    )
    if current_metadata is not None:
        print(f"Merging metadata")
        metadata = current_metadata.merge(metadata, drop_unique_old=drop_unique_old)
    metadata.sort()
    print(f"Writing content metadata to {out_path}")
    out_path.write_text(metadata.json(indent=2))


def generate_lecture_youtube_description_metadata_json(
    out_path: pathlib.Path = LECTURE_YOUTUBE_DESCRIPTIONS_METADATA_PATH
):
    print(f"Analyzing metadata for lecture YouTube descriptions")
    current_metadata: Optional[LectureYouTubeDescriptionCollectionMetadata] = None
    if out_path.exists():
        current_metadata = LectureYouTubeDescriptionCollectionMetadata.parse_raw(out_path.read_text())
        print(f"Got existing metadata with {len(current_metadata.items)} items")
    print(f"Generating new metadata for lecture YouTube descriptions")
    lecture_groups = get_lecture_groups()
    metadata = LectureYouTubeDescriptionCollectionMetadata.generate_from_lecture_groups(
        lecture_groups
    )
    if current_metadata is not None:
        print(f"Merging metadata")
        metadata = current_metadata.merge(metadata, drop_unique_old=True)
    metadata.sort()
    print(f"Writing content metadata to {out_path}")
    out_path.write_text(metadata.json(indent=2))


if __name__ == "__main__":
    generate_content_metadata_json(drop_unique_old=True)

    for path in EXAMPLE_PATHS:
        for ext in ['xlsx', 'xls', 'ipynb', 'py', 'rst', 'csv', 'pdf', 'pptx']:
            generate_content_metadata_json(
                path,
                STATIC_CONTENT_METADATA_PATH,
                StaticCollectionMetadata,
                hashed_extension=ext,
                output_extension=ext,
            )

    generate_lecture_youtube_description_metadata_json()

    RESOURCES.validate_locations()