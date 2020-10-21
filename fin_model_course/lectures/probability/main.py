from lectures.probability import notes
from lectures.model import LectureGroup
from resources.models import RESOURCES
from schedule.main import LECTURE_8_NAME


def get_probability_lecture() -> LectureGroup:
    lecture_index = 8
    title = LECTURE_8_NAME
    description = 'Incorporate probabilities into models to be able to directly model uncertainty, and to ' \
                  'know not only the most likely outcome but ' \
                  'also the chance of different outcomes occurring.'
    resources = [
        *RESOURCES.lectures.probability.resources(),
    ]
    lectures = [
        notes.get_intro_probabilistic_modeling_lecture(),
        notes.get_probability_math_review_lecture(),
        notes.get_intro_scenario_analysis_lecture(),
        notes.get_excel_scenario_analysis_lecture(),
        notes.get_excel_scenario_analysis_lab_lecture(),
        notes.get_python_scenario_analysis_lecture(),
        notes.get_intro_internal_randomness_lecture(),
        notes.get_excel_internal_randomness_lecture(),
        notes.get_python_internal_randomness_lecture(),
        notes.get_continuous_randomness_lab_lecture(),
        notes.get_discrete_randomness_lecture(),
        notes.get_internal_randomness_retirement_excel_lecture(),
        notes.get_internal_randomness_retirement_python_lecture(),
        notes.get_internal_randomness_lab_overview_lecture()
    ]
    return LectureGroup(title, description, lectures, order=lecture_index, global_resources=resources)
