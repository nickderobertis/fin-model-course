

class Car:

    def __init__(self, make, model, gas_pct=0.5):
        self.make = make
        self.model = model
        self.gas_pct = gas_pct

    def drive(self):
        self.gas_pct -= 0.1
        if self.gas_pct < 0:
            self.gas_pct = 0
            print(f'The {self.make_and_model} is out of gas!')
        else:
            print(f'The {self.make_and_model} is driving away!')
            self.show_gas()

    def fill_up(self):
        self.gas_pct = 1
        self.show_gas()

    def show_gas(self):
        print(f'The gas is now at {self.gas_pct:.0%}')

    @property
    def make_and_model(self):
        return f'{self.make} {self.model}'

    def __repr__(self):
        return f'Car(make={self.make}, model={self.model})'
