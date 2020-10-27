from lectures.model import LectureNotes, Lecture, LectureResource
from resources.models import RESOURCES


def get_intro_combining_excel_python_lecture() -> Lecture:
    title = 'Introduction to Combining Excel and Python'
    youtube_id = 'HbIVMdbZuzQ'
    week_covered = 9
    notes = LectureNotes([
        'At this point in the course, you should feel comfortable using both Python and Excel to '
        'create models to solve problems',
        'Now it is time to learn how to combine the two tools for the maximum flexibility, power, and convenience',
        'We will cover two approaches to integrating the two: using Pandas and using xlwings',
        'We are also about to learn Monte Carlo simulation, which can be done easily in Python but would require '
        'using VBA or an extension in Excel. Using this combination we can have the model in Excel and run Monte Carlo '
        'simulations on it in Python',
        'The Pandas approach is simpler but is much more limited, basically you can read in Excel workbooks and you '
        'can output an entire workbook or sheet',
        'The xlwings approach gets a bit more complicated but allows to have a connection between Excel and Python '
        'and transfer individual values or entire tables back and forth with an existing workbook'
    ], title=title)
    resources = []
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_pandas_combining_excel_python_lecture() -> Lecture:
    title = 'Combining Excel and Python using Pandas'
    youtube_id = 'GrzJSNrP6ns'
    week_covered = 9
    notes = LectureNotes([
        'If you have a Python model and you just want to load some data in from Excel, Pandas is probably your best '
        'choice',
        'If you have an Excel model and you collect the data using Python, this is also a good choice',
        'If you want to have some parts of your model in Excel and some parts in Python, you should probably look to '
        'xlwings',
        'BE CAREFUL WHEN WRITING TO WORKBOOKS as it will replace what is there. It could overwrite your Excel model. '
        'THERE IS NO UNDO (back up your work)',
    ], title=title)
    resources = [
        RESOURCES.examples.connecting_python_excel.pandas.read_write_excel_pandas,
        RESOURCES.labs.connecting_python_excel.pandas.msft_financials,
    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_xlwings_combining_excel_python_lecture() -> Lecture:
    title = 'Combining Excel and Python using xlwings'
    youtube_id = 'LYzVXHCJs40'
    week_covered = 9
    notes = LectureNotes([
        'xlwings is a package that makes it quite easy to combine Excel and Python in ways that should work for '
        'nearly every use case',
        'This can be done without xlwings using the Microsoft COM API in Python, but xlwings is far more convenient',
        'We are focusing here on only manipulating Excel from Python, but I encourage you to explore running Python '
        'from Excel on your own time',
        'Now with xlwings, anything that you can do in Excel, you can make it happen from Python',
        'It is easy to transfer individual values, ranges, and tables back and forth between Excel and Python',
        'For those who have a lot of difficulty with Python and feel comfortable in Excel, xlwings allows building out '
        'the core model in Excel and adding extensions such as Monte Carlo simulation, sensitivity analysis, and '
        'scenario analysis in Python',
    ], title=title)
    resources = [
        RESOURCES.examples.connecting_python_excel.xlwings.example_notebook,
        RESOURCES.examples.connecting_python_excel.xlwings.example_workbook,
        RESOURCES.labs.connecting_python_excel.xlwings.lab_xlsx,
    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)
