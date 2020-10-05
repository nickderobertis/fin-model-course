import pathlib
import warnings
from typing import Sequence, Union, List, Dict, Optional

from pydantic import BaseModel

from build_tools.config import (
    LAB_FOLDER_NAME,
    METADATA_PATHS,
    GENERATED_CONTENT_METADATA_PATH,
    STATIC_CONTENT_METADATA_PATH,
)
from lectures.model import LectureResource
from models.content import GeneratedCollectionMetadata, StaticCollectionMetadata
from schedule.main import (
    PROJECT_1_NAME,
    PROJECT_2_NAME,
    PROJECT_3_NAME,
    PROJECT_4_NAME,
    LECTURE_1_NAME,
    LECTURE_2_NAME,
    LECTURE_3_NAME,
    LECTURE_4_NAME,
    LECTURE_5_NAME,
    LECTURE_6_NAME,
    LECTURE_7_NAME,
    LECTURE_8_NAME,
    LECTURE_9_NAME,
    LECTURE_10_NAME,
    LECTURE_11_NAME,
    LECTURE_12_NAME,
    LECTURE_13_NAME,
)


class MissingResourceException(ValueError):
    pass


class ResourceCollection(BaseModel):
    title: str

    def resources(self, nested: bool = True) -> List[LectureResource]:
        resources: List[LectureResource] = []
        for field_name, field in self.__fields__.items():
            if issubclass(field.type_, LectureResource):
                value: LectureResource = getattr(self, field_name)
                resources.append(value)
            if nested and issubclass(field.type_, ResourceCollection):
                value: ResourceCollection = getattr(self, field_name)
                resources.extend(value.resources(nested=True))
        return resources

    def validate_locations(
        self,
        generated_metadata_path: pathlib.Path = GENERATED_CONTENT_METADATA_PATH,
        static_metadata_path: pathlib.Path = STATIC_CONTENT_METADATA_PATH,
        convert_extensions: Optional[Dict[str, str]] = None,
    ):
        if convert_extensions is None:
            convert_extensions = {'.tex': '.pdf'}

        generated = GeneratedCollectionMetadata.parse_raw(
            generated_metadata_path.read_text()
        )
        static = StaticCollectionMetadata.parse_raw(static_metadata_path.read_text())
        all = StaticCollectionMetadata(items={**generated.items, **static.items})
        file_paths = set()
        for fp in all.items.keys():
            path = pathlib.Path(fp)
            if path.suffix.casefold() in convert_extensions:
                path = path.with_suffix(convert_extensions[path.suffix.casefold()])
            file_paths.add(str(path))

        seen_file_paths = set()
        for resource in self.resources():
            if resource.static_url and resource.static_url not in file_paths:
                raise MissingResourceException(
                    f"could not find filepath {resource.static_url} "
                    f"for resource {resource.name}"
                )
            seen_file_paths.add(resource.static_url)
        unseen_file_paths = file_paths.difference(seen_file_paths)
        warnings.warn(
            f"Do not have resource objects for the following file paths: {unseen_file_paths}"
        )


class PythonBasicsLabResources(ResourceCollection):
    title: str = "Python Basics"
    dicts_lists_comprehensions_notebook: LectureResource = LectureResource(
        f"Dictionaries, List Comprehensions, and Imports Labs",
        static_url=f"{LAB_FOLDER_NAME}/Python Basics/Dicts and List Comprehensions Lab.ipynb",
    )
    python_basics_notebook: LectureResource = LectureResource(
        "Python Basics Lab Exercises",
        static_url=f"{LAB_FOLDER_NAME}/Python Basics/Python Basics Lab.ipynb",
    )


class VisualizationLabResources(ResourceCollection):
    title: str = "Visualization"
    pandas_visualization_notebook: LectureResource = LectureResource(
        f"Pandas and Visualization Labs",
        static_url=f"{LAB_FOLDER_NAME}/Visualization/Pandas and Visualization Labs.ipynb",
    )


class ConnectingPythonExcelPandasLabResources(ResourceCollection):
    title: str = "pandas"
    msft_financials: LectureResource = LectureResource(
        f"MSFT Financials",
        static_url=f"{LAB_FOLDER_NAME}/Connecting Python and Excel/pandas/MSFT Financials.xls",
    )
    financial_data: LectureResource = LectureResource(
        f"Financial Data",
        static_url=f"{LAB_FOLDER_NAME}/Connecting Python and Excel/pandas/Financial Data.xlsx",
    )


