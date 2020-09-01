import os
import pathlib
import shutil

from plbuilder.cli import build_by_file_path
import derobertis_cv

PACKAGE_ROOT = pathlib.Path(__file__).parent.parent
PROJECT_ROOT = PACKAGE_ROOT.parent
LOCAL_PLBUILDER_ROOT = PACKAGE_ROOT / 'plbuild' / 'sources'

CV_SOURCES_ROOT = pathlib.Path(derobertis_cv.__file__).parent / 'plbuild' / 'sources' / 'document'
FM_DOCUMENT_SOURCES_ROOT = LOCAL_PLBUILDER_ROOT / 'document'
FM_PRESENTATION_SOURCES_ROOT = LOCAL_PLBUILDER_ROOT / 'presentation'
CONTENT_ROOTS = [
    CV_SOURCES_ROOT,
    FM_DOCUMENT_SOURCES_ROOT,
    FM_PRESENTATION_SOURCES_ROOT,
]

DOCUMENTS_OUT_PATH = pathlib.Path('Documents')
HANDOUTS_OUT_PATH = pathlib.Path('Handouts')
OUT_PATHS = [
    DOCUMENTS_OUT_PATH,
    HANDOUTS_OUT_PATH,
]
DOCUMENTS_MOVE_TO = PROJECT_ROOT / 'docsrc' / 'source' / '_static' / 'generated' / 'pdfs'


def build_pdfs():
    _build_pdfs()
    _move_pdfs()


def _build_pdfs():
    for root in CONTENT_ROOTS:
        for file in next(os.walk(root))[2]:
            if file in ('__init__.py', 'professional_cv.py'):
                continue
            file_path = (root / file).resolve()
            build_by_file_path(file_path)


def _move_pdfs():
    if not os.path.exists(DOCUMENTS_MOVE_TO):
        os.makedirs(DOCUMENTS_MOVE_TO)
    for out_path in OUT_PATHS:
        pdfs = [file for file in next(os.walk(out_path))[2] if file.endswith('pdf')]
        for file in pdfs:
            file_path = out_path / file
            shutil.copy(file_path, DOCUMENTS_MOVE_TO)


if __name__ == '__main__':
    build_pdfs()
