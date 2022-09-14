from selenium import webdriver
from bs4 import BeautifulSoup
import re
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
URL_TO_SCAN = "https://www.ebay-kleinanzeigen.de/s-muenster-%28westfalen%29/laptop/k0l929"
driver = webdriver.Chrome(executable_path='/Users/linushenn/Desktop/Chromedriver/chromedriver', options=chrome_options)


def interceptor(request):
    request.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, ' \
                                    'like Gecko) Chrome/105.0.0.0 Safari/537.36 '


driver.request_interceptor = interceptor


def scanning():

    products = []
    locations = []
    prices = []

    driver.get(URL_TO_SCAN)

    content = driver.page_source

    soup = BeautifulSoup(content, 'html.parser')

    driver.find_element(By.ID, 'gdpr-banner-accept').click()
    sleep(2)

    for i in range(2):
        for a in soup.find_all('article', attrs={'class': 'aditem'}):
            price = a.find('p', attrs={'class': 'aditem-main--middle--price'})
            product = a.find('a', attrs={'class': 'ellipsis'})
            location = a.find('div', attrs={'class': 'aditem-main--top--left'})

            products.append(re.sub(r"\([^)]*\)", '', str(product.text).replace(" ", "")))
            prices.append(str(price.text).replace(" ", "").replace('\n', ''))
            locations.append(str(location.text).replace(" ", "").replace('\n', ''))

        driver.find_element(By.CLASS_NAME, 'pagination-next').click()
        sleep(2)

    print(products)
    print(prices)
    print(locations)
    driver.close()


scanning()
