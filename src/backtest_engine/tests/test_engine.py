import pandas as pd
import numpy as np
from backtest_engine.engine import BacktestEngine
from backtest_engine.strategy import MovingAverageStrategy


def test_backtest_runs():
    data = pd.DataFrame({
        "price": np.random.rand(100),
    })
    data["returns"] = data["price"].pct_change().fillna(0)

    strategy = MovingAverageStrategy()
    engine = BacktestEngine(data, strategy)

    equity = engine.run()

    assert len(equity) == 100
