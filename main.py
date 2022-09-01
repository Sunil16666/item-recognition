import json

import requests
import os

URL_TO_SCAN = "https://www.ebay-kleinanzeigen.de/"


def scanning():
    response = requests.get('https://www.ebay-kleinanzeigen.de/')

    if not os.path.exists("content.txt"):
        open("content.txt", 'w+').close()

    filehandle = open("content.txt", 'r')
    previous_response_html = filehandle.read()
    filehandle.close()

    if previous_response_html == response.text:
        return False
    else:
        filehandle = open("previous_content.txt", 'w')
        filehandle.write(response.text)
        filehandle.close()
        return True
