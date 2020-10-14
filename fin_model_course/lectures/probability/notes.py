from lectures.model import LectureNotes, Lecture, LectureResource
from resources.models import RESOURCES


def get_intro_probabilistic_modeling_lecture() -> Lecture:
    title = 'Introduction to Probabilistic Modeling'
    youtube_id = 'OvLatB0ax1Y'
    week_covered = 7
    notes = LectureNotes([
        'Probability is a key concept for financial models as it related to risk',
        'The base result from a deterministic model only gives a single answer, but does not '
        'consider the probability distribution of the result',
        'E.g. your model could predict a positive NPV from a project, but through probabilistic '
        'modeling you determine that there is a 98% chance the NPV is negative. Do you still want to '
        'take the project? This is important information to know when making that decision.',
        'We discuss three techniques in this course that take advantage of probability theory: '
        'scenario modeling, internal randomness, and Monte Carlo simulation',
        'Scenario modeling and Monte Carlo simulation are also methods of exploring the parameter '
        'space, just like sensitivity analysis',
        'Internal randomness is useful for when the probability is so core to the model that it '
        'should be built in from the beginning, rather than extending the base model to add probability'
    ], title=title)
    resources = []
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_probability_math_review_lecture() -> Lecture:
    title = 'Math Review for Probabilistic Modeling'
    youtube_id = '2OIjIrtUERQ'
    week_covered = 7
    notes = LectureNotes([
        'Discrete variables: specific values, continuous variables: range of values. Note that an underlying '
        'variable can be continuous but the modeler can choose to make it discrete within the model to '
        'simplify it. E.g. condition of the economy is continuous, but you might make it discrete by '
        'classifying the economic conditions into recession, neutral, or expansion. This does not work in the '
        'other direction: a variable which is truly discrete cannot be made continuous',
        'Expected value is a key concept in probability theory. We will use it in scenario analysis to get '
        'the expected outcome across multiple different cases of the inputs',
        'The variance graph shows two series with the same mean but different variances. Variance is a measure '
        'of how much the value is moving around. If it moves a lot, it has high variance. Variance has nothing '
        'to do with the average, mean, or expected value.',
        'Probability distributions tell you how likely it is to observe different values of a given variable',
        'Discrete variables: think table of values with probabilities. Continuous variables: think curve, '
        'usually displayed by a graph but defined by a function',
        'The CLT is extremely powerful, because of it most of the distributions for continuous variables '
        'are normal distributions. So if we need to pick a distribution for a variable, the normal distribution '
        'is reasonable choice the majority of the time'
    ], title=title)
    resources = []
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_intro_scenario_analysis_lecture() -> Lecture:
    title = 'Introduction to Scenario Analysis'
    youtube_id = 'ipxSUXZY5hk'
    week_covered = 7
    notes = LectureNotes([
        'Scenario modeling is another way to explore the parameter space, just like sensitivity analysis',
        'Scenario modeling is carried out in the same way as sensitivity analysis: run the model with '
        'each set of inputs and display the outputs with the inputs',
        'The difference is that unlike in sensitivity analysis where we tweak one input at a time, in '
        'scenario analysis, we consider some situations and determine all the values of the inputs that '
        'align with each situation',
        'We can also optionally assign probabilities to the situations, then take an expected value '
        'to get an expected outcome from our model',
        'Internal vs. external scenario analysis is just about whether the scenarios are included in the '
        'core model (internal), or as an extension to the base model (external)'
    ], title=title)
    resources = []
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_excel_scenario_analysis_lecture() -> Lecture:
    title = 'Scenario Analysis in Excel'
    youtube_id = 'MfqFV00GVD4'
    week_covered = 7
    notes = LectureNotes([
        'We will focus on external scenario analysis for the purpose of this exercise',
        'Typically if the model has already been created, you should opt for external '
        'rather than internal',
        'Unfortunately without some hacks, in Excel we are limited to examining two inputs '
        'changing at once with external scenario analysis, as a data table is used '
        'to run the model repeatedly',
        'We will see that we do not have this limitation in Python, and later in the course '
        'we will see that you can use Python to run external scenario analysis on your Excel '
        'model with any number of inputs'
    ], title=title)
    resources = [
        RESOURCES.examples.scenario.excel.dynamic_salary_model_scenario,
    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_excel_scenario_analysis_lab_lecture() -> Lecture:
    title = 'Lab Exercise - Adding Scenario Analysis to Project 1 - Excel'
    youtube_id = 'i7yO_o8tRyc'
    week_covered = 7
    notes = LectureNotes([
        'Here we are adding external scenario analysis to the Project 1 Excel model',
        'The process should be basically identical to what was shown in extending the '
        'Dynamic Salary Retirement Model in Excel',
    ], title=title)
    resources = [
    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_python_scenario_analysis_lecture() -> Lecture:
    title = 'Scenario Analysis in Python'
    youtube_id = ''
    week_covered = 8
    notes = LectureNotes([

    ], title=title)
    resources = [
        RESOURCES.examples.scenario.python.dynamic_salary_model_scenario,
    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_intro_internal_randomness_lecture() -> Lecture:
    title = 'Introduction to Internal Randomness'
    youtube_id = ''
    week_covered = 8
    notes = LectureNotes([

    ], title=title)
    resources = [

    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_excel_internal_randomness_lecture() -> Lecture:
    title = 'Intro to Randomness in Excel'
    youtube_id = ''
    week_covered = 8
    notes = LectureNotes([

    ], title=title)
    resources = [
        RESOURCES.examples.internal_randomness.excel.generate_numbers,
    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_python_internal_randomness_lecture() -> Lecture:
    title = 'Intro to Randomness in Python'
    youtube_id = ''
    week_covered = 8
    notes = LectureNotes([

    ], title=title)
    resources = [
        RESOURCES.examples.internal_randomness.python.generate_numbers,
    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_discrete_randomness_lecture() -> Lecture:
    title = 'Discrete Randomness'
    youtube_id = ''
    week_covered = 8
    notes = LectureNotes([

    ], title=title)
    resources = [
        RESOURCES.examples.internal_randomness.excel.generate_numbers,
        RESOURCES.examples.internal_randomness.python.generate_numbers,
    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_internal_randomness_retirement_excel_lecture() -> Lecture:
    title = 'Adding Internal Randomness to an Excel Model'
    youtube_id = ''
    week_covered = 9
    notes = LectureNotes([

    ], title=title)
    resources = [
        RESOURCES.examples.internal_randomness.excel.dynamic_salary_model_random,
    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_internal_randomness_retirement_python_lecture() -> Lecture:
    title = 'Adding Internal Randomness to a Python Model'
    youtube_id = ''
    week_covered = 9
    notes = LectureNotes([

    ], title=title)
    resources = [
        RESOURCES.examples.internal_randomness.python.dynamic_salary_model_random,
    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_internal_randomness_lab_overview_lecture() -> Lecture:
    title = 'Internal Randomness Lab Exercises Overview'
    youtube_id = ''
    week_covered = 9
    notes = LectureNotes([

    ], title=title)
    resources = [

    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)