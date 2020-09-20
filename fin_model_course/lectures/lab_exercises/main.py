from lectures.lab_exercise import LabExerciseGroup
from lectures.lab_exercises import notes
from lectures.model import LectureGroup, LectureResource


def get_lab_exercises_lecture() -> LabExerciseGroup:
    lecture_index = 'LS1'
    title = f'Lab Exercise Solutions'
    description = 'The solutions to all the lab exercises in the course.'
    resources = [

    ]
    lectures = [
        notes.get_simple_retirement_lab_lecture(),
        notes.get_extend_dynamic_retirement_excel_lab_lecture(),
        notes.get_python_basics_conditionals_lab_lecture(),
        notes.get_python_basics_lists_lab_lecture(),
        notes.get_python_basics_functions_lab_lecture(),
        notes.get_python_basics_data_types_lab_lecture(),
        notes.get_python_basics_classes_lab_lecture(),
        notes.get_extend_dynamic_retirement_python_lab_lecture(),
        notes.get_intro_to_pandas_lab_lecture(),
        notes.get_pandas_styling_lab_lecture(),
        notes.get_intro_python_visualization_lab_lecture(),
        notes.get_sensitivity_analysis_excel_lab_lecture(),
        notes.get_dictionaries_lab_lecture(),
        notes.get_list_comprehensions_lab_lecture(),
        notes.get_sensitivity_analysis_python_lab_lecture(),
        notes.get_scenario_analysis_excel_lab_lecture(),
        notes.get_scenario_analysis_python_lab_lecture(),
        notes.get_randomness_excel_lab_lecture(),
        notes.get_randomness_python_lab_lecture(),
        notes.get_random_stock_model_lab_lecture(),
        notes.get_extend_model_internal_randomness_lab_lecture(),
        notes.get_read_write_excel_pandas_lab_lecture(),
        notes.get_read_write_xlwings_lab_lecture(),
        notes.get_intro_monte_carlo_lab_lecture(),
        notes.get_python_retirement_monte_carlo_lab_lecture(),
        notes.get_excel_retirement_monte_carlo_lab_lecture(),
        notes.get_enterprise_value_lab_lecture(),
        notes.get_dcf_cost_equity_lab_lecture(),
        notes.get_dcf_cost_debt_lab_lecture(),
        notes.get_fcf_calculation_lab_lecture(),
        notes.get_simple_forecast_lab_lecture(),
        notes.get_complex_forecast_lab_lecture(),
        notes.get_dcf_tv_lab_lecture(),
    ]
    return LabExerciseGroup(title, description, lectures, order=lecture_index, global_resources=resources,
                            show_aggregate_resources=False)