class ConnectingPythonExcelXlwingsLabResources(ResourceCollection):
    title: str = "xlwings"
    lab_xlsx: LectureResource = LectureResource(
        f"xlwings Lab",
        static_url=f"{LAB_FOLDER_NAME}/Connecting Python and Excel/xlwings/xlwings Lab.xlsx",
    )


class ConnectingPythonExcelLabResources(ResourceCollection):
    title: str = "Connecting Python and Excel"
    pandas: ConnectingPythonExcelPandasLabResources = ConnectingPythonExcelPandasLabResources()
    xlwings: ConnectingPythonExcelXlwingsLabResources = ConnectingPythonExcelXlwingsLabResources()


class DCFCostOfEquityLabResources(ResourceCollection):
    title: str = "Cost of Equity"
    prices_xlsx: LectureResource = LectureResource(
        f"Prices", static_url=f"{LAB_FOLDER_NAME}/DCF/Cost of Equity/prices.xlsx"
    )


class DCFFCFLabResources(ResourceCollection):
    title: str = "FCF"
    wmt_balance_sheet: LectureResource = LectureResource(
        f"WMT Balance Sheet",
        static_url=f"{LAB_FOLDER_NAME}/DCF/FCF/WMT Balance Sheet.xlsx",
    )
    wmt_income_statement: LectureResource = LectureResource(
        f"WMT Income Statement",
        static_url=f"{LAB_FOLDER_NAME}/DCF/FCF/WMT Income Statement.xlsx",
    )


class ForecastingSimpleLabResources(ResourceCollection):
    title: str = "Simple"
    debt_interest: str = LectureResource(
        f"Debt Interest",
        static_url=f"{LAB_FOLDER_NAME}/DCF/Forecasting/Simple/Debt Interest.xlsx",
    )


class ForecastingComplexLabResources(ResourceCollection):
    title: str = "Complex"
    cat_balance_sheet: LectureResource = LectureResource(
        f"CAT Balance Sheet",
        static_url=f"{LAB_FOLDER_NAME}/DCF/Forecasting/Complex/CAT Balance Sheet.xlsx",
    )
    cat_income_statement: LectureResource = LectureResource(
        f"CAT Income Statement",
        static_url=f"{LAB_FOLDER_NAME}/DCF/Forecasting/Complex/CAT Income Statement.xlsx",
    )


class ForecastingLabResources(ResourceCollection):
    title: str = "Forecasting"
    simple: ForecastingSimpleLabResources = ForecastingSimpleLabResources()
    complex: ForecastingComplexLabResources = ForecastingComplexLabResources()


class DCFLabResources(ResourceCollection):
    title: str = "DCF"
    cost_of_equity: DCFCostOfEquityLabResources = DCFCostOfEquityLabResources()
    fcf: DCFFCFLabResources = DCFFCFLabResources()
    forecasting: ForecastingLabResources = ForecastingLabResources()


class LabResources(ResourceCollection):
    title: str = LAB_FOLDER_NAME
    python_basics: PythonBasicsLabResources = PythonBasicsLabResources()
    visualization: VisualizationLabResources = VisualizationLabResources()
    connecting_python_excel: ConnectingPythonExcelLabResources = ConnectingPythonExcelLabResources()
    dcf: DCFLabResources = DCFLabResources()


class IntroExcelExampleResources(ResourceCollection):
    title: str = "Excel"
    dynamic_salary_retirement_model: LectureResource = LectureResource(
        "Dynamic Salary Retirement Model - Excel",
        static_url="Examples/Introduction/Excel/Dynamic Salary Retirement Model.xlsx",
    )
    simple_retirement_model: LectureResource = LectureResource(
        "Simple Retirement Model - Excel",
        static_url="Examples/Introduction/Excel/Simple Retirement Model.xlsx",
    )


class IntroPythonExampleResources(ResourceCollection):
    title: str = "Python"
    dynamic_salary_retirement_model: LectureResource = LectureResource(
        "Dynamic Salary Retirement Model - Python",
        static_url="Examples/Introduction/Python/Dynamic Salary Retirement Model.ipynb",
    )
    simple_retirement_model: LectureResource = LectureResource(
        "Simple Retirement Model - Python",
        static_url="Examples/Introduction/Python/Simple Retirement Model.ipynb",
    )
    basics_notebook: LectureResource = LectureResource(
        "Python Basics", static_url="Examples/Introduction/Python/Python Basics.ipynb"
    )
    dicts_list_comp_imports_notebook: LectureResource = LectureResource(
        "Python Dicts, List Comprehensions, and Imports",
        static_url="Examples/Introduction/Python/Python Dicts, List comprehensions, and Imports.ipynb",
    )
    car_example: LectureResource = LectureResource(
        "Car Class Example", static_url="Examples/Introduction/Python/car_example.py"
    )


