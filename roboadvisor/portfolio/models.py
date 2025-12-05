from django.db import models
from django.contrib.auth.models import User

class Portfolio(models.Model):
    portfolio_id = models.AutoField(primary_key=True)
    portfolio_name = models.CharField(max_length=255)
    created_date = models.DateField()
    total_value = models.DecimalField(max_digits=15, decimal_places=2)
    risk_profile = models.CharField(
        max_length=50,
        choices=[
            ("Low", "Low"),
            ("Medium", "Medium"),
            ("High", "High"),
        ]
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "Portfolio"

    def __str__(self):
        return self.portfolio_name


class PortfolioStocks(models.Model):
    portfolio_stock_id = models.AutoField(primary_key=True)
    quantity = models.IntegerField()
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    current_value = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_date = models.DateField()

    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    stock_id = models.IntegerField()  # use real FK later

    class Meta:
        db_table = "Portfolio_Stocks"

    def __str__(self):
        return f"Stock {self.stock_id} in Portfolio {self.portfolio.portfolio_id}"
