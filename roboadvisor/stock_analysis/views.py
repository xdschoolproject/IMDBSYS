# stock_analysis/views.py
from django.shortcuts import render, redirect
import yfinance as yf
from django.contrib import messages
import json

# Import the model from the current app
from .models import StockRecord

ALLOWED_TICKERS = ["AAPL", "TSLA", "MSFT", "AMZN", "NVDA"]

def stocks_view(request):
    # --- 1. HANDLE FORM SUBMISSION (WRITE TO DB) ---
    if request.method == "POST":
        ticker = request.POST.get("ticker", "").upper()
        start_date = request.POST.get("start_date")
        end_date = request.POST.get("end_date")

        if ticker in ALLOWED_TICKERS and start_date and end_date:
            try:
                # A. CLEAR OLD DATA
                # We clear the table so the database only holds the "current" analysis.
                # This ensures the Dashboard (Home) sees exactly what is here.
                StockRecord.objects.all().delete()

                # B. FETCH NEW DATA
                stock = yf.Ticker(ticker)
                data = stock.history(start=start_date, end=end_date)
                
                # C. SAVE TO DATABASE
                for index, row in data.iterrows():
                    StockRecord.objects.create(
                        ticker=ticker,
                        date=index.date(),
                        open_price=row['Open'],
                        high_price=row['High'],
                        low_price=row['Low'],
                        close_price=row['Close'],
                        volume=int(row['Volume'])
                    )
                messages.success(request, f"Successfully loaded {ticker}")
            except Exception as e:
                print(f"Error: {e}")
                messages.error(request, "Error fetching stock data.")

        return redirect("stocks") # Redirect to self to clear POST data

    # --- 2. DISPLAY DATA (READ FROM DB) ---
    stocks = StockRecord.objects.all().order_by('date')

    # Prepare chart data for the template
    chart_labels = [stock.date.strftime("%Y-%m-%d") for stock in stocks]
    chart_data = [stock.close_price for stock in stocks]

    context = {
        "stocks": stocks,
        "chart_labels": json.dumps(chart_labels),
        "chart_data": json.dumps(chart_data)
    }

    return render(request, "stock_analysis/stocks.html", context)