class IntroductionExampleResources(ResourceCollection):
    title: str = "Introduction"
    excel: IntroExcelExampleResources = IntroExcelExampleResources()
    python: IntroPythonExampleResources = IntroPythonExampleResources()


class VisualizationExcelExampleResources(ResourceCollection):
    title: str = "Excel"
    dynamic_salary_model_visualized: LectureResource = LectureResource(
        "Dynamic Salary Retirement Model Visualized",
        static_url="Examples/Visualization/Excel/Dynamic Salary Retirement Model Visualized.xlsx",
    )


class VisualizationPythonExampleResources(ResourceCollection):
    title: str = "Python"
    dynamic_salary_model_visualized: LectureResource = LectureResource(
        "Dynamic Salary Retirement Model Visualized",
        static_url="Examples/Visualization/Python/Dynamic Salary Retirement Model Visualized.ipynb",
    )
    intro_pandas_notebook: LectureResource = LectureResource(
        "Intro to Pandas and Table Visualization",
        static_url="Examples/Visualization/Python/Intro to Pandas and Table Visualization.ipynb",
    )
    intro_graphics_notebook: LectureResource = LectureResource(
        "Intro to Graphics",
        static_url="Examples/Visualization/Python/Intro to Graphics.ipynb",
    )


class VisualizationExampleResources(ResourceCollection):
    title: str = "Visualization"
    excel: VisualizationExcelExampleResources = VisualizationExcelExampleResources()
    python: VisualizationPythonExampleResources = VisualizationPythonExampleResources()


class SensitivityAnalysisExcelExampleResources(ResourceCollection):
    title: str = "Excel"
    dynamic_salary_model_sensitivity: LectureResource = LectureResource(
        "Dynamic Salary Retirement Model Sensitivity",
        static_url="Examples/Sensitivity Analysis/Excel/Dynamic Salary Retirement Model Sensitivity.xlsx",
    )


class SensitivityAnalysisPythonExampleResources(ResourceCollection):
    title: str = "Python"
    dynamic_salary_model_sensitivity: LectureResource = LectureResource(
        "Dynamic Salary Retirement Model Sensitivity",
        static_url="Examples/Sensitivity Analysis/Python/Dynamic Salary Retirement Model Sensitivity.ipynb",
    )
    sensitivity_notebook: LectureResource = LectureResource(
        "Sensitivity Analysis",
        static_url="Examples/Sensitivity Analysis/Python/Sensitivity Analysis.ipynb",
    )


class SensitivityAnalysisExampleResources(ResourceCollection):
    title: str = "Sensitivity Analysis"
    excel: SensitivityAnalysisExcelExampleResources = SensitivityAnalysisExcelExampleResources()
    python: SensitivityAnalysisPythonExampleResources = SensitivityAnalysisPythonExampleResources()


class ScenarioAnalysisExcelExampleResources(ResourceCollection):
    title: str = "Excel"
    dynamic_salary_model_scenario: LectureResource = LectureResource(
        "Dynamic Salary Retirement Model External Scenarios",
        static_url="Examples/Scenario Analysis/Excel/Dynamic Salary Retirement Model External Scenarios.xlsx",
    )


class ScenarioAnalysisPythonExampleResources(ResourceCollection):
    title: str = "Python"
    dynamic_salary_model_scenario: LectureResource = LectureResource(
        "Dynamic Salary Retirement Model Scenario Analysis",
        static_url="Examples/Scenario Analysis/Python/Dynamic Salary Retirement Model Scenario Analysis.ipynb",
    )


class ScenarioAnalysisExampleResources(ResourceCollection):
    title: str = "Scenario Analysis"
    excel: ScenarioAnalysisExcelExampleResources = ScenarioAnalysisExcelExampleResources()
    python: ScenarioAnalysisPythonExampleResources = ScenarioAnalysisPythonExampleResources()


class InternalRandomnessExcelExampleResources(ResourceCollection):
    title: str = "Excel"
    dynamic_salary_model_random: LectureResource = LectureResource(
        "Dynamic Salary Retirement Model Internal Randomness - Excel",
        static_url="Examples/Internal Randomness/Excel/Dynamic Salary Retirement Model Internal Randomness.xlsx",
    )
    generate_numbers: LectureResource = LectureResource(
        "Generating Random Numbers - Excel",
        static_url="Examples/Internal Randomness/Excel/Generating Random Numbers.xlsx",
    )


