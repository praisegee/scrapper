import random as rd

import requests
from bs4 import BeautifulSoup

base_domain = 'https://jiji.ng'



def filter_car_link():
    """
    A function to get all the page links.
    Run this script as many as you can, to get more car detail pages.

    TIP: You can make it a recursive function and run it on a powerful machine
         like `colab.research.google.com` Project Jupyter to save time.
    """
    # response = requests.get(f'{base_domain}/cars')
    with open('./docs/links.txt', 'r') as f:
        list_link = set([link.strip() for link in f.readlines()])
        print("Links: ", len(list_link))
        # print("Links unique: ", len(list(set(list_link))))
    # response = requests.get(f'{base_domain}/isiala-ngwa/cars')
    location = rd.choice(list(list_link))
    print("Location: ", location)
    response = requests.get(f'{base_domain}/{location}/cars')
    # response = requests.get(f'{base_domain}/cars')

    soup = BeautifulSoup(response.content, 'html.parser')
    car_list = soup.find_all('div', {'class': 'masonry-item'})

    try:
        with open('./docs/car_links.txt', 'r') as fo:
            links = [x.strip() for x in fo.readlines()]
            print(links)
            print(len(links))
            print()
    except FileNotFoundError:
        links = []
        print('file not find')
        print('Re run')


    for car in car_list:
        car_link = car.find('a').attrs['href']
        if car_link not in links:
            links.append(car_link)

    # print(len(car_list))

    with open('./docs/car_links.txt', 'w') as f:
        for link in links:
            f.write(f'{link}\n')

    filter_car_link() # to make it recursive

filter_car_link()