from build_tools.config import LAB_FOLDER_NAME
from lectures.model import LectureNotes, Lecture, LectureResource


def get_project_overview_lecture() -> Lecture:
    project_title = 'Project Grading Overview'
    project_num = 0
    title = f'Project {project_num} - {project_title}'
    youtube_id = 'SW4Yk-pQdA8'
    notes = LectureNotes([
        'The biggest part of the typical project grade is accuracy, but that only represents 60% of the total.',
        'Answers with the baseline model inputs are often provided, so use these to ensure you have built the model '
        'correctly. But you cannot rely on these alone. Your model needs to be able to work with any reasonable value '
        'for any input and adjust appropriately. After you have matched the baseline result, then start changing '
        'around the inputs and ensure that your model responds in a way that is logical and consistent with the '
        'change in the input.',
        'I have built out automated grading for the first three projects for the accuracy. It will tell me if '
        'everything in your model works properly. In order for this auto-grading to work properly, you need '
        'to conform to the expectations of the project, this is why I make following the template a separate grade.',
        'If the auto-grader finds that your model does not work properly, then I go through it in detail to understand '
        'where the issues are occurring. I fix the issues one by one until your model works properly. Then I give '
        'comments on where exactly you went wrong and take off points appropriately.',
        "Regardless of the auto-grading, I go through everyone's model line by line to assess the readability and "
        "formatting of the model."
    ], title=title)
    resources = [
        LectureResource(
            'Project Grading Overview',
            static_url=f'generated/pdfs/PJ{project_num} {project_title}.pdf'
        )
    ]
    return Lecture(title, notes, youtube_id=youtube_id, resources=resources)


def get_project_1_lecture() -> Lecture:
    project_title = 'Excel and Python TVM'
    project_num = 1
    title = f'Project {project_num} - {project_title}'
    youtube_id = 'vcvE5RrtrL4'
    notes = LectureNotes([
        'This project is really about cash flow modeling which is a huge part of financial modeling.',
        'This is a classic capital budgeting problem. Buy production capacity, produce units for variable '
        'cost, maximize NPV based on selecting the investment in production capacity and unit volume',
        'Leave the bonus for last. It is fairly separate from the rest of the problem. The bonus is really '
        'intended for the more advanced students coming in with Python or programming experience who did '
        'not have a hard time with the main project to provide some additional learning. Usually very few '
        'students complete the bonuses',
        'You are completing the entire project in both Excel and Python separately so we can understand '
        'the differences',
        'Please start as early as you can. This project has the highest learning curve and students who '
        'have waited to the last minute have ended up struggling in the entire course'
    ], title=title)
    resources = [
        LectureResource(
            f'Project {project_num} Description',
            static_url=f'generated/pdfs/PJ{project_num} {project_title}.pdf'
        ),
        LectureResource(
            f'Project {project_num} Excel Template',
            static_url=f'Project Materials/Project {project_num}/Project {project_num} Template.xlsx'
        ),
        LectureResource(
            f'Project {project_num} Python Template',
            static_url=f'Project Materials/Project {project_num}/Project {project_num} Template.ipynb'
        ),
    ]
    return Lecture(title, notes, youtube_id=youtube_id, resources=resources)


