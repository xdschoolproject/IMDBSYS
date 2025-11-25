from django.urls import path
from . import views

urlpatterns = [
    # The Dashboard (Home)
    path('', views.home, name='home'),
    
    # The AI Advisor Page
    path('ai-advisor/', views.ai_advisor, name='ai_advisor'),

    # Stock Analysis Redirect
    path('stock-analysis/', views.stock_analysis, name='stock_analysis'),

    # Portfolio Page
    path('portfolio/', views.portfolio, name='portfolio'),

    # Stocks / Assets Page
    path('stocks/', views.stocks, name='stocks'),

    # Manage Account Page (NEWLY ADDED)
    # This 'name="account"' allows {% url 'account' %} to work in HTML
    path('account/', views.account, name='account'),
]