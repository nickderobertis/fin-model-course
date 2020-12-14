import re
import pandas as pd
import datetime
import numpy as np

# Regular expressions are outside the scope of the course, but they are very powerful
range_pattern = re.compile('([\d.]+)% - ([\d.]+)%')
libor_pattern = re.compile('LIBOR \+ ([\d.]+)%')


def standardize_fixed_coupons(coupon_str):
    """
    Strips percentages, takes averages of percentage ranges
    """
    # Handle missing values
    if pd.isnull(coupon_str):
        return coupon_str

    # More regular expression stuff. Extract the two percentages and take the average
    match = range_pattern.match(coupon_str)
    if match:
        bottom_pct = float(match.group(1))
        top_pct = float(match.group(2))
        return (top_pct + bottom_pct) / 2

    # Single percentage
    return float(coupon_str.strip('%'))


def standardize_floating_coupons(coupon_str, libor_rate):
    """
    Extracts percentages from string with LIBOR + pct, and fills in the value of LIBOR
    """
    # Handle missing values
    if pd.isnull(coupon_str):
        return coupon_str

    # More regular expression stuff. Extract the two percentages and take the average
    match = libor_pattern.match(coupon_str)
    if match:
        pct = float(match.group(1))
        return (libor_rate * 100) + pct

    # Shouldn't be hitting here on the current data
    return float(coupon_str.strip('%'))


def load_debt_details(file_path):
    """
    Loads the market value debt details from Capital IQ, taking the first table in the file.
    """
    debt_details = pd.read_excel(file_path, skiprows=12)
    fy_row_index = debt_details[debt_details['Description'] == 'Description'].index.values[0] - 1
    debt_details = debt_details.iloc[:fy_row_index].dropna(how='all')
    debt_details = debt_details.replace('-', np.nan)
    return debt_details


def standardize_maturity_dates(maturity):
    """
    Converts years into end of year
    """
    # Handle missing values and existing dates
    if not isinstance(maturity, (str, int)):
        return maturity

    # More regular expression stuff. Identify when it's just a year and create a date out of it
    if isinstance(maturity, int):
        return pd.to_datetime(f'Dec-31-{maturity}')

    # Regular date str
    return maturity


def assign_validity_of_bonds(debt_details):
    """
    Flag bonds as invalid if they do not have a coupon, do
    not have a maturity, or have a negative maturity.
    """
    debt_details['Valid'] = True

    # Set the value of Valid for the matching rows to False
    debt_details.loc[
        pd.isnull(debt_details['Coupon']) |
        pd.isnull(debt_details['Maturity (years)']) |
        (debt_details['Maturity (years)'] < 0),
        'Valid'
    ] = False


def years_until_from_date(date):
    """
    Calculate the number of years until a date, starting from today.
    """
    if pd.isnull(date):
        return np.nan
    today = datetime.datetime.today()
    diff = date - today
    seconds = diff.total_seconds()
    seconds_per_year = 60 * 60 * 24 * 365
    years_elapsed = seconds / seconds_per_year
    return years_elapsed


def clean_debt_details(debt_details, libor_rate):
    debt_details = debt_details.copy()  # don't modify the existing data

    # Sometimes whitespace comes in as \xa0 rather than a space, just replace it
    debt_details.columns = [col.replace('\xa0', ' ') for col in debt_details.columns]

    debt_details['Coupon/Base Rate'] = debt_details['Coupon/Base Rate'].apply(standardize_fixed_coupons)

    debt_details['Floating Rate'] = debt_details['Floating Rate'].apply(standardize_floating_coupons,
                                                                        libor_rate=libor_rate)
    debt_details['Coupon'] = debt_details['Coupon/Base Rate'].fillna(debt_details['Floating Rate'])
    debt_details['Coupon'] = debt_details['Coupon'] / 100

    debt_details['Maturity'] = debt_details['Maturity'].apply(standardize_maturity_dates)
    debt_details['Maturity (years)'] = debt_details['Maturity'].apply(years_until_from_date)

    assign_validity_of_bonds(debt_details)

    return debt_details


def load_and_clean_debt_details(file_path, libor_rate):
    debt_details = load_debt_details(file_path)
    debt_details = clean_debt_details(debt_details, libor_rate)
    return debt_details

