from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import requests
import os
import time


URL_TO_SCAN = "https://www.ebay-kleinanzeigen.de/s-muenster-%28westfalen%29/laptop/k0l929"
driver = webdriver.Chrome(executable_path='/Users/linushenn/Desktop/Chromedriver/chromedriver')


def scanning():
    headers = {
        'User-Agent': 'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}
    products = []
    locations = []
    prices = []
    views_total = []

    driver.get(URL_TO_SCAN)

    content = driver.page_source
    soup = BeautifulSoup(content, 'html.parser')
    for a in soup.find_all('a', href=True, attrs={'class': 'ellipsis'}):

        price = a.find('p', attrs={'class': 'aditem-main--middle--price'})
        product = a.find('a', attrs={'class': 'ellipsis'})
        location = a.find('div', attrs={'class': 'aditem-main--top--left'})

        products.append(str(product.text))
        prices.append(str(price.text))
        locations.append(str(location.text))


scanning()
