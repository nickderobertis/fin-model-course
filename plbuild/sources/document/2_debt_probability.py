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

    initial_default_prob_cases = [0.1, 0.3, 0.4]
    initial_default_prob_cases_str = ', '.join([str(case) for case in initial_default_prob_cases])
    bonus_initial_default_prob_mean = inputs['initial_default_prob'][1]
    bonus_initial_default_prob_std = 0.05

    # TODO: update output values
    outputs = dict(
        interest_rate=('$r_{interest}$', 0.1),
        default_prob_t=('$p_t^{default}$', 0),
        default_prob_t_minus_1=('$p_{t-1}^{default}$', 0),
    )

    default_prob_eq_str = f'{outputs["default_prob_t"][0].strip("$")} = {outputs["default_prob_t_minus_1"][0].strip("$")} ' \
                          f'{inputs["default_prob_decay"][0].strip("$")}'

    recovery_eq_str = f'{inputs["recovery_rate"][0].strip("$")}{inputs["price_machine"][0].strip("$")}'

    default_prob_cases_eq_str = f'{inputs["initial_default_prob"][0].strip("$")} = {initial_default_prob_cases_str}'

    problem_definition_pre_prob = f"""
    You work for a bank who is considering loaning funds to a small manufacturing business. The business needs 
    {inputs["price_machine"][0]} to buy machinery. The business would like to borrow the funds for 
    {inputs["loan_life"][0]}, and at that time it will repay {inputs["price_machine"][0]} in full. Interest is 
    paid annually at a rate of {outputs["interest_rate"][0]} (in the final period, both 
    {inputs["price_machine"][0]} and interest of {outputs["interest_rate"][0]} will be paid). As this is a small 
    business, there is significant default risk, but that default risk decreases over time as the business 
    matures. The probability of default in the first year is {inputs["initial_default_prob"][0]}, and then each 
    year thereafter it is:
    """

    problem_definition_post_prob = f"""
    Finally, the default probability is different in the final year, as it is the repayment year. The business has to
    pay a lot more in this period so there is a greater likelihood it can't come up with the funds. In the final year,
    (at year {inputs["loan_life"][0]}), the default probability is {inputs["final_default_prob"][0]}. 
    
    When the business defaults during the life of the loan, before year {inputs["loan_life"][0]}, then the default
    covenants of the loan trigger bankruptcy for the borrower, and the borrower must pay as much as it can on the loan 
    in the bankruptcy process. The bankruptcy process takes 2 years, and then once it is resolved, the lender will 
    collect {inputs["recovery_rate"][0]}% of {inputs["price_machine"][0]}. For the year of default and the year after,
    the lender will not collect any cash flows, and then 2 years after default, the lender will collect 
    {pl.Equation(str_eq=recovery_eq_str)}. 
    
    When the business defaults at the end of the loan, the loan will be renegotiated. It will be extended by two years.
    This means that in the original final year of the loan, and the year after, the business will pay the regular 
    interest amount. Two years after the original repayment date, the business will be required to pay the original 
    final payment of both {inputs["price_machine"][0]} and interest of {outputs["interest_rate"][0]}. At this time,
    the business could default again, and the cycle would repeat (and this can keep going).
    """

    main_q_str = f"""
    You are the commercial loan analyst trying to decide if this loan makes sense for the bank. You want to give the
    lending officer all the information she would need to negotiate a rate for this loan.
    
    Given the inputs, what
    is the minimum interest rate the bank would be willing to offer on the loan? This would be the interest rate which
    makes the NPV of the loan equal to 0, i.e. the IRR of the loan.
    
    Further, the lending officer needs some more information than just the minimum the bank is willing to accept.
    She is hoping for a table of probabilities, and the rate the bank would have to set to have that probability of
    making money, going from 10% to 90% in 10% increments. E.g. what rate does the bank have to set to have a 70% chance
    of having a positive NPV?
    
    The lending officer is also worried that she may have estimated {inputs["initial_default_prob"][0]} incorrectly. 
    She is hoping for the answers to the above questions considering that {inputs["initial_default_prob"][0]} may vary.
    Evaluate the above questions for {pl.Equation(str_eq=default_prob_cases_eq_str)}.
    """

    bonus_q_str = f"""
    Produce the same outputs as the main problem, but instead of evaluating 
    {pl.Equation(str_eq=default_prob_cases_eq_str)}, consider {inputs["initial_default_prob"][0]} as being normally
    distributed with mean {bonus_initial_default_prob_mean} and standard deviation {bonus_initial_default_prob_std}.
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

    ]

DOCUMENT_CLASS_KWARGS = {}
OUTPUT_NAME = TITLE

