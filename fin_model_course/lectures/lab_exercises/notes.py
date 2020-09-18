from build_tools.config import LAB_FOLDER_NAME
from lectures.lab_exercise import LabExerciseLecture
from lectures.model import LectureNotes, Lecture, LectureResource
from lectures.python_basics.notes import LECTURE_4_COMMON_RESOURCES
from schedule.main import LECTURE_2_NAME, LECTURE_3_NAME, LECTURE_4_NAME

LAB_LECTURE_4_COMMON_RESOURCES = [
    LECTURE_4_COMMON_RESOURCES[1],
    LectureResource(f'Slides - {LECTURE_4_NAME}',
                    static_url=f'generated/pdfs/S4 {LECTURE_4_NAME}.pdf'),
]


def get_simple_retirement_lab_lecture() -> LabExerciseLecture:
    title = 'Extending a Simple Retirement Model'
    youtube_id = 'KVVabq4n-ow'
    notes = LectureNotes([

    ], title=title)
    resources = [
        LectureResource(
            'Simple Retirement Model Excel',
            static_url='Examples/Introduction/Excel/Simple Retirement Model.xlsx'
        ),
        LectureResource(
            'Simple Retirement Model Python',
            static_url='Examples/Introduction/Python/Simple Retirement Model.ipynb'
        ),
        LectureResource(f'Slides - {LECTURE_2_NAME}', static_url=f'generated/pdfs/S2 {LECTURE_2_NAME}.pdf'),
    ]
    return LabExerciseLecture(title, notes, youtube_id=youtube_id, resources=resources)


def get_extend_dynamic_retirement_excel_lab_lecture() -> LabExerciseLecture:
    title = 'Determining Desired Cash in the Dynamic Salary Retirement Excel Model'
    youtube_id = 'cM3uKsHXS3M'
    notes = LectureNotes([

    ], title=title)
    resources = [
        LectureResource(
            'Dynamic Salary Retirement Model - Excel',
            static_url='Examples/Introduction/Excel/Dynamic Salary Retirement Model.xlsx'
        ),
        LectureResource(f'Slides - {LECTURE_3_NAME}',
                        static_url=f'generated/pdfs/S3 {LECTURE_3_NAME}.pdf'),
    ]
    return LabExerciseLecture(title, notes, youtube_id=youtube_id, resources=resources)


def get_python_basics_conditionals_lab_lecture() -> LabExerciseLecture:
    title = 'Python Basics - Conditionals'
    youtube_id = 'T4LK0QgPbNA'
    notes = LectureNotes([

    ], title=title)
    resources = [
        *LAB_LECTURE_4_COMMON_RESOURCES,
    ]
    return LabExerciseLecture(title, notes, youtube_id=youtube_id, resources=resources)


def get_python_basics_lists_lab_lecture() -> LabExerciseLecture:
    title = 'Python Basics - Lists'
    youtube_id = 'AViA3IBpXcc'
    notes = LectureNotes([

    ], title=title)
    resources = [
        *LAB_LECTURE_4_COMMON_RESOURCES,
    ]
    return LabExerciseLecture(title, notes, youtube_id=youtube_id, resources=resources)


def get_python_basics_functions_lab_lecture() -> LabExerciseLecture:
    title = 'Python Basics - Functions'
    youtube_id = 'xOxJst-SMy8'
    notes = LectureNotes([

    ], title=title)
    resources = [
        *LAB_LECTURE_4_COMMON_RESOURCES,
    ]
    return LabExerciseLecture(title, notes, youtube_id=youtube_id, resources=resources)


def get_python_basics_data_types_lab_lecture() -> LabExerciseLecture:
    title = 'Python Basics - Data Types'
    youtube_id = 'pyjfrIzdjgo'
    notes = LectureNotes([

    ], title=title)
    resources = [
        *LAB_LECTURE_4_COMMON_RESOURCES,
    ]
    return LabExerciseLecture(title, notes, youtube_id=youtube_id, resources=resources)


def get_python_basics_classes_lab_lecture() -> LabExerciseLecture:
    title = 'Python Basics - Classes'
    youtube_id = 'znxtmT66UAM'
    notes = LectureNotes([

    ], title=title)
    resources = [
        *LAB_LECTURE_4_COMMON_RESOURCES,
        LectureResource(
            'Car Class Example',
            static_url='Examples/Introduction/Python/car_example.py'
        ),
    ]
    return LabExerciseLecture(title, notes, youtube_id=youtube_id, resources=resources)

def get_lecture() -> LabExerciseLecture:
    title = ''
    youtube_id = ''
    notes = LectureNotes([

    ], title=title)
    resources = [

    ]
    return LabExerciseLecture(title, notes, youtube_id=youtube_id, resources=resources)