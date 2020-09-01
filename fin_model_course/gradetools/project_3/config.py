import os

ANSWERS_MODEL_FOLDER = os.path.sep.join(['Projects', 'Project 3'])
ANSWERS_OUTPUT_PATH = os.path.sep.join(['gradetools', 'project_3', 'answers.json'])

NUM_ITERATIONS = 10000

TOLERANCES = dict(
    mv_debt=800000000,
    mv_equity=1,
    wacc_mean=0.005,
    wacc_std=0.002,
    other=0.00001
)

DATA_DIR = os.path.sep.join(['Projects', 'Project 3'])
DATA_FILE_NAMES = [
    'SP500 Prices.xlsx',
    'WMT Balance Sheet.xlsx',
    'WMT Debt Details.xls',
    'WMT Income Statement.xlsx',
    'WMT Prices.xlsx'
]
DATA_FILES = [os.path.join(DATA_DIR, file) for file in DATA_FILE_NAMES]

INPUT_DICTS = [
    dict(
        model=dict(
            bond_years=15,
            bond_coupon=0.0525,
            bond_price=130.58,
            bond_par=100,
            risk_free=0.005,
            price=119.51,
            shares_outstanding=2850000000,
            libor_rate=0.0196,
        ),
        sim=dict(
            beta_std=0.2,
            mkt_ret_std=0.03,
            bond_price_std=30,
            tax_rate_std=0.05,
        )
    ),
    dict(
        model=dict(
            bond_years=10,
            bond_coupon=0.0325,
            bond_price=120.58,
            bond_par=150,
            risk_free=0.01,
            price=87.51,
            shares_outstanding=1250000000,
            libor_rate=0.025,
        ),
        sim=dict(
            beta_std=0.1,
            mkt_ret_std=0.02,
            bond_price_std=20,
            tax_rate_std=0.025,
        )
    ),
]
for inp_dict in INPUT_DICTS:
    inp_dict['sim']['num_iter'] = NUM_ITERATIONS


# TODO [#6]: set locations of excel inputs and outputs
EXCEL_INPUT_LOCATIONS = dict(
    bond_years='B3',
    bond_coupon='B4',
    bond_price='B5',
    bond_par='B6',
    risk_free='B7',
    price='B8',
    shares_outstanding='B9',
    libor_rate='B10',
    num_iter='B13',
    beta_std='B15',
    mkt_ret_std='B16',
    bond_price_std='B17',
    tax_rate_std='B18',
)

EXCEL_OUTPUT_LOCATIONS = {
    'wacc': 'B24',
    'coe': 'B27',
    'mv_equity': 'B28',
    'pretax_cost_of_debt': 'B29',
    'mv_debt': 'B31',
    'aftertax_cost_of_debt': 'B30',
    'mc_table': 'E26',
}
