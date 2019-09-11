import numpy as np


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

    def __init__(self, d_0, g_d, begin_advertise_year, max_year):
        self.d_0 = d_0
        self.g_d = g_d
        self.begin_advertise_year = begin_advertise_year
        self.max_year = max_year

    @property
    def quantities(self):
        return [self.d_0] * (self.begin_advertise_year - 1) + \
               [self.d_0 * (1 + self.g_d) ** (i + 1) for i in range(self.max_year - self.begin_advertise_year)]


class PhoneManufacturingModel:

    def __init__(self, n_phones, price_scrap, price_phone, n_life, n_machines, d_0, g_d, max_year, interest):
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

        self.demand = Demand(d_0, g_d, self.begin_advertise_year, max_year)
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

