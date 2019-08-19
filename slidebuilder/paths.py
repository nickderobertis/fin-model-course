from typing import Callable
import functools
import os


def path_func(root_path: str) -> Callable:
    partial = functools.partial(os.path.join, root_path)
    return partial


ASSETS_PATH = os.path.sep.join(['slidebuilder', 'assets'])
assets_path = path_func(ASSETS_PATH)
IMAGES_PATH = assets_path('images')
images_path = path_func(IMAGES_PATH)
