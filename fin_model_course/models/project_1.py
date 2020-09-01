import numpy as np
from scipy.optimize import minimize_scalar

# For bonus problem
ELASTICITY_CONSTANT_CASES = [
    (500, 900000),
    (200, 500000),
    (100, 300000),
]


class Machine:

    def __init__(self, n_phones, price_scrap, n_life, year_purchased):
        self.n_phones = n_phones
        self.price_scrap = price_scrap
        self.n_life = n_life
        self.year_purchased = year_purchased

    @property
    def units(self):
        return [0] * (self.year_purchased - 1) + [self.n_phones] * self.n_life


class MachineSet:

    def __init__(self, machines):
        self.machines = machines

    @property
    def units(self):
        num_years = max([len(machine.units) for machine in self.machines])
        output = [0] * num_years
        for i in range(num_years):
            for machine in self.machines:
                try:
                    output[i] += machine.units[i]
                except IndexError:
                    pass
        return output

    def cash_flows(self, price_phone, quantities_demanded):
        num_years = max([len(machine.units) + 1 for machine in self.machines])
        output = [0] * num_years
        for i in range(num_years):
            demanded = quantities_demanded[i]
            for machine in self.machines:
                try:
                    units = machine.units[i]
                except IndexError:
                    # Machine does not have output for this year
                    try:
                        machine.units[i - 1]
                        # Machine does have output last year. Therefore this is the scrap year
                        output[i] += machine.price_scrap
                    except IndexError:
                        # Machine has been out of operation for more than one year, it's done
                        pass
                    continue
                if units > demanded:
                    units = demanded
                output[i] += units * price_phone
                demanded -= units
        return output


class Demand:

    def __init__(self, d_0, g_d, begin_advertise_year, max_year, price, elasticity=20, demand_constant=300000,
                 bonus_problem=False):
        self.d_0 = d_0
        self.g_d = g_d
        self.begin_advertise_year = begin_advertise_year
        self.max_year = max_year
        self.elasticity = elasticity
        self.demand_constant = demand_constant
        self.bonus_problem = bonus_problem
        self.price = price

    @property
    def quantities(self):
        possible_quantities = [self.initial_demand] * (self.begin_advertise_year - 1) + \
               [self.initial_demand * (1 + self.g_d) ** (i + 1) for i in range((self.max_year - self.begin_advertise_year) + 1)]

        # Quantities will become negative if initial demand is negative, should be zero instead
        quantities = [max(0, q) for q in possible_quantities]

        return quantities

    @property
    def initial_demand(self):
        if not self.bonus_problem:
            return self.d_0

        return self.demand_constant - self.price * self.elasticity


class PhoneManufacturingModel:

    def __init__(self, n_phones=100000, price_scrap=50000, price_phone=2000, n_life=10, n_machines=5, d_0=100000,
                 g_d=0.2, max_year=20, interest=0.05,
                 elasticity=20, demand_constant=300000, bonus_problem=False):
        self.n_phones = n_phones
        self.price_scrap = price_scrap
        self.price_phone = price_phone
        self.n_life = n_life
        self.n_machines = n_machines
        self.d_0 = d_0
        self.g_d = g_d
        self.begin_advertise_year = n_machines + 1
        self.max_year = max_year
        self.interest = interest
        self.elasticity = elasticity
        self.demand_constant = demand_constant
        self.bonus_problem = bonus_problem

        self.demand = Demand(
            d_0,
            g_d,
            self.begin_advertise_year,
            max_year,
            price_phone,
            elasticity=elasticity,
            demand_constant=demand_constant,
            bonus_problem=bonus_problem
        )
        machines = [Machine(n_phones, price_scrap, n_life, i + 1) for i in range(n_machines)]
        self.machines = MachineSet(machines)

    @property
    def cash_flows(self):
        return self.machines.cash_flows(self.price_phone, self.demand.quantities)

    @property
    def pv(self):
        return np.npv(self.interest, [0] + self.cash_flows)

    @property
    def output_lines(self):
        output_lines = [
            f'PV is {self.pv:,.0f}.',
            f'Cash flows are: {[f"${cf:,.0f}" for cf in self.cash_flows]}',
            f'Units able to be produced are: {self.machines.units}',
            f'Quantities demanded are: {[f"{q:,.0f}" for q in self.demand.quantities]}'
        ]
        return output_lines

    @property
    def summary(self):
        return '\n'.join(self.output_lines)


#### Below for bonus problem ########

def get_neg_pv_for_price(price, elasticity, demand_constant):
    pmm = PhoneManufacturingModel(
        price_phone=price,
        elasticity=elasticity,
        demand_constant=demand_constant,
        bonus_problem=True
    )
    return -pmm.pv


def max_npv_setting_price_for_demand_params(elasticity_constant_tuples):
    for elasticity, demand_constant in elasticity_constant_tuples:
        res = minimize_scalar(get_neg_pv_for_price, args=(elasticity, demand_constant))
        price = res.x
        npv = -res.fun
        print(f'For E = {elasticity}, d_c = {demand_constant}: Price ${price:,.2f} achieves max NPV of {npv:,.0f}')