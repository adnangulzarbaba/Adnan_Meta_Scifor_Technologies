import requests
import pandas as pd
from textblob import TextBlob

# Function to fetch news articles
def fetch_news(stock_symbol):
    api_key = os.getenv('NEWS_API_KEY')  # Use environment variable for API key
    url = f'https://newsapi.org/v2/everything?q={stock_symbol}&apiKey={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        articles = response.json()['articles']
        return articles
    else:
        return []

# Function to analyze sentiment of articles
def analyze_sentiment(articles):
    sentiment_scores = []
    for article in articles:
        content = article['description'] if article['description'] else ''
        analysis = TextBlob(content)
        sentiment_scores.append(analysis.sentiment.polarity)  # Range: -1 (negative) to 1 (positive)
    return sentiment_scores

# Function to calculate moving averages
def calculate_moving_averages(data):
    data['Daily_MA'] = data['Close'].rolling(window=1).mean()          # Daily
    data['Weekly_MA'] = data['Close'].rolling(window=5).mean()          # Weekly (5 trading days)
    data['Monthly_MA'] = data['Close'].rolling(window=20).mean()        # Monthly (20 trading days)
    data['Quarterly_MA'] = data['Close'].rolling(window=60).mean()      # Quarterly (60 trading days)
    data['Semiannual_MA'] = data['Close'].rolling(window=126).mean()    # Semiannual (126 trading days)
    data['Annual_MA'] = data['Close'].rolling(window=252).mean()        # Annual (252 trading days)
    return data
