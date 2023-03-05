"""
    This module is use to confirm the response data
    So, to build the `Car class` in the `scraper.py` file. 
"""

# with open('car_links.txt', 'r') as f:
#     data = set([x.split('/')[1] for x in f.readlines()])

# with open('links.txt', 'w') as f:
#     for i in data:
#         f.write(f'{i}\n')

# print(data)

# Just for testing

import re

from bs4 import BeautifulSoup
import requests

response = requests.get('https://jiji.ng/alimosho/cars/toyota-rav4-2007-red-tVYF554WsKPb8bJGE817A6iC.html')

soup = BeautifulSoup(response.content, 'html.parser')

class_selector = 'h-mr-2 h-mv-1 qa-region-icon icon sprite-icons'
location = soup.find('svg', {'class': class_selector})

print(location)

# print(location.next_sibling.strip())