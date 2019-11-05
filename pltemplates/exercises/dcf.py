import pyexlatex as pl
import pyexlatex.table as lt
import pyexlatex.presentation as lp
import pyexlatex.graphics as lg
import pyexlatex.layouts as ll

from pltemplates.blocks import LabBlock
from pltemplates.exercises.lab_exercise import LabExercise


def get_dcf_enterprise_equity_value_exercise() -> LabExercise:

    bullet_contents = [
        [
            pl.TextSize(-1),
            'You are the CFO for a startup developing artificial intelligence technologies. There will be an '
            'initial research phase before making any money. Google is watching your development and will purchase '
            'the company after it is profitable.',
            r'For the first two years, the company loses \$20 million. Then there is one breakeven year, after which '
            r'the profit is \$10 million for year 4. Finally in year 5, Google purchases the company for \$70 million.',
            'The WACC for the company is 15% and it has 1 million shares outstanding. The company has \$5 million '
            'in debt and \$1 million in cash.',
            'What is the enterprise value of the stock at year 5? What about the enterprise value today? '
            'What is the price of the stock today?'
        ],
        [
            pl.TextSize(-1),
            'A pharmaceutical company developed a new drug and has 5 years to sell it before the patent expires. '
            'It forms a new company to manufacture and sell the drug. After 5 years, the company will be sold to '
            'someone that wants to continue manufacturing at the lower price.',
            r'The new company pays a dividend of \$1 per share each year, before selling it for \$30 million in '
            r'year 5.',
            r'There are 10 million shares outstanding, \$10 million of debt and \$1 million of cash throughout the '
            r'life of the company. The WACC is 10% today.',
            'What is the enterprise value at year 5 and today? What is the price of the stock today?'
        ]
    ]

    answer_contents = [
        [
            r'The enterprise value at year 5 is \$70 million',
            r'The enterprise value at year 0 is \$9.2 million',
            r'The equity value at year 0 is \$5.21 million so the share price is \$5.21'
        ],
        [
            r'The enterprise value at year 5 is \$30 million',
            r'The equity value at year 0 is \$49.2 million so the share price is \$4.92',
            r'The enterprise value at year 0 is \$58.2 million',
        ]
    ]

    return LabExercise(
        bullet_contents,
        'DCF Value of a Firm',
        f"Finding Enterprise and Equity Value Given FCF and WACC",
        label='lab:dcf-enterprise-equity',
        answers_content=answer_contents
    )


