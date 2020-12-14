from lectures.model import LectureNotes, Lecture, LectureResource
from resources.models import RESOURCES


def get_debt_details_pipeline_lecture() -> Lecture:
    title = 'Creating a Data Loading Module for Capital IQ Debt Details'
    youtube_id = 'mL4hDzrvxL0'
    week_covered = 15
    notes = LectureNotes([
        'For the DCF model we have explored using the market value of individual debt instruments to estimate '
        'the market value of debt for the whole company',
        'For Project 3, we looked at using Capital IQ as the source of those debt details',
        'Here I examine how to automate the loading and cleaning of the debt details from Capital IQ, '
        'so they are ready to be worked with in the model',
        'I also look at taking the resulting code and making a Python module, so it can be reused in future models',
        'To clean up the data, I use a combination of Pandas methods, string methods, and regular '
        'expressions (regex)'
    ], title=title)
    resources = [
        RESOURCES.examples.data_pipeline.load_capiq_debt_module,
        RESOURCES.projects.project_3.wmt_debt_details,
        RESOURCES.examples.data_pipeline.pfizer_debt_details,
    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)



