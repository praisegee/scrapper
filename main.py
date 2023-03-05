import pandas as pd

from scraper.car_scraper import Car


def main(base_domain):
    # read the link path to each car page
    with open('docs/car_links.txt') as f:
        links = [link.strip() for link in f.readlines()]

    # data = Car(f'{base_domain}{files[10]}')

    # initial dataframe
    df1 = pd.DataFrame()

    # get the index number of the link for the last execution
    with open('docs/where.txt', 'r') as f:
        count = int(f.read().strip())

    # count = 153

    # the magic iteration starts here
    for link in links[count:]:
        car = Car(f'{base_domain}{link}')

        # prevent code brake if the soup object turns out to be None
        if not car.name:
            continue
        
        # let's define our features
        gen_data = {
            'Name': [car.name],
            'Price': [car.price],
            'Market price': [car.market_price],
            'Location': [car.location],
            'Thumbnail': [car.thumbnail],
            'Images': [car.images],
            'Gear': [car.gear],
            'Odometer': [car.odometer],
            'Fuel type': [car.fuel_type],
            'Car condition': [car.car_condition],
            'Other features': [car.other_features],
            'Dealer name': [car.dealer],
            'Page link': [car.page_link]
        }

        df = pd.DataFrame(gen_data)

        for k, v in car.dict_property.items():
                df[k] = v

        df1 = pd.concat([df1, df], ignore_index=True)

        print(car.name)
        count += 1
        # write to file after getting 10 more data
        # for backup, incase the code crash at runtime
        if count % 10 == 0:
            df1.to_csv('dataset/car_scrape.csv', index=False)
            # let's keep track of where we stop
            # or where the code get interrupted
            with open('docs/where.txt', 'w') as f:
                base = count - count % 10
                f.write(str(base))

        # log the count
        print(count)


    print(df1)



if __name__ == '__main__':
     main('https://jiji.ng')