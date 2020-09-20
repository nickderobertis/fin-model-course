from lectures.model import LectureNotes, Lecture, LectureResource
from resources.models import RESOURCES


def get_extending_simple_retirement_model_lecture() -> Lecture:
    title = 'Simple Retirement Model Assumptions'
    youtube_id = 'kSuy87EELWE'
    week_covered = 2
    notes = LectureNotes([
        'Part of the reason we begin with such a seemingly simple problem is to show '
        'how complex it is to model any real-world situation with a high degree of accuracy',
        'You may have thought we solved the retirement problem already, but there is '
        'a lot that we left out intentionally to make the problem simpler',
        'Assumptions are key to any model. They allow you to simplify the problem so it is '
        'actually feasible to solve. The stronger your assumptions, the less accurate the model, '
        'but the simpler it is to implement.',
        'No real-world model will ever be perfectly accurate. The world is just too complex to capture it all. '
        'We always have to settle for some level of assumptions',
        'The assumptions form the base of the model, from which we can generate the logic and equations',
        "There can be many different possible assumptions for a given model. It is a big part of the modeler's "
        "job to pick the best assumptions that can get the model as accurate as needed while balancing the costs "
        "of building and maintaining complex models"
    ], title=title)
    resources = []
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_relaxing_salary_assumption_lecture() -> Lecture:
    title = 'Relaxing the Salary Assumption'
    youtube_id = '_PuQgUIpMTg'
    week_covered = 2
    notes = LectureNotes([
        'We will experience first-hand the tradeoff in relaxing assumptions: greater accuracy '
        'but also greater complexity',
        'We are going to now a fairly realistic assumption for salary. It is still not however '
        'the most realistic possible. For example, promotions should be less frequent and '
        'smaller raises during recessions and more frequent/larger raises during expansionary periods. '
        'Promotions should not come at a fixed interval, they should be faster in the early stages '
        'of the career and there should be randomness to it. The model should be run many times '
        'to understand the distribution of years to retirement based on the randomness in the salary.',
        "Obviously that would lead to quite a complex model already, and that's only thinking about "
        "the salary assumption.",
        'In deciding how much to relax assumptions, the desired degree of accuracy of the model is '
        'critically important. For what decisions is the model being used? Will those decisions be any '
        'different if the model increases in accuracy? What is the cost of being wrong?'
    ], title=title)
    resources = []
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_advanced_excel_functions_lecture() -> Lecture:
    title = 'Skills for the Advanced Excel Model'
    youtube_id = 'iRrVYz_cips'
    week_covered = 2
    notes = LectureNotes([
        'Larger Excel models can get very messy quickly. Then it becomes difficult for anyone to '
        'consume your model or to improve it later. Therefore it is important to stay organized.',
        'As before, we want to keep the inputs separate from the outputs. But in a larger model, we '
        'need to take this a step further. We can break the model into various parts or stages, each '
        'which have their own inputs and outputs. Each part should have its own dedicated worksheet and '
        'there should be an overview page which has the main inputs and outputs.',
        'Conditionals are necessary to control the flow and output of a model under different conditions. We '
        'use =IF, =AND, =OR in Excel to accomplish this',
        'Use modulo (=MOD) to get the division remainder. You might not need this every day in modeling but '
        'it is very useful for this particular salary situation we are modeling',
        '=VLOOKUP is very useful to find items in a table and can make your model much more flexible'
    ], title=title)
    resources = []
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_implement_dynamic_salary_excel_lecture() -> Lecture:
    title = 'Implementing the Dynamic Salary Model'
    youtube_id = 'uU3Za6p3KJs'
    week_covered = 2
    notes = LectureNotes([
        'We are building this model from scratch as it is so different from the original',
        'We can break this larger problem down into three sub-problems: determining '
        'salary over time, determining wealth over time, and determining when the '
        'individual can retire. Each of these become worksheets in the model',
        'In the overall inputs, it is good to have sections if inputs are relevant '
        'only to individual sub-problems. Also reference over the inputs onto the '
        'individual sheet for both visual organization of having everything for the '
        'calculation on one sheet as well as keeping cell references shorter',
        '=IF and =MOD combined can figure out whether it is a promotion year',
        'A cumulative sum can be used to determine how many promotions have occurred '
        'up until a given point in time',
        'Calculating factors helps split out the calculation and make it more clear'
    ], title=title)
    resources = [
        RESOURCES.examples.intro.excel.dynamic_salary_retirement_model,
    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_lab_excercise_lecture() -> Lecture:
    title = 'Lab Exercise'
    youtube_id = 'CqsIz00OH38'
    week_covered = 2
    notes = LectureNotes([
        'Feel free to work from the example model though I would recommend you '
        'build that out yourself following the prior videos',
        'The new calculation being added is simple, with the main focus being '
        'adding new functionality to an existing model and keeping it '
        'organized',
        'Hint: if you cut the desired cash cell (Ctrl/Cmd + x), you can move it from '
        'the inputs into a calculation area and retain all the references to it'
    ], title=title)
    resources = []
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)
