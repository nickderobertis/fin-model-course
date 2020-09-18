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
    ]
    return LabExerciseGroup(title, description, lectures, order=lecture_index, global_resources=resources)
