from lectures.model import LectureNotes, Lecture, LectureResource
from resources.models import RESOURCES


def get_intro_fcf_lecture() -> Lecture:
    title = 'Introduction to Free Cash Flows'
    youtube_id = 'br-5IQjIm6w'
    week_covered = 12
    notes = LectureNotes([
        'As a recap, we are focusing on FCF calculation so that we can do the discounted cash flow (DCF) '
        'valuation of a stock',
        'We need to calculate historical FCFs and also forecast future FCFs',
        'Historical FCFs are a mechanical exercise that anyone could do, but forecasting is as much an '
        'art as it is a science',
        'FCFs accrue to all investors, debt and equity, and so they can be used to determine the value of the firm',
        'Net income is a measure which accountants have devised to smooth out the cash flows of the company, '
        'representing one time outlays which are used in multiple periods by splitting the cost across those periods',
        'As far as valuation is concerned, net income does not matter. FCFs are what matters as they are what is '
        'actually happening with the operations in that time period',
        'Unless the historical FCFs are very stable, you should almost always be forecasting the financial '
        'statements and calculating the future FCFs rather than forecasting them directly',
        'There is a lot of flexibility in forecasting as you can use dozens of different possible models, and three '
        'common forecast targets (levels, growth, percentage of another item)'
    ], title=title)
    resources = []
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_historical_fcf_lecture() -> Lecture:
    title = 'Introduction to Calculating Historical Free Cash Flows'
    youtube_id = 'kghacp72D3M'
    week_covered = 12
    notes = LectureNotes([
        'There are multiple sets of equations that can be used to calculate free cash flows',
        'Here we will focus on a set of equations that does not require the statement of cash flows, '
        'only the income statement and the balance sheet',
        'I usually recommend this approach because then only the income statement and balance sheet '
        'need to be forecasted rather than all three financial statements',
        'The philosophy of this approach is that we are starting with net income, undoing the adjustments '
        'which have accountants have done, and adding our own adjustments for cash items which are '
        'not included in net income to get back to FCFs',
        'Net working capital is not counted in net income, but can be a source or use of cash so it should be '
        'included',
        'Capital expenditures are usually spread across the usage of the asset in net income, but here we are '
        'adjusting it so the cost is realized in the period of the purchase',
    ], title=title)
    resources = [
        RESOURCES.labs.dcf.fcf.wmt_income_statement,
        RESOURCES.labs.dcf.fcf.wmt_balance_sheet,
    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_historical_fcf_python_lecture() -> Lecture:
    title = 'Historical Free Cash Flows in Python Using Pandas and finstmt'
    youtube_id = 'lLFaAQH7Jos'
    week_covered = 12
    notes = LectureNotes([
        'Most of the work in calculating historical free cash flows with Pandas is just getting '
        'the data loaded, cleaned up, and in the right structure',
        'We use .loc in Pandas to look up a statement item when it is in the index and the columns '
        'are the dates',
        'Be careful about the names of columns, they may have gotten loaded in with extra spaces or otherwise '
        'not exactly as you expected',
        'Be sure to think about the sign on your item. Are costs represented as positive or negative in the statement?',
        'I created the finstmt package to make all of these operations more convenient and '
        'repeatable, with the goal being that '
        'you should be able to quickly work with financial statements without all the cleanup operations, '
        'and you should be able to provide different statements and have the code work the same',
        'I have continued to add useful features to finstmt such as calculating free cash flows and forecasting',
        'It is easy to do lags and changes in the calculations with finstmt',
    ], title=title)
    resources = [
        *RESOURCES.examples.dcf.historical_fcf.resources(),
        RESOURCES.external.python.finstmt_documentation,
    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_historical_fcf_lab_overview_lecture() -> Lecture:
    title = 'Historical Free Cash Flows Lab Exercise Overview'
    youtube_id = 'XHGvOA5sYnY'
    week_covered = 12
    notes = LectureNotes([
        'The first exercise is just about going through the math of the FCF calculation',
        'The second exercise requires you to work with actual financial statements to '
        'do the calculations, similar to the example',
    ], title=title)
    resources = [
        RESOURCES.labs.dcf.fcf.wmt_balance_sheet,
        RESOURCES.labs.dcf.fcf.wmt_income_statement,
        RESOURCES.external.python.finstmt_documentation,
    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_intro_forecasting_lecture() -> Lecture:
    title = 'Introduction to Forecasting'
    youtube_id = 'CKacJsM5ZGE'
    week_covered = 12
    notes = LectureNotes([
        'I could teach an entire course on forecasting. There is far too much material to cover in the time allowed',
        'There is so much complexity as there are multiple options on two dimensions: what to forecast and which '
        'model to use',
        'We will focus on only a few possible models in this course to keep things simple',
        'It is up to the modeler which models to use and what to forecast. It should generally be guided by knowledge '
        'of the company as well as understanding of the structure of financial statements',
        'The simple time-series models are easy to understand, but the advanced models quickly get into a confusing '
        'alphabet soup and are outside the scope of this course',
        'You could also use machine learning models for forecasting',
        'Regardless of the chosen model, the steps to forecasting are the same. So once you learn the steps in '
        'this course, you will be able to learn the more advanced models on your own and apply them in the same '
        'framework',
    ], title=title)
    resources = [
    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_simple_forecasting_lecture() -> Lecture:
    title = 'Simple Time-Series Forecasting Models'
    youtube_id = '-qtB0NcXKmY'
    week_covered = 12
    notes = LectureNotes([
        'Use the historical average approach when there is not a defined trend or growth in the historical data '
        'and when you think that the average will be more relevant than just looking at the most recent value',
        'Use the recent value approach in the same situation, but instead you think that the most recent data '
        'is more relevant than an average',
        'If the data are going up or down over time, as long as there is not a repeating pattern within that, '
        'use the trend or growth model. Use the trend model when the change seems linear/constant, and the '
        'growth model when the change seems exponential/changing over time. If there are repeating patterns within the '
        'data, a more complex model will be required'
    ], title=title)
    resources = [
    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_simple_forecasting_excel_lecture() -> Lecture:
    title = 'Simple Time-Series Forecasting in Excel'
    youtube_id = '1kYbZ98_JgM'
    week_covered = 12
    notes = LectureNotes([
        'Most of the calculations are straightforward in Excel',
        'We can use the SLOPE and INTERCEPT functions to fit the trend model without using the '
        'Data Analysis Toolpak regression',
    ], title=title)
    resources = [
        RESOURCES.examples.dcf.forecasting.simple.sales_cogs_xlsx,
        RESOURCES.examples.dcf.forecasting.simple.sales_cogs_forecasted_xlsx,
    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_simple_forecasting_python_lecture() -> Lecture:
    title = 'Simple Time-Series Forecasting in Python'
    youtube_id = '8jgvoT50NuM'
    week_covered = 12
    notes = LectureNotes([
        'The calculations themselves are straightforward in Python, though we see a couple new tricks such '
        'as transposing a DataFrame and working with the DataFrame index',
        'This example also builds up some functions which could be taken and used in a project',
    ], title=title)
    resources = [
        RESOURCES.examples.dcf.forecasting.simple.forecast_simple_notebook,
        RESOURCES.examples.dcf.forecasting.simple.sales_cogs_xlsx,
    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_simple_forecasting_lab_overview_lecture() -> Lecture:
    title = 'Simple Time-Series Forecasting Lab Overview'
    youtube_id = 'xa_Gd46zizE'
    week_covered = 12
    notes = LectureNotes([
        'This lab exercise follows closely the structure of the previous example',
        'Through this you should understand the different simple methods'
    ], title=title)
    resources = [
        RESOURCES.labs.dcf.forecasting.simple.debt_interest
    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_simple_forecasting_finstmt_python_lecture() -> Lecture:
    title = 'Forecasting Simple Financial Statements in Python with finstmt'
    youtube_id = 'OWDulQWYscU'
    week_covered = 12
    notes = LectureNotes([
        'Forecasting financial statements can be overwhelming because there are so many '
        'different line items to think through',
        'finstmt allows you to forecast them all at once, conveniently, and with reasonable '
        'baseline assumptions. You can modify the forecast method or target (level, growth, % of other item) '
        'for any item as desired by adjusting the configuration',
        'finstmt also automatically generates plots with confidence intervals for all the line items',
        'finstmt also allows you to make manual adjustments to an existing forecast, either by adjusting '
        'the existing forecasted values or by replacing them',
    ], title=title)
    resources = [
        RESOURCES.examples.dcf.forecasting.simple.forecast_finstmt_notebook,
        RESOURCES.examples.dcf.forecasting.simple.cat_bs,
        RESOURCES.examples.dcf.forecasting.simple.cat_inc,
        RESOURCES.external.python.finstmt_documentation,
    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_complex_forecasting_lecture() -> Lecture:
    title = 'Complex Time-Series Forecasting'
    youtube_id = ''
    week_covered = 13
    notes = LectureNotes([

    ], title=title)
    resources = [

    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_complex_forecasting_python_manual_lecture() -> Lecture:
    title = 'Complex Time-Series Forecasting in Python - Manual Method'
    youtube_id = ''
    week_covered = 13
    notes = LectureNotes([

    ], title=title)
    resources = [
        *RESOURCES.examples.dcf.forecasting.complex.resources(),
    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_complex_forecasting_python_finstmt_lecture() -> Lecture:
    title = 'Complex Time-Series Forecasting in Python - finstmt Method'
    youtube_id = ''
    week_covered = 13
    notes = LectureNotes([

    ], title=title)
    resources = [
        *RESOURCES.examples.dcf.forecasting.complex.resources(),
        RESOURCES.external.python.finstmt_documentation,
    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_complex_forecasting_lab_overview_lecture() -> Lecture:
    title = 'Complex Time-Series Forecasting Lab Overview'
    youtube_id = ''
    week_covered = 13
    notes = LectureNotes([

    ], title=title)
    resources = [
        *RESOURCES.labs.dcf.forecasting.complex.resources(),
    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_fcf_forecasting_lecture() -> Lecture:
    title = 'Applying Forecasting to Free Cash Flows'
    youtube_id = ''
    week_covered = 13
    notes = LectureNotes([

    ], title=title)
    resources = [

    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_tv_lecture() -> Lecture:
    title = 'Calculating a Terminal Value'
    youtube_id = ''
    week_covered = 13
    notes = LectureNotes([

    ], title=title)
    resources = [

    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)