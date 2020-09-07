"""
Creates the rst source for the downloads page
"""
import datetime
import pathlib
from typing import Sequence

from build_tools.config import (
    DOCSRC_SOURCE_PATH,
    GENERATED_CONTENT_METADATA_PATH,
    STATIC_CONTENT_METADATA_PATH,
    ZIP_FILE,
    DOCSRC_STATIC_PATH,
    ZIP_FILE_NAME,
    METADATA_PATHS,
)
from build_tools.ext_rst import header_rst
from lectures.model import LectureResource
from models.content import (
    CollectionMetadata,
    GeneratedCollectionMetadata,
    StaticCollectionMetadata,
)

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


def _get_last_modified_all_content(
    generated_metadata_path: pathlib.Path = GENERATED_CONTENT_METADATA_PATH,
    static_metadata_path: pathlib.Path = STATIC_CONTENT_METADATA_PATH,
) -> datetime.datetime:
    generated_lm = GeneratedCollectionMetadata.parse_raw(
        generated_metadata_path.read_text()
    ).last_modified
    static_lm = StaticCollectionMetadata.parse_raw(
        static_metadata_path.read_text()
    ).last_modified
    return max(generated_lm, static_lm)


def generate_downloads_rst(
    generated_metadata_path: pathlib.Path = GENERATED_CONTENT_METADATA_PATH,
    static_metadata_path: pathlib.Path = STATIC_CONTENT_METADATA_PATH,
    out_path: pathlib.Path = OUT_PATH,
):
    source = header_rst("Downloads", 2)
    all_downloads_url = str(ZIP_FILE.relative_to(DOCSRC_STATIC_PATH))
    all_downloads_last_modified = _get_last_modified_all_content(
        generated_metadata_path, static_metadata_path
    )
    all_downloads_resource = LectureResource(
        ZIP_FILE_NAME, static_url=all_downloads_url, updated=all_downloads_last_modified
    )
    source += f"""
Find all the individual files for course content on this page. Files will be 
updated over time so the last updated date is displayed next to the file. To
download all the content as a zip file, use the following link:
    """
    source += all_downloads_resource.to_rst()
    source += _generate_generated_content_rst(generated_metadata_path)
    source += _generate_static_content_rst(static_metadata_path)
    out_path.write_text(source)


if __name__ == "__main__":
    generate_downloads_rst()
