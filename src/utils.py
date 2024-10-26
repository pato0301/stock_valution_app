import yfinance as yf
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from typing import List, Tuple

def fetch_stock_data(tickers: List[str]) -> pd.DataFrame:
    data = []
    for ticker in tickers:
        stock = yf.Ticker(ticker)
        info = stock.info
        data.append({
            "Ticker": ticker,
            "P/E Ratio": info.get("trailingPE", None),
            "EPS Growth (5Y)": info.get("fiveYearAvgEPSGrowth", None)
        })
    return pd.DataFrame(data)

def plot_stock_valuation(stock_data: pd.DataFrame) -> None:
    plt.figure(figsize=(10, 8))
    sns.scatterplot(
        data=stock_data,
        x="EPS Growth (5Y)",
        y="P/E Ratio",
        hue="Ticker",
        style="Ticker",
        s=100
    )
    plt.axline((0, 0), slope=1, color="gray", linestyle="--")
    plt.xlabel("5-Year Average EPS Growth (%)")
    plt.ylabel("P/E Ratio (TTM)")
    plt.title("Stock Valuation Analysis")
    plt.legend(loc="upper right")
    plt.grid(True)
    plt.show()

def get_sorted_stocks(stock_data: pd.DataFrame) -> pd.DataFrame:
    sorted_data = stock_data.sort_values(by="P/E Ratio", ascending=True).reset_index(drop=True)
    return sorted_data