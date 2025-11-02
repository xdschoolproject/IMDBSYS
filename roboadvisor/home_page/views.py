import feedparser
from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    # RSS feed URL for Yahoo News
    rss_url = "https://finance.yahoo.com/rss/topstories"
    
    # Fetch the RSS feed and parse it using feedparser
    feed = feedparser.parse(rss_url)
    
    # Get the list of articles (limit to 6 latest articles)
    articles = []
    for entry in feed.entries[:6]:  # You can adjust this limit as needed
        article = {
            'title': entry.title,
            'link': entry.link,
            'published': entry.published,
            'image': None  # Default to no image
        }
        
        # Extract image URL from media:content
        if 'media_content' in entry:
            for media in entry.media_content:
                if 'url' in media:
                    article['image'] = media['url']  # Assign image URL to article

        articles.append(article)

    return render(request, 'home_page/home.html', {'articles': articles})


def stock_analysis(request):
    # Redirect to the Streamlit app URL (assuming it's running on localhost:8501)
    return redirect("http://localhost:8501")