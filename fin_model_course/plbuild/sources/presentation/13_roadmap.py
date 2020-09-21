import pyexlatex as pl
import pyexlatex.table as lt
import pyexlatex.presentation as lp
import pyexlatex.graphics as lg
import pyexlatex.layouts as ll

import plbuild
from lectures.advanced.main import get_advanced_modeling_lecture
from plbuild.paths import images_path
from pltemplates.frames.model_flowchart import (
    ModelFlowchartFrame,
    real_world_style,
    model_style,
    in_out_style
)
from pltemplates.blocks import LabBlock, InClassExampleBlock
from pltemplates.eq_with_variable_defs import EquationWithVariableDefinitions
from pltemplates.hyperlink import Hyperlink
from schedule.main import LECTURE_13_NAME

AUTHORS = ['Nick DeRobertis']
SHORT_TITLE = 'Modeling Road-map'
SUBTITLE = 'A Road-map to Learning Advanced Financial Modeling Topics'

SHORT_AUTHOR = 'DeRobertis'
INSTITUTIONS = [
    ['University of Florida', 'Department of Finance, Insurance, and Real Estate'],
]
SHORT_INSTITUTION = 'UF'

DOCUMENT_CLASS = lp.Presentation
OUTPUT_LOCATION = plbuild.paths.SLIDES_BUILD_PATH
HANDOUTS_OUTPUT_LOCATION = plbuild.paths.HANDOUTS_BUILD_PATH
TITLE = LECTURE_13_NAME
ORDER = 'S13'


