from pyexlatex.models.presentation.beamer.templates.frames.two_col import TwoColumnGraphicDimRevealFrame
from slidebuilder.paths import images_path

TITLE = 'Financial Modeling with Python and Excel'
SHORT_TITLE = 'Intro'
SUBTITLE = 'An Introduction'


def get_frames():
    return [
        TwoColumnGraphicDimRevealFrame(
            [
                'This is a skills-based course focused on teaching financial modeling techniques in Python and Excel',
                'The focus is not a lot of specific models, but rather general model-building techniques',
                'The focus will be simple models, but extending them in powerful ways'
            ],
            graphic_filepaths=[
                images_path('python-logo.png'),
                images_path('excel-logo.png')
            ],
            title='What is this Class?'
        )
    ]