class InternalRandomnessPythonExampleResources(ResourceCollection):
    title: str = "Python"
    dynamic_salary_model_random: LectureResource = LectureResource(
        "Dynamic Salary Retirement Model Internal Randomness - Python",
        static_url="Examples/Internal Randomness/Python/Dynamic Salary Retirement Model Internal Randomness.ipynb",
    )
    generate_numbers: LectureResource = LectureResource(
        "Generating Random Numbers - Python",
        static_url="Examples/Internal Randomness/Python/Generating Random Numbers.ipynb",
    )


class InternalRandomnessExampleResources(ResourceCollection):
    title: str = "Internal Randomness"
    excel: InternalRandomnessExcelExampleResources = InternalRandomnessExcelExampleResources()
    python: InternalRandomnessPythonExampleResources = InternalRandomnessPythonExampleResources()


class ConnectingPythonExcelPandasExampleResources(ResourceCollection):
    title: str = "pandas"
    read_write_excel_pandas: LectureResource = LectureResource(
        "Read Write Excel Pandas",
        static_url="Examples/Connecting Python and Excel/pandas/Read Write Excel Pandas.ipynb",
    )
    stock_data: LectureResource = LectureResource(
        "Stock Data",
        static_url="Examples/Connecting Python and Excel/pandas/Stock Data.xlsx",
    )


class ConnectingPythonExcelXlwingsExampleResources(ResourceCollection):
    title: str = "xlwings"
    example_notebook: LectureResource = LectureResource(
        "Combining Excel and Python",
        static_url="Examples/Connecting Python and Excel/xlwings/Combining Excel and Python.ipynb",
    )
    example_workbook: LectureResource = LectureResource(
        "Example Workbook",
        static_url="Examples/Connecting Python and Excel/xlwings/Example Workbook.xlsx",
    )


class ConnectingPythonExcelExampleResources(ResourceCollection):
    title: str = "Connecting Python and Excel"
    pandas: ConnectingPythonExcelPandasExampleResources = ConnectingPythonExcelPandasExampleResources()
    xlwings: ConnectingPythonExcelXlwingsExampleResources = ConnectingPythonExcelXlwingsExampleResources()


class MonteCarloExcelExampleResources(ResourceCollection):
    title: str = "Excel"
    dynamic_salary_model_mc: LectureResource = LectureResource(
        "Dynamic Salary Retirement Model with Monte Carlo",
        static_url="Examples/Monte Carlo/Excel/Dynamic Salary Retirement Model with Monte Carlo.xlsx",
    )
    excel_monte_carlo_notebook: LectureResource = LectureResource(
        "Excel Monte Carlo",
        static_url="Examples/Monte Carlo/Excel/Excel Monte Carlo.ipynb",
    )


class MonteCarloPythonExampleResources(ResourceCollection):
    title: str = "Python"
    dynamic_salary_model_mc: LectureResource = LectureResource(
        "Dynamic Salary Retirement Model with Monte Carlo",
        static_url="Examples/Monte Carlo/Python/Dynamic Salary Retirement Model Monte Carlo.ipynb",
    )
    investment_returns: LectureResource = LectureResource(
        "Monte Carlo Investment Returns",
        static_url="Examples/Monte Carlo/Python/MC Investment Returns.ipynb",
    )


class MonteCarloExampleResources(ResourceCollection):
    title: str = "Monte Carlo"
    excel: MonteCarloExcelExampleResources = MonteCarloExcelExampleResources()
    python: MonteCarloPythonExampleResources = MonteCarloPythonExampleResources()


class DCFCostOfDebtExampleResources(ResourceCollection):
    title: str = "Cost of Debt"
    debt_data: LectureResource = LectureResource(
        "Debt Data", static_url="Examples/DCF/Cost of Debt/debt data.xlsx"
    )
    mv_debt_notebook: LectureResource = LectureResource(
        "Market Value of Debt",
        static_url="Examples/DCF/Cost of Debt/Market Value of Debt.ipynb",
    )


class DCFCostOfEquityExampleResources(ResourceCollection):
    title: str = "Cost of Equity"
    excel_coe: LectureResource = LectureResource(
        "Cost of Equity - Excel",
        static_url="Examples/DCF/Cost of Equity/DCF Cost of Equity.xlsx",
    )
    python_coe: LectureResource = LectureResource(
        "Cost of Equity - Python",
        static_url="Examples/DCF/Cost of Equity/Determining the Cost of Equity.ipynb",
    )
    price_data: LectureResource = LectureResource(
        "Price Data", static_url="Examples/DCF/Cost of Equity/price data.xlsx"
    )


