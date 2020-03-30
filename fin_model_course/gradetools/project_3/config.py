import os

ANSWERS_MODEL_FOLDER = os.path.sep.join(['Projects', 'Project 3'])
ANSWERS_OUTPUT_PATH = os.path.sep.join(['gradetools', 'project_3', 'answers.json'])

NUM_ITERATIONS = 10000

TOLERANCES = dict(
    mv_debt=500000000,
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


# TODO: set locations of excel inputs and outputs
EXCEL_INPUT_LOCATIONS = {
    'price_machine': 'B2',
    'default_decay': 'B5',
    'final_default': 'B6',
    'recovery_rate': 'B7',
}

EXCEL_OUTPUT_LOCATIONS = {
    'coe': 'C5',
    'mv_equity': 'C6',
    'mc_table': 'C7',
}
