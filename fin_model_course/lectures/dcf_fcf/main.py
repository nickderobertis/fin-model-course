from lectures.dcf_fcf import notes
from lectures.model import LectureGroup
from resources.models import RESOURCES
from schedule.main import LECTURE_12_NAME


def get_dcf_fcf_lecture() -> LectureGroup:
    lecture_index = 12
    title = LECTURE_12_NAME
    description = 'Continues discussion of DCF valuation. This lecture series ' \
                  'focuses on the free cash flow (FCF) side of the model. General forecasting material ' \
                  'is included to be able to forecast FCFs.'
    resources = [
        *RESOURCES.lectures.dcf_fcf.resources(),
    ]
    lectures = [
        notes.get_intro_fcf_lecture(),
        notes.get_historical_fcf_lecture(),
        notes.get_historical_fcf_python_lecture(),
        notes.get_intro_forecasting_lecture(),
        notes.get_simple_forecasting_lecture(),
        notes.get_simple_forecasting_excel_lecture(),
        notes.get_simple_forecasting_python_lecture(),
        notes.get_simple_forecasting_lab_overview_lecture(),
        notes.get_complex_forecasting_lecture(),
        notes.get_complex_forecasting_python_manual_lecture(),
        notes.get_complex_forecasting_python_finstmt_lecture(),
        notes.get_complex_forecasting_lab_overview_lecture(),
        notes.get_fcf_forecasting_lecture(),
        notes.get_tv_lecture(),
    ]
    return LectureGroup(title, description, lectures, order=lecture_index, global_resources=resources)