class ForecastingSimpleExampleResources(ResourceCollection):
    title: str = "Simple"
    cat_bs: LectureResource = LectureResource(
        "CAT Balance Sheet",
        static_url="Examples/DCF/Forecasting/Simple/cat_annual_bs.csv",
    )
    cat_inc: LectureResource = LectureResource(
        "CAT Income Statement",
        static_url="Examples/DCF/Forecasting/Simple/cat_annual_income.csv",
    )
    forecast_simple_notebook: LectureResource = LectureResource(
        "Forecast Sales COGS Simple",
        static_url="Examples/DCF/Forecasting/Simple/Forecast Sales COGS Simple.ipynb",
    )
    forecast_finstmt_notebook: LectureResource = LectureResource(
        "Forecasting Financial Statements",
        static_url="Examples/DCF/Forecasting/Simple/Forecasting Financial Statements.ipynb",
    )
    sales_cogs_xlsx: LectureResource = LectureResource(
        "Sales COGS", static_url="Examples/DCF/Forecasting/Simple/Sales COGS.xlsx"
    )
    sales_cogs_forecasted_xlsx: LectureResource = LectureResource(
        "Sales COGS Forecasted",
        static_url="Examples/DCF/Forecasting/Simple/Sales COGS Forecasted.xlsx",
    )


class ForecastingComplexExampleResources(ResourceCollection):
    title: str = "Complex"
    wmt_bs: LectureResource = LectureResource(
        "WMT Balance Sheet",
        static_url="Examples/DCF/Forecasting/Complex/WMT Balance Sheet.xlsx",
    )
    wmt_inc: LectureResource = LectureResource(
        "WMT Income Statement",
        static_url="Examples/DCF/Forecasting/Complex/WMT Balance Sheet.xlsx",
    )
    forecast_notebook: LectureResource = LectureResource(
        "Forecasting Quarterly Financial Statements",
        static_url="Examples/DCF/Forecasting/Complex/Forecasting Quarterly Financial Statements.ipynb",
    )


class ForecastingExampleResources(ResourceCollection):
    title: str = "Forecasting"
    simple: ForecastingSimpleExampleResources = ForecastingSimpleExampleResources()
    complex: ForecastingComplexExampleResources = ForecastingComplexExampleResources()


class DCFFullDCFExampleResources(ResourceCollection):
    title: str = "Full DCF"
    brinks_model: LectureResource = LectureResource(
        "Brinks DCF Model",
        static_url="Examples/DCF/Full DCF/Brinks Operating Model V 2.0.xlsx",
    )
    brinks_paper: LectureResource = LectureResource(
        "Brinks DCF Write-up", static_url="Examples/DCF/Full DCF/Brinks Paper Final.pdf"
    )
    brinks_presentation: LectureResource = LectureResource(
        "Brinks DCF Presentation",
        static_url="Examples/DCF/Full DCF/Presentation_V3.5 regionals.pptx",
    )


class DCFHistoricalFCFExampleResources(ResourceCollection):
    title: str = "Historical FCF"
    calculate_fcf_notebook: LectureResource = LectureResource(
        "Calculating Historical FCF",
        static_url="Examples/DCF/Historical FCF/Calculating Historical FCF.ipynb",
    )
    xom_financials: LectureResource = LectureResource(
        "Exxon-Mobil Financials",
        static_url="Examples/DCF/Historical FCF/Exxon Mobil Corporation NYSE XOM Financials.xls",
    )


class DCFExampleResources(ResourceCollection):
    title: str = "DCF"
    cost_of_debt: DCFCostOfDebtExampleResources = DCFCostOfDebtExampleResources()
    cost_of_equity: DCFCostOfEquityExampleResources = DCFCostOfEquityExampleResources()
    forecasting: ForecastingExampleResources = ForecastingExampleResources()
    full_dcf: DCFFullDCFExampleResources = DCFFullDCFExampleResources()
    historical_fcf: DCFHistoricalFCFExampleResources = DCFHistoricalFCFExampleResources()


class ExampleResources(ResourceCollection):
    title: str = "Examples"
    intro: IntroductionExampleResources = IntroductionExampleResources()
    visualization: VisualizationExampleResources = VisualizationExampleResources()
    sensitivity: SensitivityAnalysisExampleResources = SensitivityAnalysisExampleResources()
    scenario: ScenarioAnalysisExampleResources = ScenarioAnalysisExampleResources()
    internal_randomness: InternalRandomnessExampleResources = InternalRandomnessExampleResources()
    connecting_python_excel: ConnectingPythonExcelExampleResources = ConnectingPythonExcelExampleResources()
    monte_carlo: MonteCarloExampleResources = MonteCarloExampleResources()
    dcf: DCFExampleResources = DCFExampleResources()


