# home_page/views.py
import feedparser
import json
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout

# IMPORTANT: Import the StockRecord model from the OTHER app
from stock_analysis.models import StockRecord

# 1. HOME VIEW (Dashboard)
def home(request):
    # --- A. NEWS LOGIC ---
    rss_url = "https://finance.yahoo.com/rss/topstories"
    feed = feedparser.parse(rss_url)
    articles = []
    for entry in feed.entries[:6]:
        article = {
            'title': entry.title,
            'link': entry.link,
            'published': entry.published,
            'summary': entry.summary if 'summary' in entry else '', 
            'image': None 
        }
        if 'media_content' in entry:
            for media in entry.media_content:
                if 'url' in media:
                    article['image'] = media['url']
                    break 
        articles.append(article)

    # --- B. STOCK GRAPH LOGIC (REFLECTS STOCKS PAGE) ---
    # We query the SAME table that stock_analysis/views.py writes to.
    stocks_data = StockRecord.objects.all().order_by('date')

    chart_labels = []
    chart_data = []
    current_ticker = "Overview"

    if stocks_data.exists():
        chart_labels = [stock.date.strftime("%Y-%m-%d") for stock in stocks_data]
        chart_data = [float(stock.close_price) for stock in stocks_data]
        current_ticker = stocks_data.last().ticker

    context = {
        'articles': articles,
        'chart_labels': json.dumps(chart_labels),
        'chart_data': json.dumps(chart_data),
        'current_ticker': current_ticker,
    }

    return render(request, 'home_page/home.html', context)

# 2. STOCK ANALYSIS REDIRECT
def stock_analysis(request):
    return redirect("http://localhost:8501")

# 3. AI ADVISOR
def ai_advisor(request):
    return render(request, 'home_page/AiAdvisor.html')

# 4. PORTFOLIO
def portfolio(request):
    return render(request, 'portfolio/portfolio.html')

# 5. STOCKS PAGE LINK
# Note: This just renders the template if you access it via this URL, 
# but usually, you map the URL directly to the stock_analysis view.
def stocks(request):
    # Ideally, you should redirect to the view in the other app, 
    # or import that view here. For now, assuming URL routing handles it:
    return render(request, 'stock_analysis/stocks.html')

# 6. ACCOUNT MANAGEMENT
@login_required
def account(request):
    user = request.user 
    if request.method == 'POST':
        new_username = request.POST.get('username')
        new_first_name = request.POST.get('first_name')
        new_last_name = request.POST.get('last_name')
        new_email = request.POST.get('email')

        if User.objects.filter(username=new_username).exclude(pk=user.pk).exists():
            messages.error(request, "Username already taken.")
        else:
            user.username = new_username
            user.first_name = new_first_name
            user.last_name = new_last_name
            user.email = new_email
            user.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('account')

    context = { "user": user }
    return render(request, 'home_page/account.html', context)

# 7. LOGOUT
def logout_view(request):
    logout(request)
    return redirect('home')