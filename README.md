# Stock Valuation Analysis App

## Overview

The Stock Valuation Analysis App is a web application built with Streamlit that allows users to analyze stock data based on P/E ratios and 5-year average EPS growth. Users can input a list of ticker symbols, and the app fetches the relevant data using the `yfinance` library. It provides visualizations to help users understand the valuation of stocks and see which are undervalued or overvalued.

## Features

- **Fetch Stock Data**: Input ticker symbols to retrieve stock data, including P/E ratios and EPS growth.
- **Data Visualization**: A scatter plot displays the relationship between EPS growth and P/E ratios.
- **Sorting**: The app sorts stocks based on P/E ratios, helping users identify potentially undervalued stocks.

## Requirements

- Python 3.x
- Streamlit
- yfinance
- pandas
- seaborn
- matplotlib

## Setup

To set up the project, follow these steps:

1. **Clone the Repository**:

```bash
git clone <repository-url>
cd <repository-directory>
```

2. Create a Conda Environment: You can create a new conda environment using the provided environment.yml file. Make sure you have Conda installed.

```bash
conda env create -f environment.yml
```

3. Activate the Environment:

```bash
conda activate stock_valuation
```

4. Install Dependencies: Ensure that all necessary packages are installed. This is usually done by the environment.yml, but you can run:

```bash
pip install -r requirements.txt
```

## Running the App

To run the Streamlit app, use the following command:

```bash
streamlit run app.py
```

This command will start a local web server and open the app in your default web browser.

## Usage

1. Input Tickers: Enter a comma-separated list of ticker symbols (e.g., AAPL, MSFT, GOOGL) in the input box provided on the app's interface.
2. View Stock Data: The app will display the fetched stock data in a table format.
3. Analyze Stock Valuation: View the stock valuation chart to analyze the relationship between P/E ratios and EPS growth.
4. Sorted Stocks: See a table of stocks sorted by P/E ratio, from undervalued to overvalued.

## Testing

To run the unit tests for this project, you can execute:

```bash
python -m unittest discover -s tests
```

## Contributions

Contributions are welcome! Please feel free to submit a pull request or open an issue if you encounter any bugs or have suggestions for improvement.