import pathlib

PACKAGE_ROOT = pathlib.Path(__file__).parent.parent
PROJECT_ROOT = PACKAGE_ROOT.parent
LOCAL_PLBUILDER_ROOT = PACKAGE_ROOT / 'plbuild' / 'sources'
BUILD_TOOLS_ROOT = PACKAGE_ROOT / 'build_tools'

DOCSRC_SOURCE_PATH = PROJECT_ROOT / 'docsrc' / 'source'
GENERATED_OUT_PATH = DOCSRC_SOURCE_PATH / '_static' / 'generated'
GENERATED_PDFS_OUT_PATH = GENERATED_OUT_PATH / 'pdfs'

GENERATED_CONTENT_METADATA_PATH = BUILD_TOOLS_ROOT / "generated-content-metadata.json"