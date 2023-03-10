import re

import requests
from bs4 import BeautifulSoup


class Car:
    """A model class to get all the attributes/features of a car."""

    def __init__(self, url) -> None:
        self.url = url
        content = requests.get(self.url).content
        self.soup = BeautifulSoup(content, 'html.parser')     

    def __repr__(self) -> str:
        return f'<CarParser {self.name}>'

    def __str__(self) -> str:
        return f'{self.name}'

    @property
    def name(self):
        class_selector = 'b-advert-title-inner qa-advert-title b-advert-title-inner--h1'
        name = self.soup.find('div', {'class': class_selector})
        if not name:
            return None
        return name.text.strip()

    @property
    def price(self):
        class_selector = 'qa-advert-price-view b-alt-advert-price__container'
        price_text = self.soup.find('div', {'class': class_selector})
        if not price_text:
            return ''
        price = re.findall("₦.[\d+,]+", price_text.text)[0]
        return price.strip()

    @property
    def market_price(self):
        class_selector = 'fw-button__slot-wrapper'
        market_price_finder = self.soup.find_all('span', {'class': class_selector})
        market_price_list = list(filter(lambda x: '₦' in x, [txt.text.strip() for txt in market_price_finder]))

        if len(list(market_price_list)) >= 1:
            market_price = market_price_list[0]
        else:
            market_price = ''
        try:
            price = re.findall("₦.[\d+\.\d+\s+\w\s+~]+", market_price)
            if len(price) >= 1:
                price = price[0]
            else:
                price = ''
        except AttributeError:
            price = ''

        return price

    @property
    def location(self):
        class_selector = 'h-mr-2 h-mv-1 qa-region-icon icon sprite-icons'
        location = self.soup.find('svg', {'class': class_selector})
        if not location:
            return ''
        return location.next_sibling.strip()

    @property
    def thumbnail(self):
        thumbnail = self.soup.find('img', {'class': 'b-slider-image qa-carousel-slide'})
        if not thumbnail:
            return ''
        return thumbnail.attrs['src'].strip()

    @property
    def images(self):
        images = self.soup.find_all('img', {'class': 'b-carousel-thumbnails--image qa-carousel-thumbnail__image'})
        if not images:
            return ''
        return " | ".join([image.attrs['src'].strip() for image in images])

    @property
    def dict_property(self):
        keys_selector = 'b-advert-attribute__key'
        values_selector = 'b-advert-attribute__value'

        keys = [key.text for key in self.soup.find_all('div', {'class': keys_selector})]
        values = [value.text for value in self.soup.find_all('div', {'class': values_selector})]
        
        properties = {key.strip(): value.strip().replace('\n', '') for key,value in zip(keys, values)}
        
        return properties

    @property
    def gear(self):
        gear = self.soup.find('span', {'itemprop': 'vehicleTransmission'})
        if not gear:
            return ''
        return gear.text.strip()
        
    @property
    def car_condition(self):
        condition = self.soup.find('span', {'itemprop': 'itemCondition'})
        if not condition:
            return ''
        return condition.text.strip()
    
    @property
    def odometer(self):
        odometer = self.soup.find('span', {'itemprop': 'mileageFromOdometer'})
        if not odometer:
            return ''
        return odometer.text.strip()
    
    @property
    def fuel_type(self):
        fuel_type = self.soup.find('span', {'itemprop': 'fuelType'})
        if not fuel_type:
            return ''
        return fuel_type.text.strip()

    @property
    def other_features(self):
        features = self.soup.find_all('div', {'class': 'b-advert-attributes__tag'})
        if not features:
            return ''
        return " | ".join([feature.text.strip() for feature in features])

    @property
    def dealer(self):
        dealer = self.soup.find('div', {'class': 'b-seller-block__name'})
        if not dealer:
            return ''
        return dealer.text.strip()
    
    @property
    def page_link(self):
        return self.url 

    # @property
    # def is_electric(self):
    #     pass

    # @property
    # def uses_petrol(self):
    #     pass

    # @property
    # def is_registered(self):
    #     pass

    # @property
    # def date_posted(self):
    #     pass