class Project1Resources(ResourceCollection):
    title: str = "Project 1"
    description: LectureResource = LectureResource(
        f"Project 1 - {PROJECT_1_NAME}",
        static_url=f"generated/pdfs/PJ1 {PROJECT_1_NAME}.pdf",
    )
    python_template: LectureResource = LectureResource(
        "Project 1 Template - Python",
        static_url="Project Materials/Project 1/Project 1 Template.ipynb",
    )
    excel_template: LectureResource = LectureResource(
        "Project 1 Template - Excel",
        static_url="Project Materials/Project 1/Project 1 Template.xlsx",
    )


class Project2Resources(ResourceCollection):
    title: str = "Project 2"
    description: LectureResource = LectureResource(
        f"Project 2 - {PROJECT_2_NAME}",
        static_url=f"generated/pdfs/PJ2 {PROJECT_2_NAME}.pdf",
    )
    python_template: LectureResource = LectureResource(
        "Project 2 Template - Python",
        static_url="Project Materials/Project 2/Project 2 Template.ipynb",
    )
    excel_template: LectureResource = LectureResource(
        "Project 2 Template - Excel",
        static_url="Project Materials/Project 2/Project 2 Template.xlsx",
    )


class Project3Resources(ResourceCollection):
    title: str = "Project 3"
    description: LectureResource = LectureResource(
        f"Project 3 - {PROJECT_3_NAME}",
        static_url=f"generated/pdfs/PJ3 {PROJECT_3_NAME}.pdf",
    )
    python_template: LectureResource = LectureResource(
        "Project 3 Template - Python",
        static_url="Project Materials/Project 3/Project 3 Template.ipynb",
    )
    excel_template: LectureResource = LectureResource(
        "Project 3 Template - Excel",
        static_url="Project Materials/Project 3/Project 3 Template.xlsx",
    )
    sp500_prices: LectureResource = LectureResource(
        "S&P 500 Prices", static_url="Project Materials/Project 3/SP500 Prices.xlsx"
    )
    wmt_bs: LectureResource = LectureResource(
        "WMT Balance Sheet",
        static_url="Project Materials/Project 3/WMT Balance Sheet.xlsx",
    )
    wmt_inc: LectureResource = LectureResource(
        "WMT Income Statement",
        static_url="Project Materials/Project 3/WMT Income Statement.xlsx",
    )
    wmt_prices: LectureResource = LectureResource(
        "WMT Prices", static_url="Project Materials/Project 3/WMT Prices.xlsx"
    )
    wmt_debt_details: LectureResource = LectureResource(
        "WMT Debt Details",
        static_url="Project Materials/Project 3/WMT Debt Details.xls",
    )


class Project4Resources(ResourceCollection):
    title: str = "Project 4"
    description: LectureResource = LectureResource(
        f"Project 4 - {PROJECT_4_NAME}",
        static_url=f"generated/pdfs/PJ4 {PROJECT_4_NAME}.pdf",
    )


class ProjectResources(ResourceCollection):
    title: str = "Project Materials"
    project_1: Project1Resources = Project1Resources()
    project_2: Project2Resources = Project2Resources()
    project_3: Project3Resources = Project3Resources()
    project_4: Project4Resources = Project4Resources()
    grading_overview: LectureResource = LectureResource(
        f"Project Grading Overview",
        static_url=f"generated/pdfs/PJ0 Project Grading Overview.pdf",
    )


class CourseMaterialsResources(ResourceCollection):
    title: str = "Course Materials"
    syllabus: LectureResource = LectureResource(
        f"Syllabus", static_url=f"generated/pdfs/C1 Financial Modeling Syllabus.pdf",
    )
    course_schedule: LectureResource = LectureResource(
        f"Course Schedule", static_url=f"generated/pdfs/C2 Course Schedule.pdf",
    )


class IntroLectureResources(ResourceCollection):
    title: str = LECTURE_1_NAME
    slides: LectureResource = LectureResource(
        f"Slides - {LECTURE_1_NAME}",
        static_url=f"generated/pdfs/S1 {LECTURE_1_NAME}.pdf",
    )
    notes: LectureResource = LectureResource(
        f"Lecture Notes - {LECTURE_1_NAME}",
        static_url=f"generated/pdfs/LN1 {LECTURE_1_NAME}.pdf",
    )


