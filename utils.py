import datetime
from pprint import pprint


def get_age():
    time_founded = datetime.datetime(year=1920, month=1, day=1, hour=0)
    now = datetime.datetime.now()
    return (now - time_founded).days // 365


def parse_drink(file):
    with open(file, 'r') as drink_file:
        data = drink_file.read().split('\n\n\n')

    drinks = []
    category = {}
    drink = {}

    for row in data:
        if '#' in row:
            category['name'] = row.split('# ')[-1]
            category['drinks'] = []

        if 'Название' in row:
            drinks_data = row.split('\n\n')

            for drink_data in drinks_data:
                _row = drink_data.split('\n')
                for line in _row:
                    if 'Название' in line:
                        drink['name'] = line.split(': ')[-1]
                    if 'Сорт' in line:
                        drink['sort'] = line.split(': ')[-1]
                    if 'Цена' in line:
                        drink['price'] = line.split(': ')[-1]
                    if 'Выгодное предложение' in line:
                        drink['good_offer'] = True
                    if 'Картинка' in line:
                        drink['image'] = line.split(': ')[-1]

                category['drinks'].append(drink)
                drink = {}

            drinks.append(category)
            category = {}

    return drinks


if __name__ == '__main__':
    pprint(parse_drink('wine'))
