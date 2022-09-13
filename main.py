from selenium import webdriver
from bs4 import BeautifulSoup
import re

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

    for a in soup.find_all('article', attrs={'class': 'aditem'}):
        price = a.find('p', attrs={'class': 'aditem-main--middle--price'})
        product = a.find('a', attrs={'class': 'ellipsis'})
        location = a.find('div', attrs={'class': 'aditem-main--top--left'})

        products.append(re.sub(r"\([^)]*\)", '', str(product.text).replace(" ", "")))
        prices.append(str(price.text).replace(" ", "").replace('\n', ''))
        locations.append(str(location.text).replace(" ", "").replace('\n', ''))

    print(products)
    print(prices)
    print(locations)
    driver.close()


scanning()