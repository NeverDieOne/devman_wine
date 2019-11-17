import datetime
from pprint import pprint


def get_age():
    year_founded = 1920
    current_year = datetime.datetime.now().year
    return current_year - year_founded


def parse_drink(drink_data):
    drink = {}

    part_wine_info = drink_data.split('\n')
    for line in part_wine_info:
        if 'Название' in line:
            drink['name'] = line.split(': ')[-1]
        if 'Сорт' in line and len(line.split(': ')) > 1:
            drink['sort'] = line.split(': ')[-1]
        if 'Цена' in line:
            drink['price'] = line.split(': ')[-1]
        if 'Выгодное предложение' in line:
            drink['good_offer'] = True
        if 'Картинка' in line:
            drink['image'] = line.split(': ')[-1]

    return drink


def read_file(file):
    with open(file, 'r') as drink_file:
        data = drink_file.read().split('\n\n\n')

    return data


def parse_drinks_data(file):
    data = read_file(file)

    drinks = []

    for chunk in data:
        if '#' in chunk:
            category = {
                'name': chunk.split('# ')[-1],
                'drinks': []
            }

        if 'Название' in chunk:
            drinks_data = chunk.split('\n\n')

            [category['drinks'].append(parse_drink(drink)) for drink in drinks_data]

            drinks.append(category)
            category = {}

    return drinks


if __name__ == '__main__':
    pprint(parse_drinks_data('wine'))
