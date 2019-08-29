from typing import Optional
import fire

from slidebuilder.builder import (
    create_all_presentations,
    create_presentation_by_number,
    create_presentation_by_file_name,
    get_next_presentation_number,
    create_presentation_template
)


def build(number: Optional[int] = None, file_name: Optional[str] = None):
    """
    Create slides and handout PDFs from slidebuilder pyexlatex templates.
    Passing no arguments will build all templates.

    :param number: number of template from which to build PDFs
    :param file_name: name of template from which to build PDFs
    :return: None
    """
    _validate_build(
        number=number,
        file_name=file_name
    )
    if number is None and file_name is None:
        create_all_presentations()
    if number is not None:
        create_presentation_by_number(number)
    if file_name is not None:
        create_presentation_by_file_name(file_name)


def _validate_build(**kwargs):
    if kwargs['number'] is not None and kwargs['file_name'] is not None:
        raise ValueError('only provide one of number and file_name')


def create(name: str):
    """
    Creates a slide template using the passed name

    :param name: Display name, will be standardized to snakecase and lowercase for use in the file name
    :return:
    """
    num = get_next_presentation_number()
    create_presentation_template(num, name)


if __name__ == '__main__':
    fire.Fire({
        'build': build,
        'create': create
    })
