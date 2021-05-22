from scraping.models import StockData
from celery import shared_task
# scraping
import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
import lxml
# scraping function


@shared_task
def status_invest_data():
    stock_list = []
    try:
        print('Starting the scraping tool')
        # execute my request, parse the data using XML
        # parser in BS4
        r = requests.get('https://statusinvest.com.br/acoes/busca-avancada')
        soup = BeautifulSoup(r.content, features='xml')
        # select only the "items" I want from the data
        stocks = soup.findAll('item')

        # for each "item" I want, parse it into a list
        for item in stocks:
            ticker = item.find('ticker').text
            peg_ratio = item.find('pegRatio')
            dividend_yield = item.find('dy')
            # print(published, published_wrong) # checking correct date format
            # create an "stock" object with the data
            # from each "item"
            stock = {
                'ticker': ticker,
                'peg': peg_ratio,
                'dy': dividend_yield,
            }
            # append my "stock_list" with each "stock" object
            stock_list.append(stock)
            print('Finished scraping the stocks')

            # after the loop, dump my saved objects into a .txt file
            return save_function(stock_list)
    except Exception as e:
        print('The scraping job failed. See exception:')
        print(e)

@shared_task(serializer='json')
def save_function(stock_list):
    print('starting')
    new_count = 0

    for stock in stock_list:
        try:
            StockData.objects.create(
                ticker = stock['ticker'],
                peg_ratio = stock['peg'],
                dividend_yield = stock['dy'],
            )
            new_count += 1
        except Exception as e:
            print('failed at latest_stock is none')
            print(e)
            break
    return print('finished')