def get_content():
    lecture = get_advanced_modeling_lecture()

    pd_mono = pl.Monospace('pandas')
    selenium_mono = pl.Monospace('selenium')
    requests_mono = pl.Monospace('requests')
    matplotlib_mono = pl.Monospace('matplotlib')
    holoviews_mono = pl.Monospace('holoviews')
    open_mono = pl.Monospace('open')
    os_mono = pl.Monospace('os')
    shutil_mono = pl.Monospace('shutil')
    pathlib_mono = pl.Monospace('pathlib')
    git_mono = pl.Monospace('git')
    fin_model_types = {
        'Portfolio valuation and optimization': 'Find the returns, value, and risk of a portfolio and select the best '
                                                'asset allocation for the portfolio',
        'Additional Funds Needed (AFN)': 'Budgeting model which uses forecasted financial statements to determine '
                                         'how much capital should be raised',
        'Lease or Own': 'Guides the decision of whether to rent or buy an asset',
        'Event Studies': 'Tries to determine the impact of an event',
        'Merger and Aquisition (M&A)': 'A DCF valuation of a target company with operations being combined '
                                       'with the parent at a merger date. Detetermines M&A price.',
        'Leveraged Buyout (LBO)': 'A specialized M&A model used for when large amounts of debt are being used '
                                  'to purchase the target firm.',
        'Derivatives Valuation': 'Value options, swaps, forwards, etc.',
        'Debt models': 'Immunization models are about having the right amount of cash in the future, term structure '
                       'models estimate the rates for different maturity bonds, and default-adjusted return models '
                       'factor in default in determining debt returns',
        'Value at Risk (VaR)': 'Determine how much an investment might lose with a certain probability in a certain '
                               'time span',
    }
    fin_model_items = [f'{pl.Underline(key)}: {value}' for key, value in fin_model_types.items()]

    return [
        pl.Section(
            [
                lp.DimRevealListFrame(
                    [
                        'Throughout this course, we have covered Python and Excel basics',
                        'We have also covered financial modeling specifics, such as how to structure a '
                        'financial model in both Python and Excel, cash flow and probability modeling, '
                        'sensitivity analysis, scenario analysis, and Monte Carlo simulations',
                        'As far as types of financial models, we covered a retirement model, a '
                        'capital budgeting model, a lender profitiability model, and the discounted '
                        'cash flow (DCF) valuation of a stock',
                        "This could have been a two-semester course. There is a lot I didn't cover. Let's "
                        "do a quick overview of it today."
                    ],
                    title='What we Covered and What is Left'
                )
            ],
            title='Introduction'
        ),
        pl.Section(
            [
                lp.DimRevealListFrame(
                    fin_model_items[:5],
                    title='Financial Models 1'
                ),
                lp.DimRevealListFrame(
                    fin_model_items[5:9],
                    title='Financial Models 2'
                ),
                lp.DimRevealListFrame(
                    [
                        'Here are some links with free resources to learn more about types of models',
                        'The following examples will be using Excel only',
                        Hyperlink('http://macabacus.com/learn', 'Macabacus'),
                        Hyperlink(
                            'https://corporatefinanceinstitute.com/resources/knowledge/modeling/',
                            'Corporate Finance Institute'
                        ),
                        Hyperlink('https://fminstitute.com/learning/', 'Financial Modeling Institute'),
                        'And I found a couple Python resources, though the coding standards are not great:',
                        Hyperlink('http://www.financeandpython.com/Finance.html', 'Finance and Python'),
                        Hyperlink(
                            'https://www.datacamp.com/community/tutorials/finance-python-trading',
                            'Build a Trading Algorithm in Python',
                        )
                    ],
                    title='Financial Model Resources'
                )
            ],
            title='Types of Financial Models'
        ),
        pl.Section(
            [
                lp.TwoColumnGraphicDimRevealFrame(
                    [
                        'Data pipelines are about getting the input data into your model in a '
                        'standardized way',
                        'Within data pipelines, there are two main steps: data collection and '
                        'data cleaning.',
                        'Either step can be automated, ideally both would be, but it always comes down '
                        'to a tradeoff with modeler time'
                    ],
                    graphics=[
                        images_path('data-pipeline.png')
                    ]
                ),
                lp.DimRevealListFrame(
                    [
                        'Data can come from many sources, but most typically it originates from the Internet',
                        'If you can manually download the data, you can automate it via web scraping',
                        'You can also extract different types of data with web scraping, even if it is not structured '
                        'as a dataset',
                        'Some data comes from an API, where you need to send requests to download the data',
                        [selenium_mono, 'uses Python code to drive a browser such as Chrome while', requests_mono,
                         'is a more lightweight, text based way to make web requests (good for APIs).']

                    ],
                    title='Data Collection'
                ),
                lp.DimRevealListFrame(
                    [
                        ['We have already covered the best general-purpose tool for cleaning data:', pd_mono],
                        'We did not cover it in enough detail to cover all data cleaning cases',
                        'The main material left is selecting, merging, grouping, and reshaping',
                        'Regular expressions are a way of matching any possible string and extracting parts of '
                        'it, which useful for messy data'
                    ],
                    title='Data Cleaning'
                ),
                lp.DimRevealListFrame(
                    [
                        Hyperlink(
                            'https://stackabuse.com/getting-started-with-selenium-and-python/',
                            'Get Started Browser-Based Web Scraping with Selenium'
                        ),
                        Hyperlink(
                            'https://realpython.com/python-requests/',
                            'Get Started Text-Based Web Scraping with Requests'
                        ),
                        Hyperlink(
                            'https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html',
                            'Pandas Intro, Covers Basics of Needed Topics'
                        ),
                        Hyperlink(
                            'https://pandas.pydata.org/pandas-docs/stable/user_guide/cookbook.html#cookbook',
                            'Advanced Pandas'
                        ),
                        Hyperlink(
                            'https://scotch.io/tutorials/an-introduction-to-regex-in-python',
                            'Intro to Regular Expressions'
                        ),
                        Hyperlink(
                            'https://docs.python.org/3/library/re.html',
                            'Regular Expression Reference'
                        )
                    ],
                    title='Data Pipelines Resources',

                )
            ],
            title='Data Pipelines'
        ),
        pl.Section(
            [
                lp.TwoColumnGraphicDimRevealFrame(
                    [
                        'We covered basic mathematical tools including basic probability theory, '
                        'algebra, variance/standard deviation, averages, and basic regressions',
                        'Most financial modeling does not take very advanced math, with the exception '
                        'of some derivatives models',
                        "But there are a few more useful tools we didn't have time to cover"
                    ],
                    graphics=[
                        images_path('equations-chalkboard-2.jpg')
                    ],
                    title='What Math we Covered'
                ),
                lp.DimRevealListFrame(
                    [
                        ['Often we want to maximize or minimize something, e.g. maximize returns or NPV, '
                         'minimize risk. We can do this in general with a mathematical technique called',
                         pl.Underline('optimization')],
                        ['If you have a complicated custom model, such that the algebra is getting too difficult '
                        'to do by hand, you can use a', pl.Underline('computer algebra system')],
                        [pl.Underline('Levenshtein (edit) distance'), 'can be used to say how similar two strings are,',
                         'which is useful for data cleaning and more.']
                    ],
                    title='General Math Tools'
                ),
                lp.DimRevealListFrame(
                    [
                        'We covered Ordinary Least Squares (OLS) regressions, which is what anyone means if they '
                        'just say regression',
                        ["There are many more kinds of regressions, we can't even mention them all here. "
                         "But most likely to be useful include", pl.Underline('logistic regression'), 'for when',
                         'probabilities are dependent variables and', pl.Underline('panel regression + fixed effects'),
                         'for when you are dealing',
                         'with multiple instruments over time'],
                        'There are many time-series models to cover, as was mentioned in the forecasting lecture',
                        [pl.Underline('Machine learning/AI'), 'can be used to make classifications or predictions']
                    ],
                    title='Statistics Tools'
                ),
                lp.DimRevealListFrame(
                    [
                        Hyperlink(
                            'https://towardsdatascience.com/optimization-with-scipy-and-application-ideas-to-machine-learning-81d39c7938b8',
                            'Optimization with SciPy'
                        ),
                        Hyperlink(
                            'https://docs.sympy.org/latest/tutorial/preliminaries.html',
                            'Computer Algebra with SymPy'
                        ),
                        Hyperlink(
                            'https://www.geeksforgeeks.org/fuzzywuzzy-python-library/',
                            'Levenshtein Distance using fuzzywuzzy'
                        ),
                        Hyperlink(
                            'https://towardsdatascience.com/logistic-regression-python-7c451928efee',
                            'Intro to Logistic Regression in Python'
                        ),
                        Hyperlink(
                            'https://medium.com/pew-research-center-decoded/using-fixed-and-random-effects-models-for-panel-data-in-python-a795865736ab',
                            'Intro to Panel Regression in Python'
                        ),
                        Hyperlink(
                            'https://www.statsmodels.org/stable/py-modindex.html',
                            'Statistical Models in statsmodels'
                        ),
                        Hyperlink(
                            'https://bashtage.github.io/linearmodels/doc/index.html',
                            'More Statistical Models in linearmodels'
                        ),
                        Hyperlink(
                            'https://docs.scipy.org/doc/scipy/reference/stats.html',
                            'More Statistical Tools in Scipy'
                        ),
                        Hyperlink(
                            'https://machinelearningmastery.com/machine-learning-in-python-step-by-step/',
                            'Getting Started with Machine Learning in Python'
                        ),
                        Hyperlink(
                            'https://machinelearningmastery.com/start-here/',
                            'General Introduction to Machine Learning'
                        ),
                        Hyperlink(
                            'datacamp.com/community/tutorials/deep-learning-python',
                            'Deep Learning (AI) in Python using Keras'
                        ),
                    ],
                    title='Mathematical Tools Resources'
                )
            ],
            title='Mathematical Tools'
        ),
        pl.Section(
            [
                lp.TwoColumnGraphicDimRevealFrame(
                    [
                        "We didn't have very much time to cover presenting the model in Python, other than formatting text",
                        "For Excel, the model is already presented so just structure the workbook well",
                        "A well structured Jupyter notebook or Python script is important for another modeler to "
                        "pick up where you left off. But it still is not an ideal format for non-technical consumers "
                        "of your model"
                    ],
                    graphics=[
                        images_path('example-report.png')
                    ],
                    title='Presenting Model Results'
                ),
                lp.DimRevealListFrame(
                    [
                        "One easy way that doesn't require anything we haven't learned is separating model logic "
                        "and presentation",
                        "Develop as you will while building the model. But when it's time to share the results, "
                        "separate the main model logic (classes and functions) into separate Python file(s)",
                        "Then the Jupyter notebook will just show high-level calls to your model and the results"
                    ],
                    title='Present with Basic Jupyter'
                ),
                lp.DimRevealListFrame(
                    [
                        'Less technical consumers of the model may just want the model conclusions and not '
                        'to actually use the model themselves',
                        'In this case, it is useful to generate reports containing the model results',
                        'There are three major ways to make reports: HTML, LaTeX, and direct PDF solutions',
                        'If all you need is PDF output, a direct solution is fine, but HTML and LaTeX (which '
                        'can be converted to HTML) can both be converted to PDF and have the added advantage of '
                        'being viewable as a web page',
                        'Templating is also easier with HTML and LaTeX'
                    ],
                    title='Create Reports'
                ),
                lp.DimRevealListFrame(
                    [
                        'There is another way for non-technical consumers of your model to interact with it: '
                        'via an app',
                        'It is possible to build apps right in a Jupyter notebook using widgets',
                        'A web app could also be created with a web framework',
                        'With an app, a non-technical consumer of your model can adjust the inputs and see '
                        'the outputs, without having any knowledge of Python or instructions'
                    ],
                    title='Publish Reports and Models'
                ),
                lp.DimRevealListFrame(
                    [
                        ['We covered very basic plots using', pd_mono],
                        [matplotlib_mono, 'provides all the plotting functionality to', pd_mono, 'and any', pd_mono,
                         'plots can be adjusted using', matplotlib_mono, 'options'],
                        'Several libraries exist for interactive plots, which allow for dropdowns, sliders, '
                        'selecting points, zooming, tooltips, and more',
                        ['Other plotting styles are becoming more popular, such as', holoviews_mono + ',', 'in which',
                         'you just describe the data and it can generate interactive plots for you']
                    ],
                    title='Advanced Plotting'
                ),
                lp.DimRevealListFrame(
                    [
                        pl.TextSize(-1),
                        Hyperlink(
                            'https://dev.to/goyder/automatic-reporting-in-python---part-1-from-planning-to-hello-world-32n1',
                            'Intro to Creating HTML Reports in Python',
                        ),
                        Hyperlink(
                            'https://towardsdatascience.com/creating-pdf-reports-with-python-pdfkit-and-jinja2-templates-64a89158fa2d',
                            'Create HTML Reports and Output to PDF',
                        ),
                        Hyperlink(
                            'https://realpython.com/primer-on-jinja-templating/',
                            'Templating HTML and LaTeX Using Jinja'
                        ),
                        Hyperlink(
                            'https://www.reportlab.com/docs/reportlab-userguide.pdf',
                            'Direct PDF Output with Reportlab',
                        ),
                        Hyperlink(
                            'https://nickderobertis.github.io/py-ex-latex/',
                            'Direct to LaTeX Using pyexlatex'
                        ),
                        Hyperlink(
                            'https://www.datacamp.com/community/tutorials/matplotlib-tutorial-python',
                            'Matplotlib Plotting Tutorial'
                        ),
                        Hyperlink(
                            'https://holoviews.org/getting_started/index.html',
                            'Get started with Holoviews'
                        ),
                        Hyperlink(
                            'https://towardsdatascience.com/bring-your-jupyter-notebook-to-life-with-interactive-widgets-bc12e03f0916',
                            'Use ipywidgets to Build an App in Jupyter'
                        ),
                        Hyperlink(
                            'https://voila.readthedocs.io/en/stable/',
                            'Convert a Jupyter Notebook to a Web App using Viola'
                        ),
                        Hyperlink(
                            'https://voila-gallery.org/services/gallery/',
                            'Examples of Viola Web Apps'
                        ),
                        Hyperlink(
                            'https://scotch.io/tutorials/getting-started-with-flask-a-python-microframework',
                            'Get Started Building Web Apps with Flask'
                        ),
                        Hyperlink(
                            'https://anvil.works/learn/tutorials/jupyter-notebook-to-web-app',
                            'Convert a Jupyter Notebook to a Web App using Anvil'
                        ),
                        Hyperlink(
                            'https://www.fullstackpython.com/',
                            'Full Tutorials for Python Web Development'
                        ),
                    ],
                    title='Presentation Resources'
                )
            ],
            title='Present Results'
        ),
        pl.Section(
            [
                lp.TwoColumnGraphicDimRevealFrame(
                    [
                        'We were only able to cover basic Python, and certainly not a lot of practices that would '
                        'typically be used in programming',
                        'Python is very flexible in that you can be productive in it with very little understanding '
                        'or mastery of it',
                        'But if you do gain a greater knowledge of it, it can unlock new potential.',
                        'Further, there is more we can learn from the software engineering world in how to improve '
                        'our programming'
                    ],
                    graphics=[
                        images_path('python-code-blur.jpeg')
                    ],
                    title='Your Programming Future'
                ),
                lp.DimRevealListFrame(
                    [
                        pl.TextSize(-1),
                        'We can learn a few things from the software engineers that are programming all day every day',
                        [pl.Underline('Version control'), 'or', pl.Underline('source control'), 'is a way of tracking',
                         'changes to code over time. You can get the full history of the project, and multiple',
                         'people can work on the same project at the same time and later merge the changes together.',
                         git_mono, 'is the gold standard for this.'],
                        ['Share', git_mono, 'repositories with the world via Github (or others), allowing anyone to '
                         'use and improve your project'],
                        "Automated testing of your code allows you to make changes ensuring it won't break anything",
                        "Input validation is useful for when others interact with your model directly",
                        'Use an integrated development environment (IDE) such as PyCharm or VS Code for better code '
                        'completion and linking',
                        'Automatically run tests, style your code, deploy Python packages or web apps, and more with '
                        'continuous integration/continuous deployment (CI/CD)'
                    ],
                    title='General Programming'
                ),
                lp.DimRevealListFrame(
                    [
                        ['Python can work with the files on your computer through the', open_mono, 'command and the',
                         os_mono, pathlib_mono,
                         'and', shutil_mono, 'modules'],
                        'Get unique items, unions, intersections using sets',
                        'Override how objects work by overriding double-underscore (dunder) class methods',
                        'Modify existing functions using decorators',
                        'Store Python objects by picking them',
                        'Check yourself and make your code easier to understand using type annotations',
                        'Structure projects using packages and modules',
                        'Isolate project requirements using virtual environments',
                    ],
                    title='Python Programming'
                ),
                lp.DimRevealListFrame(
                    [
                        pl.TextSize(-1),
                        Hyperlink(
                            'https://product.hubspot.com/blog/git-and-github-tutorial-for-beginners',
                            'Get Started with Git and Github'
                        ),
                        Hyperlink(
                            'https://desktop.github.com/',
                            'Github Desktop is an App that Makes Git Easy'
                        ),
                        Hyperlink(
                            'https://realpython.com/python-testing/',
                            'Get Started with Automated Testing in Python'
                        ),
                        Hyperlink(
                            'https://www.youtube.com/watch?v=IL3eZYiV70g',
                            'Intro to Input Validation in Python'
                        ),
                        Hyperlink(
                            'https://www.jetbrains.com/pycharm/',
                            'PyCharm IDE'
                        ),
                        Hyperlink(
                            'https://code.visualstudio.com/',
                            'Visual Studio Code (VS Code) IDE'
                        ),
                        Hyperlink(
                            'https://semaphoreci.com/blog/cicd-pipeline',
                            'Intro to CI/CD'
                        ),
                        Hyperlink(
                            'https://github.com/features/actions',
                            'CI/CD Using Github Actions'
                        ),
                        Hyperlink(
                            'https://www.pythonforbeginners.com/files/reading-and-writing-files-in-python',
                            'Intro to Reading and Writing Files with Python'
                        ),
                        Hyperlink(
                            'https://realpython.com/python-pathlib/',
                            'Beyond the Basics of Working with Files in Python'
                        ),
                    ],
                    title='Programming Resources 1'
                ),
                lp.DimRevealListFrame(
                    [
                        pl.TextSize(-1),
                        Hyperlink(
                            'https://realpython.com/python-sets/',
                            'Work with Sets in Python'
                        ),
                        Hyperlink(
                            'https://dbader.org/blog/python-dunder-methods',
                            'Get Started with Dunder Methods in Python'
                        ),
                        Hyperlink(
                            'https://realpython.com/python-data-classes/',
                            'Advanced Dataclasses'
                        ),
                        Hyperlink(
                            'https://ipython.readthedocs.io/en/stable/config/integrating.html',
                            'Rich Object Display in Jupyter'
                        ),
                        Hyperlink(
                            'https://realpython.com/primer-on-python-decorators/',
                            'Get Started with Python Decorators'
                        ),
                        Hyperlink(
                            'https://www.datacamp.com/community/tutorials/pickle-python-tutorial',
                            'Store Python Objects with pickle and dill'
                        ),
                        Hyperlink(
                            'https://dev.to/dstarner/using-pythons-type-annotations-4cfe',
                            'Intro to Type Annotations in Python'
                        ),
                        Hyperlink(
                            'https://docs.python-guide.org/writing/structure/',
                            'Intro to Project Structure in Python'
                        ),
                        Hyperlink(
                            'https://www.dabapps.com/blog/introduction-to-pip-and-virtualenv-python/',
                            'Introduction to Virtual Environments in Python'
                        ),
                        Hyperlink(
                            'https://realpython.com/pipenv-guide/',
                            'Virtual Environments Made Easy with pipenv'
                        )
                    ],
                    title='Programming Resources 2'
                )

            ],
            title='Programming'
        ),
        pl.Section(
            [
                lp.DimRevealListFrame(
                    [
                        Hyperlink(
                            'https://docs.python-guide.org/',
                            "The Hickhiker's Guide to Python"
                        ),
                        Hyperlink(
                            'https://realpython.com/',
                            'Real Python'
                        ),
                        Hyperlink(
                            'https://automatetheboringstuff.com/',
                            'Automate the Boring Stuff with Python'
                        ),
                        Hyperlink(
                            'https://pbpython.com/',
                            'Practical Business Python'
                        )

                    ],
                    title='General Resources'
                )
            ],
            title='Extras'
        ),
        pl.PresentationAppendix([lecture.pyexlatex_resources_frame]),
    ]

DOCUMENT_CLASS_KWARGS = dict(
    nav_header=True,
    toc_sections=True
)
OUTPUT_NAME = TITLE

