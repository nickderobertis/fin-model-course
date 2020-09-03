"""
Takes hashes of all the generated content and determines whether the hash
has changed to update a JSON file with modified times
"""
import pathlib
from typing import Optional

from build_tools.config import GENERATED_PDFS_OUT_PATH, BUILD_TOOLS_ROOT
from models.content import CollectionMetadata

IN_FOLDER = GENERATED_PDFS_OUT_PATH
OUT_PATH = BUILD_TOOLS_ROOT / "generated-content-metadata.json"


def generate_content_metadata_json(
    in_folder: pathlib.Path = IN_FOLDER, out_path: pathlib.Path = OUT_PATH
):
    print(f"Analyzing metadata for folder {in_folder}")
    current_metadata: Optional[CollectionMetadata] = None
    if out_path.exists():
        current_metadata = CollectionMetadata.parse_raw(out_path.read_text())
        print(f"Got existing metadata with {len(current_metadata.items)} items")
    print(f"Generating new metadata for folder {in_folder}")
    metadata = CollectionMetadata.generate_from_folder(in_folder)
    if current_metadata is not None:
        print(f"Merging metadata")
        metadata = current_metadata.merge(metadata)
    print(f"Writing content metadata to {out_path}")
    out_path.write_text(metadata.json(indent=2))


if __name__ == "__main__":
    generate_content_metadata_json()
