import yfinance as yf
import pandas as pd
from enum import Enum

from thestrat import strat_identification


pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 25)
pd.set_option('display.expand_frame_repr', False)


class Timeframe(Enum):
    MINUTES_15 = ('7d', '15m')
    MINUTES_30 = ('7d', '30m')
    MINUTES_60 = ('7d', '60m')
    HOURS_4 = ('30d', '4h')
    DAYS_1 = ('5y', '1d')
    WEEKS_1 = ('5y', '1wk')
    MONTHS_1 = ('5y', '1mo')
    QUARTERS_1 = ('5y', '3mo')


def fetch_symbol_data(symbol: str, tf: Timeframe) -> pd.DataFrame:
    period, interval = tf.value
    ticker = yf.Ticker(symbol)
    df = ticker.history(period=period, interval=interval)
    return df


def main():
    symbols = ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'TSLA']

    for symbol in symbols:
        for tf in Timeframe:
            print(f'fetching {symbol} {tf.name} data..')
            df = fetch_symbol_data(symbol, tf)
            df = strat_identification(df)
            print(df.head())
            df.to_csv(f'data/{symbol}_{tf.name}.csv')


if __name__ == '__main__':
    main()
