from django.urls import path
from . import views

urlpatterns = [
    path("", views.portfolio_view, name="portfolio"),
    path("add/", views.add_position, name="add_position"),
    path('get-latest-price/', views.get_latest_price, name='get_latest_price'),  # NEW
]
