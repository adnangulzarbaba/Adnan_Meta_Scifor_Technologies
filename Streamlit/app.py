import streamlit as st
import yfinance as yf
import plotly.graph_objs as go
import os
from utils import fetch_news, analyze_sentiment, calculate_moving_averages

# Streamlit app
st.title("Stock Market Dashboard")

# Sidebar for stock input
st.sidebar.title("Stock Market Dashboard")
stock_symbol = st.sidebar.text_input("Enter stock symbol:")

if stock_symbol:
    with st.spinner("Fetching data..."):
        stock_data = yf.Ticker(stock_symbol)

        # Display stock data
        st.markdown("## Real-Time Stock Price Updates")
        st.write(stock_data.history(period="1d"))

        # Stock Performance Graphs
        data = stock_data.history(period="2y")  # Fetch 2 years of data for moving averages
        data = calculate_moving_averages(data)

        # Plot using Plotly
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=data.index, y=data['Close'], mode='lines', name='Closing Price'))
        fig.add_trace(go.Scatter(x=data.index, y=data['Daily_MA'], mode='lines', name='Daily MA', line=dict(dash='dash')))
        fig.add_trace(go.Scatter(x=data.index, y=data['Weekly_MA'], mode='lines', name='Weekly MA', line=dict(dash='dash')))
        fig.add_trace(go.Scatter(x=data.index, y=data['Monthly_MA'], mode='lines', name='Monthly MA', line=dict(dash='dash')))
        fig.add_trace(go.Scatter(x=data.index, y=data['Quarterly_MA'], mode='lines', name='Quarterly MA', line=dict(dash='dash')))
        fig.add_trace(go.Scatter(x=data.index, y=data['Semiannual_MA'], mode='lines', name='Semiannual MA', line=dict(dash='dash')))
        fig.add_trace(go.Scatter(x=data.index, y=data['Annual_MA'], mode='lines', name='Annual MA', line=dict(dash='dash')))

        fig.update_layout(title=f"{stock_symbol} Performance Over Last 2 Years",
                          xaxis_title="Date",
                          yaxis_title="Price",
                          legend_title="Legend")

        st.plotly_chart(fig)

        # Fetch and display news articles
        articles = fetch_news(stock_symbol)
        st.markdown("## Latest News Articles")
        if articles:
            for article in articles:
                st.write(f"**Title:** {article['title']}")
                st.write(f"**Description:** {article['description']}")
                st.write(f"[Read more]({article['url']})")
                
            # Sentiment Analysis
            sentiment_scores = analyze_sentiment(articles)
            average_sentiment = sum(sentiment_scores) / len(sentiment_scores) if sentiment_scores else 0
            st.markdown("## Sentiment Analysis")
            st.write(f"Average Sentiment Score: {average_sentiment:.2f} (range: -1 to 1)")
            
            if average_sentiment > 0:
                st.success("Overall sentiment is positive!")
            elif average_sentiment < 0:
                st.error("Overall sentiment is negative!")
            else:
                st.warning("Overall sentiment is neutral.")
        else:
            st.write("No articles found.")
