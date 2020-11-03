from lectures.monte_carlo import notes
from lectures.model import LectureGroup
from resources.models import RESOURCES
from schedule.main import LECTURE_10_NAME


def get_monte_carlo_lecture() -> LectureGroup:
    lecture_index = 10
    title = LECTURE_10_NAME
    description = 'Assign probability distributions to inputs to be able to get probability distributions ' \
                  'of outputs. Enables a much deeper understanding of model results and especially the risk ' \
                  'of a result.'
    resources = [
        *RESOURCES.lectures.monte_carlo.resources(),
    ]
    lectures = [
        notes.get_intro_monte_carlo_lecture(),
        notes.get_mc_investment_returns_lecture(),
        notes.get_mc_ddm_lab_lecture(),
        notes.get_formal_mc_lecture(),
        notes.get_io_mc_lecture(),
        notes.get_mc_retirement_python_lecture(),
        notes.get_mc_retirement_excel_lecture(),
        notes.get_mc_retirement_excel_io_analysis_lecture(),
    ]
    return LectureGroup(title, description, lectures, order=lecture_index, global_resources=resources)
