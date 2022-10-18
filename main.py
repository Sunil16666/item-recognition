#! /usr/bin/python3

import csv
import os
import pymongo as pymongo
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from scanning import scanning
from data_handling import data_handling

# START: INIT
client = pymongo.MongoClient("mongodb+srv://54o84mnf9k5g2DAC:54o84mnf9k5g2DAC@webscraper-ebay.k17drvn.mongodb.net/items?retryWrites=true&w=majority")
db = client.test
print(db)

ELEMENT_TO_SEARCH = input("enter element to search for: ")
chrome_options = Options()
# chrome_options.add_argument("--headless")
chrome_options.add_argument('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36')
URL_TO_SCAN = f"https://www.ebay-kleinanzeigen.de/s-muenster-%28westfalen%29/{ELEMENT_TO_SEARCH}/k0l929"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
# END: INIT


scanning()
data_handling()