class GettingStartedLectureResources(ResourceCollection):
    title: str = LECTURE_2_NAME
    slides: LectureResource = LectureResource(
        f"Slides - {LECTURE_2_NAME}",
        static_url=f"generated/pdfs/S2 {LECTURE_2_NAME}.pdf",
    )
    notes: LectureResource = LectureResource(
        f"Lecture Notes - {LECTURE_2_NAME}",
        static_url=f"generated/pdfs/LN2 {LECTURE_2_NAME}.pdf",
    )


class DepthFinancialModelExcelLectureResources(ResourceCollection):
    title: str = LECTURE_3_NAME
    slides: LectureResource = LectureResource(
        f"Slides - {LECTURE_3_NAME}",
        static_url=f"generated/pdfs/S3 {LECTURE_3_NAME}.pdf",
    )
    notes: LectureResource = LectureResource(
        f"Lecture Notes - {LECTURE_3_NAME}",
        static_url=f"generated/pdfs/LN3 {LECTURE_3_NAME}.pdf",
    )


class GoingBeyondInitialPythonLectureResources(ResourceCollection):
    title: str = LECTURE_4_NAME
    slides: LectureResource = LectureResource(
        f"Slides - {LECTURE_4_NAME}",
        static_url=f"generated/pdfs/S4 {LECTURE_4_NAME}.pdf",
    )
    notes: LectureResource = LectureResource(
        f"Lecture Notes - {LECTURE_4_NAME}",
        static_url=f"generated/pdfs/LN4 {LECTURE_4_NAME}.pdf",
    )


class DepthFinancialModelPythonLectureResources(ResourceCollection):
    title: str = LECTURE_5_NAME
    slides: LectureResource = LectureResource(
        f"Slides - {LECTURE_5_NAME}",
        static_url=f"generated/pdfs/S5 {LECTURE_5_NAME}.pdf",
    )
    notes: LectureResource = LectureResource(
        f"Lecture Notes - {LECTURE_5_NAME}",
        static_url=f"generated/pdfs/LN5 {LECTURE_5_NAME}.pdf",
    )


class VisualizationLectureResources(ResourceCollection):
    title: str = LECTURE_6_NAME
    slides: LectureResource = LectureResource(
        f"Slides - {LECTURE_6_NAME}",
        static_url=f"generated/pdfs/S6 {LECTURE_6_NAME}.pdf",
    )
    notes: LectureResource = LectureResource(
        f"Lecture Notes - {LECTURE_6_NAME}",
        static_url=f"generated/pdfs/LN6 {LECTURE_6_NAME}.pdf",
    )


class SensitivityAnalysisLectureResources(ResourceCollection):
    title: str = LECTURE_7_NAME
    slides: LectureResource = LectureResource(
        f"Slides - {LECTURE_7_NAME}",
        static_url=f"generated/pdfs/S7 {LECTURE_7_NAME}.pdf",
    )
    notes: LectureResource = LectureResource(
        f"Lecture Notes - {LECTURE_7_NAME}",
        static_url=f"generated/pdfs/LN7 {LECTURE_7_NAME}.pdf",
    )


class ProbabilityLectureResources(ResourceCollection):
    title: str = LECTURE_8_NAME
    slides: LectureResource = LectureResource(
        f"Slides - {LECTURE_8_NAME}",
        static_url=f"generated/pdfs/S8 {LECTURE_8_NAME}.pdf",
    )
    notes: LectureResource = LectureResource(
        f"Lecture Notes - {LECTURE_8_NAME}",
        static_url=f"generated/pdfs/LN8 {LECTURE_8_NAME}.pdf",
    )


class CombiningExcelPythonLectureResources(ResourceCollection):
    title: str = LECTURE_9_NAME
    slides: LectureResource = LectureResource(
        f"Slides - {LECTURE_9_NAME}",
        static_url=f"generated/pdfs/S9 {LECTURE_9_NAME}.pdf",
    )
    notes: LectureResource = LectureResource(
        f"Lecture Notes - {LECTURE_9_NAME}",
        static_url=f"generated/pdfs/LN9 {LECTURE_9_NAME}.pdf",
    )


class MonteCarloLectureResources(ResourceCollection):
    title: str = LECTURE_10_NAME
    slides: LectureResource = LectureResource(
        f"Slides - {LECTURE_10_NAME}",
        static_url=f"generated/pdfs/S10 {LECTURE_10_NAME}.pdf",
    )
    notes: LectureResource = LectureResource(
        f"Lecture Notes - {LECTURE_10_NAME}",
        static_url=f"generated/pdfs/LN10 {LECTURE_10_NAME}.pdf",
    )


