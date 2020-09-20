from lectures.model import LectureNotes, Lecture, LectureResource
from resources.models import RESOURCES


def get_intro_dcf_lecture() -> Lecture:
    title = 'Introduction to Discounted Cash Flow (DCF) Valuation'
    youtube_id = ''
    week_covered = 11
    notes = LectureNotes([

    ], title=title)
    resources = []
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_ev_lecture() -> Lecture:
    title = 'Enterprise Value and Equity Value'
    youtube_id = ''
    week_covered = 11
    notes = LectureNotes([

    ], title=title)
    resources = []
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_intro_cost_of_equity_lecture() -> Lecture:
    title = 'Introduction to Cost of Equity'
    youtube_id = ''
    week_covered = 11
    notes = LectureNotes([

    ], title=title)
    resources = []
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_python_cost_of_equity_lecture() -> Lecture:
    title = 'Cost of Equity in Python'
    youtube_id = ''
    week_covered = 11
    notes = LectureNotes([

    ], title=title)
    resources = [
        RESOURCES.examples.dcf.cost_of_equity.python_coe,
        RESOURCES.examples.dcf.cost_of_equity.price_data,
    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_excel_cost_of_equity_lecture() -> Lecture:
    title = 'Cost of Equity in Excel'
    youtube_id = ''
    week_covered = 11
    notes = LectureNotes([

    ], title=title)
    resources = [
        RESOURCES.examples.dcf.cost_of_equity.excel_coe,
    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_mv_equity_lecture() -> Lecture:
    title = 'Market Value of Equity'
    youtube_id = ''
    week_covered = 11
    notes = LectureNotes([

    ], title=title)
    resources = [
    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_intro_cost_of_debt_lecture() -> Lecture:
    title = 'Introduction to Cost of Debt'
    youtube_id = ''
    week_covered = 11
    notes = LectureNotes([

    ], title=title)
    resources = []
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_intro_mv_debt_lecture() -> Lecture:
    title = 'Introduction to Market Value of Debt'
    youtube_id = ''
    week_covered = 11
    notes = LectureNotes([

    ], title=title)
    resources = []
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_mv_debt_python_lecture() -> Lecture:
    title = 'Calculating the Market Value of Debt in Python'
    youtube_id = ''
    week_covered = 11
    notes = LectureNotes([

    ], title=title)
    resources = [
        *RESOURCES.examples.dcf.cost_of_debt.resources(),
    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_wacc_lecture() -> Lecture:
    title = 'Calculating the Weighted Average Cost of Capital (WACC)'
    youtube_id = ''
    week_covered = 11
    notes = LectureNotes([

    ], title=title)
    resources = [

    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)