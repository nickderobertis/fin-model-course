import math
import numpy as np
import pandas as pd


class RetirementModel:

    def __init__(self, begin_salary=60000, promo_every_n_years=5, cost_of_living_raise=0.02, promo_raise=0.15,
                 savings_rate=0.25,
                 interest=0.05, annual_spend_retire=40000, years_in_retire=25):
        self.begin_salary = begin_salary
        self.promo_every_n_years = promo_every_n_years
        self.cost_of_living_raise = cost_of_living_raise
        self.promo_raise = promo_raise
        self.savings_rate = savings_rate
        self.interest = interest
        self.annual_spend_retire = annual_spend_retire
        self.years_in_retire = years_in_retire
        self.salary_model = SalaryModel(
            begin_salary=begin_salary,
            promo_every_n_years=promo_every_n_years,
            cost_of_living_raise=cost_of_living_raise,
            promo_raise=promo_raise
        )
        self.wealth_model = WealthModel(
            self.salary_model,
            begin_salary=begin_salary,
            savings_rate=savings_rate,
            interest=interest,
            desired_cash=self.desired_cash
        )

    def years_to_retirement(self):
        max_year = 100  # we'll evaluate up until 100 years, there are more elegant ways where we wouldn't have to specify a limit
        wealths = self.wealth_model.wealths(max_year)
        year = 0
        for i, wealth in enumerate(wealths):
            year = i + 1
            if wealth > self.desired_cash:
                break
        return year

    @property
    def desired_cash(self):
        return np.pv(self.interest, self.years_in_retire, -self.annual_spend_retire, 0)

    def get_df(self, num_years: int):
        df = pd.DataFrame()
        df['Time'] = [t + 1 for t in np.arange(num_years)]
        df['Salaries'] = self.salary_model.salaries(num_years)
        df['Wealths'] = self.wealth_model.wealths(num_years)
        return df

    def get_formatted_df(self, num_years: int):
        df = self.get_df(num_years)
        for col in ['Salaries', 'Wealths']:
            df[col] = df[col].apply(lambda x: fr'{x:,.0f}')
        return df


class SalaryModel:

    def __init__(self, begin_salary=60000, promo_every_n_years=5, cost_of_living_raise=0.02, promo_raise=0.15):
        self.begin_salary = begin_salary
        self.promo_every_n_years = promo_every_n_years
        self.cost_of_living_raise = cost_of_living_raise
        self.promo_raise = promo_raise

    def num_promotions(self, year):
        return math.floor(year / self.promo_every_n_years)

    def salary(self, year):
        return self.begin_salary * (1 + self.cost_of_living_raise) ** year * (
                    1 + self.promo_raise) ** self.num_promotions(year)

    def salaries(self, max_year):
        return [self.salary(year) for year in range(1, max_year + 1)]


class WealthModel:

    def __init__(self, salary_model, begin_salary=60000, savings_rate=0.25, interest=0.05, desired_cash=1500000):
        self.salary_model = salary_model
        self.begin_salary = begin_salary
        self.savings_rate = savings_rate
        self.interest = interest
        self.desired_cash = desired_cash

    def wealth(self, year):
        salaries = self.salary_model.salaries(year)
        wealth_output = self.begin_salary * self.savings_rate
        for salary in salaries:
            # Investment return
            wealth_output *= (1 + self.interest)

            # Add salary
            wealth_output += salary * self.savings_rate
        return wealth_output

    def wealths(self, max_year):
        salaries = self.salary_model.salaries(max_year)
        wealth_output = []
        for i, salary in enumerate(salaries):
            # Investment return
            if i == 0:
                new_wealth = self.begin_salary * self.savings_rate
            else:
                new_wealth = wealth_output[i - 1]
            new_wealth *= (1 + self.interest)

            # Add salary
            new_wealth += salary * self.savings_rate
            wealth_output.append(new_wealth)
        return wealth_output

