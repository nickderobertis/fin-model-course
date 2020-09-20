from lectures.dcf_cost_capital import notes
from lectures.model import LectureGroup
from resources.models import RESOURCES
from schedule.main import LECTURE_11_NAME


def get_dcf_cost_capital_lecture() -> LectureGroup:
    lecture_index = 11
    title = LECTURE_11_NAME
    description = 'Introduces the discounted cash flow (DCF) valuation of a stock. This lecture series ' \
                  'focuses on the cost of capital (WACC) side of the model.'
    resources = [
        *RESOURCES.lectures.dcf_cost_capital.resources(),
    ]
    lectures = [
        notes.get_intro_dcf_lecture(),
        notes.get_ev_lecture(),
        notes.get_intro_cost_of_equity_lecture(),
        notes.get_python_cost_of_equity_lecture(),
        notes.get_excel_cost_of_equity_lecture(),
        notes.get_mv_equity_lecture(),
        notes.get_intro_cost_of_debt_lecture(),
        notes.get_intro_mv_debt_lecture(),
        notes.get_mv_debt_python_lecture(),
        notes.get_wacc_lecture(),
    ]
    return LectureGroup(title, description, lectures, order=lecture_index, global_resources=resources)
