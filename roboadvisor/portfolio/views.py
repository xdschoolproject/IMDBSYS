from django.shortcuts import render
from .models import Portfolio, PortfolioStocks
from .forms import AddPositionForm
import yfinance as yf
from django.http import JsonResponse

def portfolio_view(request):
    portfolio = Portfolio.objects.filter(user=request.user).first()
    stocks = portfolio.portfoliostocks_set.all() if portfolio else []

    return render(request, "portfolio/portfolio.html", {
        "portfolio": portfolio,
        "stocks": stocks,
    })

def add_position(request):
    portfolio = Portfolio.objects.filter(user=request.user).first()
    if request.method == "POST":
        form = AddPositionForm(request.POST)
        if form.is_valid():
            new_stock = form.save(commit=False)
            new_stock.portfolio = portfolio
            new_stock.save()
            return redirect("portfolio")
    else:
        form = AddPositionForm()
    
    return render(request, "portfolio/add_position.html", {"form": form})

def get_latest_price(request):
    ticker = request.GET.get('ticker')
    if not ticker:
        return JsonResponse({'price': None})
    try:
        stock = yf.Ticker(ticker)
        data = stock.history(period="1d")
        if not data.empty:
            latest_price = data['Close'].iloc[-1]
            return JsonResponse({'price': float(latest_price)})
        else:
            return JsonResponse({'price': None})
    except Exception:
        return JsonResponse({'price': None})