class DCFCostCapitalLectureResources(ResourceCollection):
    title: str = LECTURE_11_NAME
    slides: LectureResource = LectureResource(
        f"Slides - {LECTURE_11_NAME}",
        static_url=f"generated/pdfs/S11 {LECTURE_11_NAME}.pdf",
    )
    notes: LectureResource = LectureResource(
        f"Lecture Notes - {LECTURE_11_NAME}",
        static_url=f"generated/pdfs/LN11 {LECTURE_11_NAME}.pdf",
    )


class DCFFCFLectureResources(ResourceCollection):
    title: str = LECTURE_12_NAME
    slides: LectureResource = LectureResource(
        f"Slides - {LECTURE_12_NAME}",
        static_url=f"generated/pdfs/S12 {LECTURE_12_NAME}.pdf",
    )
    notes: LectureResource = LectureResource(
        f"Lecture Notes - {LECTURE_12_NAME}",
        static_url=f"generated/pdfs/LN12 {LECTURE_12_NAME}.pdf",
    )


class AdvancedLectureResources(ResourceCollection):
    title: str = LECTURE_13_NAME
    slides: LectureResource = LectureResource(
        f"Slides - {LECTURE_13_NAME}",
        static_url=f"generated/pdfs/S13 {LECTURE_13_NAME}.pdf",
    )
    notes: LectureResource = LectureResource(
        f"Lecture Notes - {LECTURE_13_NAME}",
        static_url=f"generated/pdfs/LN13 {LECTURE_13_NAME}.pdf",
    )


class LectureResources(ResourceCollection):
    title: str = "Lectures"
    intro: IntroLectureResources = IntroLectureResources()
    getting_started: GettingStartedLectureResources = GettingStartedLectureResources()
    depth_excel: DepthFinancialModelExcelLectureResources = DepthFinancialModelExcelLectureResources()
    beyond_initial_python: GoingBeyondInitialPythonLectureResources = GoingBeyondInitialPythonLectureResources()
    depth_python: DepthFinancialModelPythonLectureResources = DepthFinancialModelPythonLectureResources()
    visualization: VisualizationLectureResources = VisualizationLectureResources()
    sensitivity_analysis: SensitivityAnalysisLectureResources = SensitivityAnalysisLectureResources()
    probability: ProbabilityLectureResources = ProbabilityLectureResources()
    combining_excel_python: CombiningExcelPythonLectureResources = CombiningExcelPythonLectureResources()
    monte_carlo: MonteCarloLectureResources = MonteCarloLectureResources()
    dcf_cost_capital: DCFCostCapitalLectureResources = DCFCostCapitalLectureResources()
    dcf_fcf: DCFFCFLectureResources = DCFFCFLectureResources()
    advanced: AdvancedLectureResources = AdvancedLectureResources()


class VisualizationExternalResources(ResourceCollection):
    title: str = "Visualization External Resources"
    pandas_official_intro: LectureResource = LectureResource(
        f"10 Minutes to Pandas (Official Intro)",
        external_url='https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html',
    )
    pandas_styling_guide: LectureResource = LectureResource(
        'Pandas Official Styling Guide',
        external_url='https://pandas.pydata.org/pandas-docs/stable/user_guide/style.html',
    )
    pandas_visualization_guide: LectureResource = LectureResource(
        'Pandas Official Visualization Guide',
        external_url='https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html',
    )


class GeneralPythonExternalResources(ResourceCollection):
    title: str = 'Python External Resources'
    imports_guide = LectureResource(
        'Guide to Python Imports',
        external_url='https://realpython.com/absolute-vs-relative-python-imports/'
    )


class ExternalResources(ResourceCollection):
    title: str = 'External Resources'
    python: GeneralPythonExternalResources = GeneralPythonExternalResources()
    visualization: VisualizationExternalResources = VisualizationExternalResources()


class FinancialModelingResources(ResourceCollection):
    title: str = "Financial Modeling Resources"
    labs: LabResources = LabResources()
    examples: ExampleResources = ExampleResources()
    projects: ProjectResources = ProjectResources()
    course_materials: CourseMaterialsResources = CourseMaterialsResources()
    lectures: LectureResources = LectureResources()
    external: ExternalResources = ExternalResources()


RESOURCES = FinancialModelingResources()
RESOURCES.validate_locations()
