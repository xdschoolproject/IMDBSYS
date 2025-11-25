# myapp/admin.py
from django.contrib import admin
from .models import StockRecord  # replace MyModel with your actual model(s)

admin.site.register(StockRecord)
