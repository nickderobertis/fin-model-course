import pathlib
from typing import Callable
import functools
import os


def path_func(root_path: str) -> Callable:
    partial = functools.partial(os.path.join, root_path)
    return partial

PLBUILDER_PATH = str(pathlib.Path(__file__).parent)
plbuilder_path = path_func(PLBUILDER_PATH)
ASSETS_PATH = plbuilder_path('assets')
assets_path = path_func(ASSETS_PATH)
IMAGES_PATH = assets_path('images')
images_path = path_func(IMAGES_PATH)
SLIDES_BUILD_PATH = 'Slides'
slides_build_path = path_func(SLIDES_BUILD_PATH)
HANDOUTS_BUILD_PATH = 'Handouts'
handouts_build_path = path_func(HANDOUTS_BUILD_PATH)
DOCUMENTS_BUILD_PATH = 'Documents'
documents_build_path = path_func(DOCUMENTS_BUILD_PATH)
SOURCE_PATH = plbuilder_path('sources')
source_path = path_func(SOURCE_PATH)
SLIDES_SOURCE_PATH = source_path('presentation')
slides_source_path = path_func(SLIDES_SOURCE_PATH)
DOCUMENTS_SOURCE_PATH = source_path('document')
documents_source_path = path_func(DOCUMENTS_SOURCE_PATH)
TEMPLATES_PATH = plbuilder_path('templates')
templates_path_func = path_func(TEMPLATES_PATH)

create_dirs = [
    HANDOUTS_BUILD_PATH,
    DOCUMENTS_BUILD_PATH,
    SLIDES_BUILD_PATH,
]
for cd in create_dirs:
    if not os.path.exists(cd):
        os.makedirs(cd)
