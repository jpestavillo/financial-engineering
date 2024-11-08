from typing import Optional

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


class Amortization:

    def __init__(self, amount: float, rate: float, n: int):
        self.amount = amount
        self.rate = rate
        self.n = n

    @property
    def annuity(self) -> float:
        return self.amount * self.rate / (1 - (1 + self.rate) ** -self.n)

    def get_table(self, save_file: Optional[str] = None) -> pd.DataFrame:
        table_amortization = pd.DataFrame(columns=['t', 'B', 'A', 'P', 'I'])
        i = 0
        table_amortization.loc[i] = [i, self.amount, np.nan, np.nan, np.nan]

        def make_table(balance, amortization_table, t):
            if abs(round(balance, 0)) != 0:
                interest = amortization_table['B'][t] * self.rate
                pay_to_cap = self.annuity - interest
                balance = amortization_table['B'][t] - pay_to_cap
                t += 1
                amortization_table.loc[t] = [int(t), balance, self.annuity, pay_to_cap, interest]
                make_table(balance, amortization_table, t)

        make_table(self.amount, table_amortization, i)
        if save_file:
            table_amortization.to_csv(save_file, index=False)
        return table_amortization

    def plot(self, show: bool = False, save_file: Optional[str] = None) -> None:
        table_amortization = self.get_table()
        ind = np.arange(self.n+1)
        payment = table_amortization['P'].fillna(0)
        interest = table_amortization['I'].fillna(0)

        fig = plt.figure()
        plt.bar(ind, payment, label='P')
        plt.bar(ind, interest, label='I', bottom=payment)

        plt.xticks(ind, ind)
        plt.ylabel('$$$')
        plt.xlabel('t')
        plt.title('Amortization Payment')
        plt.legend(loc="upper left")
        plt.grid()

        if save_file:
            fig.savefig(save_file)
        if show:
            plt.show()
        return None
