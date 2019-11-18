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


def parse_drinks_data(data):
    chunks = data.split('\n\n\n')
    drinks = []

    for chunk in chunks:
        if '#' in chunk:
            category = {
                'name': chunk.split('# ')[-1],
                'drinks': []
            }

        if 'Название' in chunk:
            drinks_data = chunk.split('\n\n')

            parsed_drinks = [parse_drink(drink) for drink in drinks_data]
            category['drinks'].extend(parsed_drinks)

            drinks.append(category)
            category = {}

    return drinks


if __name__ == '__main__':
    pprint(parse_drinks_data('wine'))
