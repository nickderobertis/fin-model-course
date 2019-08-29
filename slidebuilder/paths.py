from typing import Callable
import functools
import os


def path_func(root_path: str) -> Callable:
    partial = functools.partial(os.path.join, root_path)
    return partial

SLIDEBUILDER_PATH = 'slidebuilder'
slidebuilder_path = path_func(SLIDEBUILDER_PATH)
ASSETS_PATH = os.path.sep.join(['slidebuilder', 'assets'])
assets_path = path_func(ASSETS_PATH)
IMAGES_PATH = assets_path('images')
images_path = path_func(IMAGES_PATH)
SLIDES_BUILD_PATH = 'Slides'
slides_build_path = path_func(SLIDES_BUILD_PATH)
HANDOUTS_BUILD_PATH = 'Handouts'
handouts_build_path = path_func(HANDOUTS_BUILD_PATH)
SLIDES_SOURCE_PATH = slidebuilder_path('slides')
slides_source_path = path_func(SLIDES_SOURCE_PATH)
SLIDE_TEMPLATE_PATH = slides_source_path('0_template.py')
