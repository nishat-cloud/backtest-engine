import pandas as pd
import numpy as np


class BacktestEngine:
    def __init__(self, data: pd.DataFrame, strategy, initial_capital: float = 100000):
        self.data = data
        self.strategy = strategy
        self.initial_capital = initial_capital
        self.positions = None
        self.returns = None

    def run(self):
        signals = self.strategy.generate_signals(self.data)
        self.positions = signals.shift(1).fillna(0)
        self.returns = self.positions * self.data["returns"]

        equity_curve = (1 + self.returns).cumprod() * self.initial_capital
        return equity_curve
