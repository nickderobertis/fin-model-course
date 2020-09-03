import pyexlatex as pl
import pyexlatex.table as lt
import pyexlatex.presentation as lp
import pyexlatex.graphics as lg
import pyexlatex.layouts as ll

import plbuild
from plbuild.paths import images_path
from schedule.main import PROJECT_2_NAME

AUTHORS = ['Nick DeRobertis']

DOCUMENT_CLASS = pl.Document
OUTPUT_LOCATION = plbuild.paths.DOCUMENTS_BUILD_PATH
HANDOUTS_OUTPUT_LOCATION = None

TITLE = PROJECT_2_NAME
ORDER = 'PJ2'


def get_content():
    inputs = dict(
        price_machine=('$price_{machine}$', 1000000),
        loan_life=('$n_{life}$', 5),
        initial_default_prob=('$p_1^{default}$', 0.2),
        default_prob_decay=('$Decay_{default}$', 0.9),
        final_default_prob=('$p_n^{default}$', 0.4),
        recovery_rate=('$r_{recovery}$', 0.4),
    )

    inputs_content = pl.OrderedList(
        [f'{input_name}: {input_value}' for input_key, (input_name, input_value) in inputs.items()]
    )

    initial_default_prob_cases = [0.1, 0.3]
    initial_default_prob_cases_str = ', '.join([str(case) for case in initial_default_prob_cases])
    bonus_initial_default_prob_mean = inputs['initial_default_prob'][1]
    bonus_initial_default_prob_std = 0.05

    # TODO [#11]: update output values
    outputs = dict(
        interest_rate=('$r_{interest}$', 0.1),
        default_prob_t=('$p_t^{default}$', 0),
        default_prob_t_minus_1=('$p_{t-1}^{default}$', 0),
    )

    # tuple is (offered rate, default prob)
    solutions = {
        (0.2, 0.2): -0.03,
        (0.2, 0.3): -0.09,
        (0.4, 0.2): 0.13,
        (0.4, 0.3): 0
    }

    solutions_list = [f'With ${outputs["interest_rate"][0].strip("$")} = {tup[0]}$, ' \
                      f'${inputs["initial_default_prob"][0].strip("$")} = {tup[1]}$: {solution:.0%} IRR'
                      for tup, solution in solutions.items()]

    case_solutions = {
        'Default in $t=1$': -.2632,
        'Default in $t=2$': -.1496,
        'Default in $t=3$': -.0643,
        'Default in $t=4$': 0,
        'Default in $t=5$': 0.0482,
        'No Default': .2
    }

    case_solutions_list = [f'{key}: {value:.2%}' for key, value in case_solutions.items()]

    align_c = lt.ColumnAlignment('c')
    align_l = lt.ColumnAlignment('l')
    align = lt.ColumnsAlignment([align_l, align_c])

    default_prob_eq_str = f'{outputs["default_prob_t"][0].strip("$")} = {outputs["default_prob_t_minus_1"][0].strip("$")} ' \
                          f'{inputs["default_prob_decay"][0].strip("$")}'

    recovery_eq_str = f'{inputs["recovery_rate"][0].strip("$")}{inputs["price_machine"][0].strip("$")}'

    default_prob_cases_eq_str = f'{inputs["initial_default_prob"][0].strip("$")} = {initial_default_prob_cases_str}'

    problem_definition_pre_prob = f"""
    You work for a bank who is considering loaning funds to a small manufacturing business. The business needs 
    {inputs["price_machine"][0]} to buy machinery. The business would like to borrow the funds for 
    {inputs["loan_life"][0]}, and at that time it will repay {inputs["price_machine"][0]} in full. Interest is 
    paid annually at a rate of {outputs["interest_rate"][0]} (in the final period, both 
    {inputs["price_machine"][0]} and interest at the rate of {outputs["interest_rate"][0]} will be paid). As this is a small 
    business, there is significant default risk, but that default risk decreases over time as the business 
    matures. The probability of default in the first year is {inputs["initial_default_prob"][0]}, and then each 
    year thereafter it is:
    """

    problem_definition_post_prob = f"""
    Finally, the default probability is different in the final year, as it is the repayment year. The business has to
    pay a lot more in this period so there is a greater likelihood it can't come up with the funds. In the final year,
    (at year {inputs["loan_life"][0]}), the default probability is {inputs["final_default_prob"][0]}. 
    
    When the business defaults, then the default
    covenants of the loan trigger bankruptcy for the borrower, and the borrower must pay as much as it can on the loan 
    in the bankruptcy process. The bankruptcy process takes two years, and then once it is resolved, the lender will 
    collect {inputs["recovery_rate"][0]}% of {inputs["price_machine"][0]}. For the year of default and the year after,
    the lender will not collect any cash flows, and then two years after default, the lender will collect 
    {pl.Equation(str_eq=recovery_eq_str)}. Note that this means the number of years of cash flows may be up to two
    years greater than the life of the loan.
    """

    main_q_str = f"""
    You are the commercial loan analyst trying to decide if this loan makes sense for the bank. You want to give the
    lending officer all the information she would need to negotiate a rate for this loan.
    
    Given the inputs, what is the expected IRR of the loan for a variety of interest rates on the loan? The lending
    officer would like you to evaluate rates in 5% increments from 30% to 40%.
    
    The lending officer is also worried that she may have estimated {inputs["initial_default_prob"][0]} incorrectly. 
    She is hoping for the answers to the above questions considering that {inputs["initial_default_prob"][0]} may vary.
    Evaluate the above questions for {pl.Equation(str_eq=default_prob_cases_eq_str)} in addition to the base case 
    of {inputs["initial_default_prob"][1]}.

    Finally, the lending officer is unsure for how long she should extend the loan. So she would like to see all
    of the previously mentioned results with loan lifes of 5, 10, and 20 years.

    You should visualize the results of your model through graphs, conditional formatting, etc.
    """

    notes = [
    f"""
    You may assume a maximum loan life of 20 years in your model, which would make up to 22 years of cash flows.
    """,
    "Probably the easiest approach to building this model will use internal randomness. Though it certainly is "
    "possible to build this model using only "
    "expected values, I think that is generally more difficult.",
    "With the internal randomness approach, make sure you set the number of "
    "iterations to 1,000 per set of inputs to get a good estimate. ",
    "While you are testing things out, set it lower, such as 10 or 100, to have it run quicker, but beware that the lower "
    "your number of iterations, the less consistent the results will be.",
    'Also beware that with 1,000 iterations as required for the final submission, it may take over an hour to '
    'run the model, so plan for that time.',
    "You may choose to either submit a pure Python model, pure Excel model, or a combination of the two. If you use "
    "both, then the Python model should be what I ultimately run and extract results from. The Python model would "
    "be running the Excel model many times and extracting the results.",
    "Upon reading the prior note, you may think to implement in pure Excel because of greater familiarity, but I think "
    "you will find meeting the objective of running the model repeatedly with three changing inputs quite difficult. "
    "You need to run your model 27,000 times in total with three inputs changing together.",

    'Your answers may differ slightly from those in the Selected Solutions section. This is the nature of a random model. They '
    'should be very close with 1,000 iterations, though.',
    'Do not move any of the input or output cells. ',
    ]

    bonus_q_str = f"""
    Especially good visualization of the original problem will earn part of the bonus.
    
    Further, produce the same outputs as the main problem, but instead of evaluating 
    {pl.Equation(str_eq=default_prob_cases_eq_str)}, consider {inputs["initial_default_prob"][0]} as being normally
    distributed with mean {bonus_initial_default_prob_mean} and standard deviation {bonus_initial_default_prob_std}.

    Also examine a single selected input case with different numbers of iterations, producing visualizations and 
    summary statistics of the results with different numbers of iterations, to show how precise the expected IRR 
    estimates are.
    """

    submission_str = f"""
    Work off of the "Project 2 Template.xlsx" and "Project 2 Template.ipynb" files on Canvas. 

    Again it is up to you whether you submit a pure Python, pure Excel, or combination model. For whichever tools
    you use, you should use the templates, so those submitting a combination model will submit both a Jupyter notebook
    and an Excel workbook, both based off the templates. With the combination model, your ultimate answer should be
    in the Jupyter notebook.
    """

    solutions_str = """
    The below solutions are with the base case inputs provided. Your model will also need to be able to adjust for
    different inputs. Try changing the inputs and verify that the model changes in the way it should respond. Do 
    this for all the inputs. Note that your solution may differ significantly from mine due to the random nature of the 
    model. Run your model with 1,000 iterations to get a decent check (this will take about 10 minutes). Even then it may be 
    off by up to a couple percentage points.
    """

    case_solutions_str = """
    I am also providing the IRRs for each possible default situation in the model with base case inputs 
    and a 20% interest rate. This way you
    can check your model without having to run lots of iterations. Make sure that your model can reproduce each of the
    IRRs corresponding to each default case, and then you will only need the full solutions to check that the probabilities
    are set correctly. Note that unlike the full solutions, you should be able to match these default case solutions 
    exactly.
    """

    return [
        pl.Section(
            [
                pl.SubSection(
                    [
                        problem_definition_pre_prob,
                        pl.Equation(str_eq=default_prob_eq_str, inline=False),
                        problem_definition_post_prob
                    ],
                    title='Problem Definition'
                ),
                pl.SubSection(
                    [
                        main_q_str
                    ],
                    title='Main Question'
                ),
                pl.SubSection(
                    [
                        pl.UnorderedList(notes)
                    ],
                    title='Notes'
                ),
                pl.SubSection(
                    [
                        inputs_content
                    ],
                    title='Inputs'
                ),
                pl.SubSection(
                    [
                        bonus_q_str
                    ],
                    title='Bonus Question'
                ),
            ],
            title='Overview'
        ),
        pl.Section(
            [
                pl.SubSection(
                    [
                        submission_str
                    ],
                    title='Submission'
                ),
                pl.SubSection(
                    [
                        solutions_str,
                        pl.Center(
                            pl.Graphic(images_path('project-2-solutions.png'), width=0.5),
                        ),
                        case_solutions_str,
                        pl.UnorderedList(case_solutions_list),
                    ],
                    title='Selected Solutions'
                ),
                pl.SubSection(
                    [
                        pl.Center(
                            lt.Tabular(
                                [

                                    lt.MultiColumnLabel('Grading Breakdown', span=2),
                                    lt.TopRule(),
                                    lt.ValuesTable.from_list_of_lists(
                                        [
                                            ['Category', 'Percentage']
                                        ]
                                    ),
                                    lt.TableLineSegment(0, 1),
                                    lt.ValuesTable.from_list_of_lists(
                                        [
                                            ['Model Accuracy', '60%'],
                                            ['Model Readability', '20%'],
                                            ['Model Formatting', '10%'],
                                            ['Following the Template', '10%'],
                                            ['Bonus', '5%']
                                        ]
                                    ),
                                    lt.MidRule(),
                                    lt.ValuesTable.from_list_of_lists(
                                        [
                                            ['Total Possible', '105%']
                                        ]
                                    ),
                                    lt.BottomRule()

                                ],
                                align=align
                            )
                        )
                    ],
                    title='Grading'
                ),
            ],
            title='Submission & Grading'
        )

    ]

DOCUMENT_CLASS_KWARGS = dict(
    remove_section_numbering=True,
)
OUTPUT_NAME = TITLE
