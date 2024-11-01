import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import requests

# Function to fetch news articles
def fetch_news(stock_symbol):
    api_key = st.secrets.get("news_api_key")  # Access the secret here
    if not api_key:
        st.error("News API key is missing!")
        return []
    
    url = f'https://newsapi.org/v2/everything?q={stock_symbol}&apiKey={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        articles = response.json().get('articles', [])
        return articles[:5]  # Limit to the top 5 articles
    else:
        st.error("Failed to fetch news articles.")
        return []

# Function to calculate moving averages
def calculate_moving_averages(data):
    data['Daily_MA'] = data['Close'].rolling(window=1).mean()
    data['Weekly_MA'] = data['Close'].rolling(window=5).mean()
    data['Monthly_MA'] = data['Close'].rolling(window=20).mean()
    data['Quarterly_MA'] = data['Close'].rolling(window=60).mean()
    data['Semiannual_MA'] = data['Close'].rolling(window=126).mean()
    data['Annual_MA'] = data['Close'].rolling(window=252).mean()
    return data

# Streamlit app
st.title("Stock Market Dashboard")

# Real-Time Stock Price Updates
stock_symbol = st.text_input("Enter stock symbol:")
if stock_symbol:
    try:
        stock_data = yf.Ticker(stock_symbol)
        # Display stock data
        st.write(stock_data.history(period="1d"))

        # Stock Performance Graphs
        data = stock_data.history(period="2y")  # Fetch 2 years of data for moving averages
        data = calculate_moving_averages(data)

        plt.figure(figsize=(12, 6))
        plt.plot(data.index, data['Close'], label='Closing Price', color='blue')
        plt.plot(data['Daily_MA'], label='Daily MA', linestyle='--', color='orange')
        plt.plot(data['Weekly_MA'], label='Weekly MA', linestyle='--', color='green')
        plt.plot(data['Monthly_MA'], label='Monthly MA', linestyle='--', color='purple')
        plt.plot(data['Quarterly_MA'], label='Quarterly MA', linestyle='--', color='red')
        plt.plot(data['Semiannual_MA'], label='Semiannual MA', linestyle='--', color='brown')
        plt.plot(data['Annual_MA'], label='Annual MA', linestyle='--', color='pink')

        plt.title(f"{stock_symbol} Performance Over Last 2 Years")
        plt.xlabel("Date")
        plt.ylabel("Price")
        plt.legend()
        st.pyplot(plt)

        # Fetch and display news articles
        articles = fetch_news(stock_symbol)
        if articles:
            st.write(f"Latest news articles for {stock_symbol}:")
            for article in articles:
                st.write(f"**Title:** {article['title']}")
                st.write(f"**Description:** {article['description']}")
                st.write(f"[Read more]({article['url']})")
        else:
            st.write("No articles found.")
    except Exception as e:
        st.error(f"Error fetching data for {stock_symbol}: {e}")
