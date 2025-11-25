from django.shortcuts import render, redirect
import yfinance as yf
from .models import StockRecord
import json  # needed to pass data to template

ALLOWED_TICKERS = ["AAPL", "TSLA", "MSFT", "AMZN", "NVDA"]

def stocks_view(request):
    if request.method == "POST":
        ticker = request.POST.get("ticker", "").upper()
        start_date = request.POST.get("start_date")
        end_date = request.POST.get("end_date")

        if ticker in ALLOWED_TICKERS and start_date and end_date:
            # Fetch historical stock data
            stock = yf.Ticker(ticker)
            data = stock.history(start=start_date, end=end_date)
            
            # Save each day in the database
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
        print(f"{ticker} successfully added to your Database!")
        return redirect("stocks")

    # GET request – display saved stocks
    stocks = StockRecord.objects.all().order_by('date')

    # Prepare chart data
    chart_labels = [stock.date.strftime("%Y-%m-%d") for stock in stocks]
    chart_data = [stock.close_price for stock in stocks]

    context = {
        "stocks": stocks,
        "chart_labels": json.dumps(chart_labels),
        "chart_data": json.dumps(chart_data)
    }


    return render(request, "stock_analysis/stocks.html", context)