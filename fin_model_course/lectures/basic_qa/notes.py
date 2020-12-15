from lectures.model import LectureNotes, Lecture, LectureResource
from resources.models import RESOURCES


def get_finstmt_q_a_12_14_2020_lecture() -> Lecture:
    title = 'finstmt Q&A 12/14/2020'
    youtube_id = 'qCxp4Hi2M1k'
    week_covered = 12
    notes = LectureNotes([
        'Should we be worried about the data that did not get extracted in finstmt?',
        'Could you show finstmt being used with xlwings?',
        'Is the copy function only in finstmt?',
        'Could you give an example of how to take specific values out of finstmt? E.g. the revenue for the '
        '3rd forecasted period.',
        'How can I see the effects of adjusting the financial statements manually?',
    ], title=title)
    resources = [
        RESOURCES.external.python.finstmt_documentation,
    ]
    notes_section_name = 'Questions'
    return Lecture(
        title, week_covered, notes, youtube_id=youtube_id, resources=resources, notes_section_name=notes_section_name
    )


def get_project_4_q_a_12_14_2020_lecture() -> Lecture:
    title = 'Project 4 Q&A 12/14/2020'
    youtube_id = 'Cxvc0qkwZFc'
    week_covered = 12
    notes = LectureNotes([
        'What are the variables I should include in the Monte Carlo simulation?',
        'Should I use annual or quarterly financial statements?',
        "How should I approach the write-up around the forecasting assumptions?",
    ], title=title)
    resources = []
    notes_section_name = 'Questions'
    return Lecture(
        title, week_covered, notes, youtube_id=youtube_id, resources=resources, notes_section_name=notes_section_name
    )