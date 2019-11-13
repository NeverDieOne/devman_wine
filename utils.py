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
        if 'Сорт' in line:
            drink['sort'] = line.split(': ')[-1]
        if 'Цена' in line:
            drink['price'] = line.split(': ')[-1]
        if 'Выгодное предложение' in line:
            drink['good_offer'] = True
        if 'Картинка' in line:
            drink['image'] = line.split(': ')[-1]

    return drink


def parse_drinks_data(file):
    with open(file, 'r') as drink_file:
        data = drink_file.read().split('\n\n\n')

    drinks = []

    for row in data:
        if '#' in row:
            category = {
                'name': row.split('# ')[-1],
                'drinks': []
            }

        if 'Название' in row:
            drinks_data = row.split('\n\n')

            for drink_data in drinks_data:
                # Из за добавления функции исчезла вложенность if'ов и for'ов
                drink = parse_drink(drink_data)
                category['drinks'].append(drink)

            drinks.append(category)
            category = {}

    return drinks


if __name__ == '__main__':
    pprint(parse_drinks_data('wine'))
