import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Function to fetch stock data
def fetch_stock_data(tickers, period):
    stock_data = {}
    for ticker in tickers:
        data = yf.download(ticker + '.NS', period=period, interval='1d')
        data.reset_index(inplace=True)
        stock_data[ticker] = data
    return stock_data

# Function to fetch latest stock prices
def fetch_latest_prices(tickers):
    latest_prices = {}
    for ticker in tickers:
        stock = yf.Ticker(ticker + '.NS')
        latest_prices[ticker] = stock.history(period='1d')['Close'].iloc[-1]
    return latest_prices

# Function to calculate moving averages
def calculate_moving_averages(stock_data):
    for ticker in stock_data:
        stock_data[ticker]['50_MA'] = stock_data[ticker]['Close'].rolling(window=50).mean()
        stock_data[ticker]['200_MA'] = stock_data[ticker]['Close'].rolling(window=200).mean()

# Function to plot stock data for comparative analysis
def plot_comparative_stock_data(stock_data, tickers, timeframe):
    plt.figure(figsize=(12, 6))
    for ticker in tickers:
        if timeframe == 'Daily':
            plt.plot(stock_data[ticker]['Date'], stock_data[ticker]['Close'], label=f'{ticker} Close Price (INR)')
        else:
            # Resample the data for weekly or monthly averages
            resampled_data = stock_data[ticker].set_index('Date').resample(timeframe[0]).mean().reset_index()
            plt.plot(resampled_data['Date'], resampled_data['Close'], label=f'{ticker} {timeframe} Close Price (INR)')

    plt.title(f'Comparative Stock Prices ({timeframe})')
    plt.xlabel('Date')
    plt.ylabel('Price (in ₹)')
    plt.legend()
    plt.grid()
    st.pyplot(plt)

# Streamlit App
st.title('Real-Time Stock Market Dashboard (INR)')

# User input for stock tickers
tickers = st.text_input("Enter Stock Tickers (comma-separated, e.g., RELIANCE, TCS):", "RELIANCE, TCS")
tickers = [ticker.strip() for ticker in tickers.split(',')]

# Timeframe selection
timeframe = st.selectbox("Select Timeframe:", ["Daily", "Weekly", "Monthly"])

if tickers:
    # Determine the period based on the selected timeframe
    if timeframe == "Daily":
        period = '1y'  # 1 year for daily
    elif timeframe == "Weekly":
        period = '5y'  # 5 years for weekly
    else:  # Monthly
        period = '5y'  # 5 years for monthly

    # Fetch stock data
    stock_data = fetch_stock_data(tickers, period)

    # Fetch latest stock prices
    latest_prices = fetch_latest_prices(tickers)
    st.subheader('Latest Stock Prices (INR)')
    for ticker, price in latest_prices.items():
        st.write(f"{ticker}: ₹{price:.2f}")

    # Calculate Moving Averages
    calculate_moving_averages(stock_data)

    # Display data and plot
    for ticker in tickers:
        st.subheader(f'{ticker} Stock Data (INR)')
        st.write(stock_data[ticker].tail())
    
    # Plot comparative stock data
    plot_comparative_stock_data(stock_data, tickers, timeframe)

    # Comparative Analysis: Displaying latest prices and moving averages in a table
    comparison_data = {
        "Ticker": [],
        "Latest Price (INR)": [],
        "50-Day MA (INR)": [],
        "200-Day MA (INR)": [],
    }

    for ticker in tickers:
        comparison_data["Ticker"].append(ticker)
        comparison_data["Latest Price (INR)"].append(f"₹{latest_prices[ticker]:.2f}")
        comparison_data["50-Day MA (INR)"].append(f"₹{stock_data[ticker]['50_MA'].iloc[-1]:.2f}" if not stock_data[ticker]['50_MA'].isna().all() else "N/A")
        comparison_data["200-Day MA (INR)"].append(f"₹{stock_data[ticker]['200_MA'].iloc[-1]:.2f}" if not stock_data[ticker]['200_MA'].isna().all() else "N/A")

    comparison_df = pd.DataFrame(comparison_data)
    st.subheader('Comparative Analysis of Stocks')
    st.write(comparison_df)

    # Downloadable reports
    for ticker in tickers:
        csv = stock_data[ticker].to_csv(index=False)
        st.download_button(
            label=f"Download {ticker} CSV",
            data=csv,
            file_name=f"{ticker}_stock_data.csv",
            mime="text/csv",
        )
