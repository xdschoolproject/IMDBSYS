import feedparser
from django.shortcuts import render, redirect

# 1. HOME VIEW (Dashboard + News)
def home(request):
    rss_url = "https://finance.yahoo.com/rss/topstories"
    # Make sure 'feedparser' is installed: pip install feedparser
    feed = feedparser.parse(rss_url)
    
    articles = []
    # Limit to 6 articles
    for entry in feed.entries[:6]:
        article = {
            'title': entry.title,
            'link': entry.link,
            'published': entry.published,
            'summary': entry.summary if 'summary' in entry else '', 
            'image': None 
        }
        
        # Try to extract image from media_content if available
        if 'media_content' in entry:
            for media in entry.media_content:
                if 'url' in media:
                    article['image'] = media['url']
                    break 

        articles.append(article)

    return render(request, 'home_page/home.html', {'articles': articles})

# 2. STOCK ANALYSIS (Redirect to Streamlit)
def stock_analysis(request):
    # Adjust localhost port if your Streamlit runs elsewhere
    return redirect("http://localhost:8501")

# 3. AI ADVISOR VIEW
def ai_advisor(request):
    return render(request, 'home_page/AiAdvisor.html')

# 4. PORTFOLIO VIEW
def portfolio(request):
    return render(request, 'portfolio/portfolio.html')

# 5. STOCKS / ASSETS VIEW
def stocks(request):
    return render(request, 'stock_analysis/stocks.html')

# 6. MANAGE ACCOUNT VIEW (NEWLY ADDED)
def account(request):
    # This assumes your HTML file is named 'account.html'
    # If it is named 'manage_account.html', change it below.
    return render(request, 'home_page/account.html')