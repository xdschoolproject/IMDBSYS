from django import forms
from .models import PortfolioStocks

class AddPositionForm(forms.ModelForm):
    class Meta:
        model = PortfolioStocks
        fields = ["stock_id", "quantity", "purchase_price", "purchase_date"]
        widgets = {
            "purchase_date": forms.DateInput(attrs={"type": "date"})
        }
