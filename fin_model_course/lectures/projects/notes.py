from build_tools.config import LAB_FOLDER_NAME
from lectures.model import LectureNotes, Lecture, LectureResource
from resources.models import RESOURCES


def get_project_overview_lecture() -> Lecture:
    project_title = 'Project Grading Overview'
    project_num = 0
    title = f'Project {project_num} - {project_title}'
    youtube_id = 'SW4Yk-pQdA8'
    week_covered = 2
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
        RESOURCES.projects.grading_overview,
    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_project_1_lecture() -> Lecture:
    project_title = 'Excel and Python TVM'
    project_num = 1
    title = f'Project {project_num} - {project_title}'
    youtube_id = 'vcvE5RrtrL4'
    week_covered = 2
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
        *RESOURCES.projects.project_1.resources(),
    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_project_2_lecture() -> Lecture:
    project_title = 'Probabilistic Loan Pricing'
    project_num = 2
    title = f'Project {project_num} - {project_title}'
    youtube_id = 'Jxuuw8mM-vQ'
    week_covered = 7
    notes = LectureNotes([
        'The focus of this project is to reinforce probabilistic modeling and to solve a common '
        'problem faced by lenders: deciding the loan terms to offer',
        'This project also tests your ability to explore the parameter space and visualize the results, '
        'extending the base model',
        'This model typically incorporates internal randomness. This means you will get a different result each time '
        'you run your model. You can increase the number of iterations to get a more consistent result, but '
        'it will also take longer for the model to run. When checking your answers against the provided solutions, they '
        'will not match exactly, but as you run the model multiple times each number should be similar to the reported '
        'answers. When you are ready to submit the model, run it with '
        '1000 iterations and be sure to allow time for this',
        'This project, and the remaining projects going forward in the course, may be submitted as an '
        'Excel model, a Python model, or a combination model that uses both Python and Excel',
        'It is up to you how you want to structure the model and which tools to use, but this problem is '
        'difficult to solve using only Excel. If you want to work in Excel as much as possible, I would '
        'recommend building the base deterministic model in Excel then handle the randomness and exploring '
        'the parameter space using Python',
        'As always, save the bonus for last, though students have generally found this bonus exercise easier than '
        'that of the first project',
    ], title=title)
    resources = [
        *RESOURCES.projects.project_2.resources(),
    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_project_3_lecture() -> Lecture:
    project_title = 'Monte Carlo Cost of Capital'
    project_num = 3
    title = f'Project {project_num} - {project_title}'
    youtube_id = '1mlVhKn81DY'
    week_covered = 10
    notes = LectureNotes([
        'The focus of this project is to start working towards the Discounted Cash Flow (DCF) valuation '
        'of a stock. The weighted average cost of capital (WACC) is a component of that model',
        'This project also tests your ability to carry out a Monte Carlo simulation',
        'Project 4 will be the full DCF valuation, which means it will include doing this analysis again '
        'for a different company. I encourage you to write general functions that will be useful for both, '
        'and after this project you can move those functions into a separate file so they can be shared',
        'This is also our first project that requires working with external data',
        'You can feel free to modify any of the data files. If you do modify them, then submit them along '
        'with your project. If you did not modify the file, leave it out of the submission',
        'To earn the bonus, complete the project without modifying any data files. I would recommend saving '
        'this for last as it will be a substantial challenge. If you plan to do the bonus, as you modify the '
        'files for your model, take note of every manual step that you take so you can try to automate it later',
        'Please see the project description for some links to extra resources to help you automate the data cleanup',
        'As with Project 2 and the remaining projects in the course, you are free to submit a Python model, Excel '
        'model, or combination Python/Excel model. The only requirement is if you do submit a combination model, '
        'the final outputs should be in Python',
    ], title=title)
    resources = [
        *RESOURCES.projects.project_3.resources(),
    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)
