import pyexlatex as pl
import pyexlatex.table as lt
import pyexlatex.presentation as lp
import pyexlatex.graphics as lg
import pyexlatex.layouts as ll

import plbuild
from plbuild.paths import images_path


AUTHORS = ['Nick DeRobertis']

DOCUMENT_CLASS = pl.Document
OUTPUT_LOCATION = plbuild.paths.DOCUMENTS_BUILD_PATH
HANDOUTS_OUTPUT_LOCATION = None

TITLE = 'Probabilistic Loan Pricing'
ORDER = 2


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

    initial_default_prob_cases = [0.3]
    initial_default_prob_cases_str = ', '.join([str(case) for case in initial_default_prob_cases])
    bonus_initial_default_prob_mean = inputs['initial_default_prob'][1]
    bonus_initial_default_prob_std = 0.05

    # TODO: update output values
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
    officer would like you to evaluate rates in 2% increments from 20% to 40%.
    
    The lending officer is also worried that she may have estimated {inputs["initial_default_prob"][0]} incorrectly. 
    She is hoping for the answers to the above questions considering that {inputs["initial_default_prob"][0]} may vary.
    Evaluate the above questions for {pl.Equation(str_eq=default_prob_cases_eq_str)} in addition to the base case 
    of {inputs["initial_default_prob"][1]}.
    """

    notes = [
    f"""
    Unlike the prior project, you cannot assume some maximum number of years. Your model should accept any possible
    positive loan life.
    """,
    "Probably the easiest approach to building this model will use internal randomness. I have set up the project "
    "template so to help you out with this. There is a button that will run your model repeatedly and collect the "
    "outputs into a separate tab. Make sure you set Number of iterations to at least 100 to get a good estimate. "
    "While you are testing things out, set it lower to have it run quicker.",
    'Your "IRR (this run)" should change when the inputs change. You do not need to have your final answers changing '
    'when the model changes, as you will have to use the button to get the output. So you can use the button to get '
    'the result with the appropriate inputs, then hardcode that result into the output table.',
    'Your answers may differ slightly from those in the Selected Solutions section. This is the nature of a random model. They '
    'should not be far off, though.',
    "Save often. Use Dropbox or save separate files as versions of your model as you go through. Occasionally there "
    "can be some bugs which make your UDFs disappear. UDFs can also disable undo functionality at times.",
    'Do not move any of the input or output cells. It will break the model.',
    'There is some weird issue where cell formatting is not working correctly in the template. I will be looking into this, '
    'but for the purposes of this assignment I will not be grading formatting.'
    ]

    bonus_q_str = f"""
    Produce the same outputs as the main problem, but instead of evaluating 
    {pl.Equation(str_eq=default_prob_cases_eq_str)}, consider {inputs["initial_default_prob"][0]} as being normally
    distributed with mean {bonus_initial_default_prob_mean} and standard deviation {bonus_initial_default_prob_std}.
    """

    submission_str = f"""
    Work off of the "project2.xlsm" and "project2.py" files on Canvas. This is an
    xlwings project with some setup for you already. 

    Your submission should contain both the macro-enabled XLSM workbook and the .py Python file.
    """

    solutions_str = """
    The below solutions are with the base case inputs provided. Your model will also need to be able to adjust for
    different inputs. Try changing the inputs and verify that the model changes in the way it should respond. Do 
    this for all the inputs.
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
                        pl.UnorderedList(solutions_list),
                    ],
                    title='Selected Solutions'
                ),
                pl.SubSection(
                    [
                        pl.Center(
                            lt.Tabular(
                                [

                                    lt.MultiColumn('Grading Breakdown', span=2),
                                    lt.TopRule(),
                                    lt.ValuesTable.from_list_of_lists(
                                        [
                                            ['Category', 'Percentage']
                                        ]
                                    ),
                                    lt.TableLineSegment(0, 1),
                                    lt.ValuesTable.from_list_of_lists(
                                        [
                                            ['Model Accuracy', '80%'],
                                            ['Model Readability', '20%'],
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

