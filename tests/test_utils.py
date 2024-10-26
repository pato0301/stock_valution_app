import unittest
from unittest.mock import patch
import pandas as pd
from src.utils import fetch_stock_data, plot_stock_valuation, get_sorted_stocks

class TestFetchStockData(unittest.TestCase):
    
    @patch("src.utils.yf.Ticker")
    def test_fetch_stock_data_success(self, mock_ticker):
        # Mocking the response from yfinance
        mock_ticker.return_value.info = {
            "trailingPE": 15.2,
            "fiveYearAvgEPSGrowth": 12.5
        }
        result = fetch_stock_data(["AAPL"])
        expected = pd.DataFrame({
            "Ticker": ["AAPL"],
            "P/E Ratio": [15.2],
            "EPS Growth (5Y)": [12.5]
        })
        pd.testing.assert_frame_equal(result, expected)
    
    @patch("src.utils.yf.Ticker")
    def test_fetch_stock_data_failure(self, mock_ticker):
        mock_ticker.return_value.info = {}
        result = fetch_stock_data(["INVALID"])
        expected = pd.DataFrame({
            "Ticker": ["INVALID"],
            "P/E Ratio": [None],
            "EPS Growth (5Y)": [None]
        })
        pd.testing.assert_frame_equal(result, expected)


class TestGetSortedStocks(unittest.TestCase):

    def test_get_sorted_stocks_success(self):
        # Test with a normal DataFrame and check if sorted correctly
        data = pd.DataFrame({
            "Ticker": ["AAPL", "MSFT", "GOOG"],
            "P/E Ratio": [15.2, 10.4, 20.5]
        })
        result = get_sorted_stocks(data)
        expected = pd.DataFrame({
            "Ticker": ["MSFT", "AAPL", "GOOG"],
            "P/E Ratio": [10.4, 15.2, 20.5]
        }).reset_index(drop=True)
        pd.testing.assert_frame_equal(result, expected)

    def test_get_sorted_stocks_failure(self):
        with self.assertRaises(KeyError):
            invalid_data = pd.DataFrame({
                "Ticker": ["AAPL", "MSFT", "GOOG"]
            })
            get_sorted_stocks(invalid_data)

if __name__ == "__main__":
    unittest.main()
