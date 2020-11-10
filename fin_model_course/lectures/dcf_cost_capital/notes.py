from lectures.model import LectureNotes, Lecture, LectureResource
from resources.models import RESOURCES


def get_intro_dcf_lecture() -> Lecture:
    title = 'Introduction to Discounted Cash Flow (DCF) Valuation'
    youtube_id = '9wRZmIbnEmw'
    week_covered = 11
    notes = LectureNotes([
        'The Discounted Cash Flow (DCF) valuation of a stock is often considered a capstone finance '
        'model as incorporates many different concepts and also the technical skills to implement them',
        'I have often heard of job applicants being asked to prepare a DCF model to prove their skills and knowledge',
        'It is also generally considered the valuation approach which can be the most accurate, though there are '
        'a lot of assumptions which must be made which could influence the results',
        'There are two main portions of the DCF model: coming up with the weighted average cost of capital (WACC) '
        'and estimating future free cash flows. Each of these portions have smaller tasks involved',
        'At the end of the day, the concept of the model is extremely simple: take the present value of future '
        'cash flows to determine the value of the company. The difficult part is figuring out those cash flows '
        'and the discount rate',
        'In this segment we will be focusing on the cost of capital estimation, and we will come back in the next '
        'segment to cover FCF estimation',
        'We will focus on using the Capital Asset Pricing Model (CAPM) to estimate the cost of equity and we will '
        'discuss several approaches for estimating the cost and market value of debt depending on the availability '
        'of data and amount of time that can be invested into building the model'
    ], title=title)
    resources = []
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_ev_lecture() -> Lecture:
    title = 'Enterprise Value and Equity Value'
    youtube_id = 'hhmWGkoJmCU'
    week_covered = 11
    notes = LectureNotes([
        'When we take the present value of future cash flows, we will get the enterprise value which is '
        'a combination of the value from different sources of capital',
        'Ultimately we are interested in determining the value of the stock which represents only equity value, '
        'and so we need to extract the equity value from the enterprise value by removing the other components',
        'Many struggle with the concept that additional cash reduces enterprise value. I think it is useful to '
        'think through scenarios with the two interpretations of enterprise value: asset value or cost to acquire '
        'the company. In the context of cost to acquire, if an acquirer buys the business, they immediately own that '
        'cash on hand, so really the cash on hand offsets the purchase price. In the context of asset value, imagine '
        'two companies with identical operations. One decides to issue an additional \$10M of stock just to put cash '
        'on the balance sheet. Now they have \$10M of additional equity value, and if cash also added to enterprise value '
        'then all of a sudden they would be worth \$20M more than the other company despite the same operations. If the '
        'cash comes in the equation negatively, then there is no change in value for the stock issuance, which makes '
        'sense as the two companies still have the same operations'
    ], title=title)
    resources = []
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_intro_cost_of_equity_lecture() -> Lecture:
    title = 'Introduction to Cost of Equity'
    youtube_id = 'UaRJcnj48Z8'
    week_covered = 11
    notes = LectureNotes([
        'We are using the Capital Asset Pricing Model (CAPM) to estimate the cost of equity for the company',
        'There are many other possible models which could be used such as one of the many factor '
        'models including Fama-French factors, but CAPM is the most basic and once you '
        'understand the approach it is not difficult to switch for a more complex model',
        'In the general approach, we estimate the model on historical data and assume that the resulting estimated '
        'parameters will hold in the future to predict the future cost of capital'
    ], title=title)
    resources = []
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_python_cost_of_equity_lecture() -> Lecture:
    title = 'Cost of Equity in Python'
    youtube_id = 'xs9otS3z_Qo'
    week_covered = 11
    notes = LectureNotes([
        'The process to estimating cost of capital using prior stock prices is straightforward: calculate returns, '
        'run the CAPM regression, then take the coefficient on the market risk premium (MRP) as the Beta, then '
        'plug the beta in the CAPM to estimate the future cost of equity based on an expected market return and '
        'risk free rate',
        'Once you calculate returns, the first row will have missing data as there is no prior price. '
        'Statsmodels cannot handle missing data, so we will need to add a Pandas command to remove those rows',
    ], title=title)
    resources = [
        RESOURCES.examples.dcf.cost_of_equity.python_coe,
        RESOURCES.examples.dcf.cost_of_equity.price_data,
    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_excel_cost_of_equity_lecture() -> Lecture:
    title = 'Cost of Equity in Excel'
    youtube_id = 'PmMN6i46ssY'
    week_covered = 11
    notes = LectureNotes([
        'The process to estimating cost of capital using historical prices in Excel is similar to doing it in Python',
        'The main difference is just how we run the regression with the Data Analysis Tookpack GUI rather than through '
        'statsmodels',
        'A disappointing aspect of doing this in Excel is it cannot automatically update if you add new data'
    ], title=title)
    resources = [
        RESOURCES.examples.dcf.cost_of_equity.excel_coe,
    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_mv_equity_lecture() -> Lecture:
    title = 'Market Value of Equity'
    youtube_id = '_Tt42ybud_4'
    week_covered = 11
    notes = LectureNotes([
        'If you are dealing with a publicly traded company, the calculation of market value of equity is '
        'simply number of shares multiplied price per share',
        'With a private company, this is much more difficult. You can look at public comparables to help with this. If '
        'a public competitor has a \$10B valuation, and this company has 10% of its market share and similar profit '
        'margins, a \$1B valuation might be a reasonable estimate',
        'With early stage companies, you might not even have financials or a reasonable public comparable. But often '
        'these companies do not have debt and so it is not necessary to estimate the market value as you know it '
        'will be 100% of the capitalization',
    ], title=title)
    resources = [
    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_intro_cost_of_debt_lecture() -> Lecture:
    title = 'Cost of Debt'
    youtube_id = 'd8vbTRBEntA'
    week_covered = 11
    notes = LectureNotes([
        'If your company is very mature and stable, the financial statements approach to cost of debt may '
        'be a reasonable approach',
        'If your company does not have market bonds outstanding or you do not have access to data on these bonds, '
        'you are stuck with the financial statement approach regardless',
        'If you can find information on even one market bond, it may be better to use the market rate of bonds approach, '
        'though this approach is even better when you can take a weighted average of multiple bonds',
        'The handling of taxes is crucial in dealing with the cost of debt considering that debt is tax-advantaged '
        'in the US and many countries',
        'The tax rate can be estimated from historical financial statements',
    ], title=title)
    resources = []
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_intro_mv_debt_lecture() -> Lecture:
    title = 'Introduction to Market Value of Debt'
    youtube_id = 'QOuyNfFTtfA'
    week_covered = 11
    notes = LectureNotes([
        'Simple models often just assume the market value of debt is equal to the book value of debt. While this '
        'makes the calculation simple and is sometimes all you can do due to data availability, this can be quite '
        'inaccurate for most companies',
        'The market value of individual instruments approach can be the most accurate but requires the most data '
        'and takes more effort to implement',
        'We are still keeping things a bit simple for both MV and cost of debt. In a more detailed model you would '
        'also consider seniority of the debt when doing these calculations'
    ], title=title)
    resources = []
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_mv_debt_python_lecture() -> Lecture:
    title = 'Calculating the Market Value of Debt in Python'
    youtube_id = 'x2jhJdV7Dh4'
    week_covered = 11
    notes = LectureNotes([
        'The value of a hypothetical bond approach just uses traditional bond valuation techniques',
        'For the market value of individual bonds approach, again we are just applying traditional '
        'bond valuation, but we can use Pandas to apply the single calculation across all the bonds '
        'at once',
        'We are also covering some material here on working with dates as you will usually have a maturity '
        'date to work with and need to convert it into a number of years',

    ], title=title)
    resources = [
        *RESOURCES.examples.dcf.cost_of_debt.resources(),
    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_wacc_lecture() -> Lecture:
    title = 'Calculating the Weighted Average Cost of Capital (WACC)'
    youtube_id = 'Vb07rhwC6io'
    week_covered = 11
    notes = LectureNotes([
        'The WACC is simply the weighted average of the costs of each source of capital',
        'The weights are the percentage of the capital structure which is allocated to the type of asset, i.e. '
        'the market value of the source of capital divided by the total market value of the company',
        'Be sure to use the after-tax cost of debt in the calculation',
        'Companies with the same costs of capital can have very different WACCs due to a different percentage '
        'of debt and equity in the capital structure',
    ], title=title)
    resources = [

    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)