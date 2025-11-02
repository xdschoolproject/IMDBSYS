import streamlit as st
import yfinance as yf
import pandas as pd
import os
import django
import sqlite3
import sys

# Add the parent directory of 'roboadvisor' to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "roboadvisor.settings")  # This tells Django where the settings file is located
django.setup()

# Import the Stock model from the Django app
from stock_analysis_back_end.models import Stock

# Get the path to the db.sqlite3 file in your Django project
db_path = os.path.join(os.path.dirname(__file__), '..', 'db.sqlite3')  # Moves 2 levels up to access the db.sqlite3 file
conn = sqlite3.connect(db_path)  # Now it connects to the correct SQLite file

# --- App Title ---
st.title("Stock Analysis Tool")

# --- Limit options to 5 stock tickers ---
tickers = ["AAPL", "GOOGL", "AMZN", "MSFT", "TSLA"]
ticker = st.selectbox("Select a Stock Ticker", tickers)

# --- Input: Date range ---
start_date = st.date_input("Start Date")
end_date = st.date_input("End Date")

# --- Button to fetch data ---
if st.button("Get Stock Data"):
    if ticker:
        # Fetch data from yfinance
        data = yf.download(ticker, start=start_date, end=end_date)

        if not data.empty:
            # --- Plot closing price ---
            st.subheader(f"Closing Price Chart for {ticker}")
            st.line_chart(data['Close'])

            # --- Save to Django database using ORM ---
            try:
                # Loop through the data and save each row to the Django database
                for index, row in data.iterrows():
                    stock_record = Stock(
                        date=index, 
                        open_price=row['Open'],
                        high_price=row['High'],
                        low_price=row['Low'],
                        close_price=row['Close'],
                        volume=row['Volume'],
                        ticker=ticker
                    )
                    stock_record.save()

                st.success("Data saved to database!")

            except Exception as e:
                st.error(f"Error saving to database: {e}")
        else:
            st.warning("No data found for this ticker.")
    else:
        st.warning("Please select a ticker symbol.")
