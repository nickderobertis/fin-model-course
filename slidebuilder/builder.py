from typing import Sequence
import importlib.util
import os
from copy import deepcopy
from pyexlatex.presentation import Frame
from slidebuilder.base import FinancialModelingPresentation
from slidebuilder.paths import SLIDES_BUILD_PATH, SLIDES_SOURCE_PATH, slides_source_path, HANDOUTS_BUILD_PATH

IGNORED_SLIDES = [
    '__init__.py',
    '0_template.py'
]


def create_all_presentations():
    presentation_files = [file for file in next(os.walk(SLIDES_SOURCE_PATH))[2] if file not in IGNORED_SLIDES]
    [create_presentation_by_file_name(file) for file in presentation_files]


def create_presentation_by_file_name(file_name: str):
    print(f'Creating presentation for {file_name}')
    file_path = slides_source_path(file_name)
    mod = _module_from_file(file_path)
    create_presentation(
        mod.get_frames(),
        title=mod.TITLE,
        short_title=mod.SHORT_TITLE,
        subtitle=mod.SUBTITLE,
        index=int(file_name[0])
    )


def create_presentation_by_number(num: int):
    presentation_files = [file for file in next(os.walk(SLIDES_SOURCE_PATH))[2] if file not in IGNORED_SLIDES]
    presentation_split_files = [file.split('_') for file in presentation_files]
    for split_file in presentation_split_files:
        num_str = split_file[0]
        name = '_'.join(split_file[1:])
        if int(num_str) == num:
            file_name = '_'.join([num_str, name])
            create_presentation_by_file_name(file_name)
            break


def create_presentation(frames: Sequence[Frame], title: str, short_title: str, subtitle: str,
                        index: int = 1) -> FinancialModelingPresentation:
    out_name = f'{index} {title}'
    kwargs = dict(
        title=title,
        short_title=short_title,
        subtitle=subtitle
    )
    fmp = FinancialModelingPresentation(
        frames,
        **kwargs
    )
    fmp.to_pdf(
        SLIDES_BUILD_PATH,
        out_name
    )
    fmp_handout = FinancialModelingPresentation(
        frames,
        handouts=True,
        **kwargs
    )
    fmp_handout.to_pdf(
        HANDOUTS_BUILD_PATH,
        out_name
    )


def _module_from_file(file_path: str):
    mod_name = os.path.basename(file_path).strip('.py')
    return _module_from_file_and_name(file_path, mod_name)


def _module_from_file_and_name(file_path: str, module_name: str):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


if __name__ == '__main__':
    create_all_presentations()