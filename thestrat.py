import pandas as pd
import numpy as np


def strat_identification(df: pd.DataFrame) -> pd.DataFrame:
    df['prev_high'] = df['High'].shift(1)
    df['prev_low'] = df['Low'].shift(1)

    inside = (df['High'] <= df['prev_high']) & (df['Low'] >= df['prev_low'])
    outside = (df['High'] > df['prev_high']) & (df['Low'] < df['prev_low'])
    two_up = df['High'] > df['prev_high']
    two_down = df['Low'] < df['prev_low']

    conditions = [inside, outside, two_up, two_down]
    choices = ['1', '3', '2U', '2D']
    df['strat_id'] = np.select(conditions, choices, default=np.nan)
    df['strat_id'] = df['strat_id'].astype('category')

    return df
