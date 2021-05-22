from django.shortcuts import render
from django.views import generic
from scraping.models import StockData

def test_vue(request):
    return render(request, 'client/test.html')