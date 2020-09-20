from lectures.model import LectureNotes, Lecture, LectureResource
from resources.models import RESOURCES


def get_intro_fcf_lecture() -> Lecture:
    title = 'Introduction to Free Cash Flows'
    youtube_id = ''
    week_covered = 12
    notes = LectureNotes([

    ], title=title)
    resources = []
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_historical_fcf_lecture() -> Lecture:
    title = 'Introduction to Calculating Historical Free Cash Flows'
    youtube_id = ''
    week_covered = 12
    notes = LectureNotes([

    ], title=title)
    resources = [
        RESOURCES.labs.dcf.fcf.wmt_income_statement,
        RESOURCES.labs.dcf.fcf.wmt_balance_sheet,
    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_historical_fcf_python_lecture() -> Lecture:
    title = 'Historical Free Cash Flows in Python'
    youtube_id = ''
    week_covered = 12
    notes = LectureNotes([

    ], title=title)
    resources = [
        *RESOURCES.examples.dcf.historical_fcf.resources(),
    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_intro_forecasting_lecture() -> Lecture:
    title = 'Introduction to Forecasting'
    youtube_id = ''
    week_covered = 12
    notes = LectureNotes([

    ], title=title)
    resources = [
    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_simple_forecasting_lecture() -> Lecture:
    title = 'Simple Time-Series Forecasting Models'
    youtube_id = ''
    week_covered = 12
    notes = LectureNotes([

    ], title=title)
    resources = [
    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_simple_forecasting_excel_lecture() -> Lecture:
    title = 'Simple Time-Series Forecasting in Excel'
    youtube_id = ''
    week_covered = 12
    notes = LectureNotes([

    ], title=title)
    resources = [
        RESOURCES.examples.dcf.forecasting.simple.sales_cogs_xlsx,
        RESOURCES.examples.dcf.forecasting.simple.sales_cogs_forecasted_xlsx,
    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_simple_forecasting_python_lecture() -> Lecture:
    title = 'Simple Time-Series Forecasting in Python'
    youtube_id = ''
    week_covered = 12
    notes = LectureNotes([

    ], title=title)
    resources = [
        RESOURCES.examples.dcf.forecasting.simple.forecast_simple_notebook,
        RESOURCES.examples.dcf.forecasting.simple.forecast_finstmt_notebook,
        RESOURCES.examples.dcf.forecasting.simple.cat_bs,
        RESOURCES.examples.dcf.forecasting.simple.cat_inc,
    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_simple_forecasting_lab_overview_lecture() -> Lecture:
    title = 'Simple Time-Series Forecasting Lab Overview'
    youtube_id = ''
    week_covered = 12
    notes = LectureNotes([

    ], title=title)
    resources = [
        RESOURCES.labs.dcf.forecasting.simple.debt_interest
    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_complex_forecasting_lecture() -> Lecture:
    title = 'Complex Time-Series Forecasting'
    youtube_id = ''
    week_covered = 13
    notes = LectureNotes([

    ], title=title)
    resources = [

    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_complex_forecasting_python_manual_lecture() -> Lecture:
    title = 'Complex Time-Series Forecasting in Python - Manual Method'
    youtube_id = ''
    week_covered = 13
    notes = LectureNotes([

    ], title=title)
    resources = [
        *RESOURCES.examples.dcf.forecasting.complex.resources(),
    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_complex_forecasting_python_finstmt_lecture() -> Lecture:
    title = 'Complex Time-Series Forecasting in Python - finstmt Method'
    youtube_id = ''
    week_covered = 13
    notes = LectureNotes([

    ], title=title)
    resources = [
        *RESOURCES.examples.dcf.forecasting.complex.resources(),
    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_complex_forecasting_lab_overview_lecture() -> Lecture:
    title = 'Complex Time-Series Forecasting Lab Overview'
    youtube_id = ''
    week_covered = 13
    notes = LectureNotes([

    ], title=title)
    resources = [
        *RESOURCES.labs.dcf.forecasting.complex.resources(),
    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_fcf_forecasting_lecture() -> Lecture:
    title = 'Applying Forecasting to Free Cash Flows'
    youtube_id = ''
    week_covered = 13
    notes = LectureNotes([

    ], title=title)
    resources = [

    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_tv_lecture() -> Lecture:
    title = 'Calculating a Terminal Value'
    youtube_id = ''
    week_covered = 13
    notes = LectureNotes([

    ], title=title)
    resources = [

    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)