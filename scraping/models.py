from django.db import models

# Create your models here.
class StockData(models.Model):
    ticker = models.CharField(max_length=10)

    peg_ratio = models.FloatField(max_length=100)

    dividend_yield = models.FloatField(max_length=100)

    # price_per_lpa = models.FloatField(max_length=100)

    # lpa = models.FloatField(max_length=100)

    # vpa = models.FloatField(max_length=100)

    # roe = models.FloatField(max_length=100)

    # cagr_profit = models.FloatField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)