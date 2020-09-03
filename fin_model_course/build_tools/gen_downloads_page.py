"""
Creates the rst source for the downloads page
"""
import pathlib

from build_tools.config import DOCSRC_SOURCE_PATH, GENERATED_CONTENT_METADATA_PATH
from models.content import CollectionMetadata

IN_PATH = GENERATED_CONTENT_METADATA_PATH
OUT_PATH = DOCSRC_SOURCE_PATH / "downloads.rst"


def generate_downloads_rst(
    metadata_path: pathlib.Path = IN_PATH, out_path: pathlib.Path = OUT_PATH
):
    metadata = CollectionMetadata.parse_raw(metadata_path.read_text())
    source = metadata.to_rst()
    out_path.write_text(source)


if __name__ == "__main__":
    generate_downloads_rst()
