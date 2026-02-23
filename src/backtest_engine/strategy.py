import pandas as pd


class MovingAverageStrategy:
    def __init__(self, short_window: int = 20, long_window: int = 50):
        self.short_window = short_window
        self.long_window = long_window

    def generate_signals(self, data: pd.DataFrame):
        signals = pd.Series(index=data.index, dtype=float)

        short_ma = data["price"].rolling(self.short_window).mean()
        long_ma = data["price"].rolling(self.long_window).mean()

        signals[short_ma > long_ma] = 1
        signals[short_ma <= long_ma] = 0

        return signals
