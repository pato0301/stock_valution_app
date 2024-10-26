import streamlit as st
import pandas as pd
from src.utils import fetch_stock_data, plot_stock_valuation, get_sorted_stocks

st.title("Stock Valuation Analysis")

tickers_input = st.text_input("Enter a comma-separated list of ticker symbols (e.g., AAPL, MSFT, GOOGL):")
if tickers_input:
    tickers = [ticker.strip() for ticker in tickers_input.split(",")]

    stock_data = fetch_stock_data(tickers)

    st.subheader("Stock Data")
    st.dataframe(stock_data)

    st.subheader("Stock Valuation Chart")
    plot_stock_valuation(stock_data)

    st.subheader("Stocks Sorted by P/E Ratio (from undervalued to overvalued)")
    sorted_stocks = get_sorted_stocks(stock_data)
    st.dataframe(sorted_stocks)