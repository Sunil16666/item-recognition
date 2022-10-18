from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import csv
from main import driver, URL_TO_SCAN


def scanning():
    products = []
    locations = []
    prices = []

    driver.get(URL_TO_SCAN)

    content = driver.page_source

    soup = BeautifulSoup(content, 'html.parser')
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID, 'gdpr-banner-accept'))).click()

    def get_elements():
        try:
            WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME, 'aditem')))
        except TimeoutException:
            pass

        for a in soup.find_all('article', attrs={'class': 'aditem'}):

            price = a.find('p', attrs={'class': 'aditem-main--middle--price' and 'aditem-main--middle--price-shipping--price'})
            name = a.find('a', attrs={'class': 'ellipsis'})
            location = a.find('div', attrs={'class': 'aditem-main--top--left'})

            products.append(str(name.text).strip())

            if len(driver.find_elements(By.CSS_SELECTOR, '#srchrslt-adtable > li:nth-child(1) > article > div.aditem-main > div.aditem-main--middle > div.aditem-main--middle--price-shipping > p')) != 0:
                prices.append(str(price.text).strip())
            else:
                prices.append('n/a')

            locations.append(str(location.text).strip())

            try:
                if driver.find_elements(By.CLASS_NAME, 'pagination-next'):
                    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.CLASS_NAME, 'pagination-next'))).click()
                else:
                    pass
            except NoSuchElementException:
                pass
    get_elements()
    while driver.find_elements(By.CLASS_NAME, 'pagination-next'):
        get_elements()
    else:
        driver.close()
    print(products)
    print(prices)
    print(locations)

    with open('items.csv', 'w', newline='') as item_storing:
        writer = csv.writer(item_storing, quoting=csv.QUOTE_ALL)
        writer.writerow(products)
        writer.writerow(prices)
        writer.writerow(locations)

    'make proper sorting based on the price'
    # numpy.sort(products, axis=-1, kind='quicksort')

