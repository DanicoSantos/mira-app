from django.shortcuts import render
from django.views import generic
from scraping.models import StockData

class HomePageView(generic.ListView):
    template_name = 'test.html'
    context_object_name = 'stock'

    def get_queryset(self):
        return StockData.objects.all()