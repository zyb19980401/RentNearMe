from bs4 import BeautifulSoup
import requests
from requests import get

headers = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})

sapo = "https://condos.ca/toronto/condos-for-sale"
response = get(sapo, headers=headers)
print(response)
print(response.text[:1000])
