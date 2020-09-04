"""
Creates the rst source for the downloads page
"""
import pathlib

from build_tools.config import DOCSRC_SOURCE_PATH, GENERATED_CONTENT_METADATA_PATH, STATIC_CONTENT_METADATA_PATH
from models.content import CollectionMetadata, GeneratedCollectionMetadata, StaticCollectionMetadata

OUT_PATH = DOCSRC_SOURCE_PATH / "downloads.rst"


def _generate_generated_content_rst(
    metadata_path: pathlib.Path = GENERATED_CONTENT_METADATA_PATH,
) -> str:
    metadata = GeneratedCollectionMetadata.parse_raw(metadata_path.read_text())
    source = metadata.to_rst()
    return source

def _generate_static_content_rst(
    metadata_path: pathlib.Path = STATIC_CONTENT_METADATA_PATH,
) -> str:
    metadata = StaticCollectionMetadata.parse_raw(metadata_path.read_text())
    source = metadata.to_rst()
    return source


def generate_downloads_rst(
    generated_metadata_path: pathlib.Path = GENERATED_CONTENT_METADATA_PATH,
    static_metadata_path: pathlib.Path = STATIC_CONTENT_METADATA_PATH,
    out_path: pathlib.Path = OUT_PATH,
):
    source = _generate_generated_content_rst(generated_metadata_path)
    source += _generate_static_content_rst(static_metadata_path)
    out_path.write_text(source)


if __name__ == "__main__":
    generate_downloads_rst()
