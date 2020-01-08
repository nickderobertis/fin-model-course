import pyexlatex as pl
import pyexlatex.table as lt
import pyexlatex.presentation as lp
import pyexlatex.graphics as lg
import pyexlatex.layouts as ll

salary_block_content = [
    lp.adjust_to_full_size_and_center(pl.Equation(str_eq=r'S_t = S_0 (1 + r_l)^t (1 + r_p)^p')),
    pl.UnorderedList([
        f'{pl.Equation(str_eq="S_t")}:  Salary at year {pl.Equation(str_eq="t")}',
        f'{pl.Equation(str_eq="S_0")}:  Starting wealth',
        f'{pl.Equation(str_eq="r_l")}:  Return for cost of living',
        f'{pl.Equation(str_eq="r_p")}:  Return for promotion',
        f'{pl.Equation(str_eq="t")}:  Number of years',
        f'{pl.Equation(str_eq="p")}:  Number of promotions',

    ])
]