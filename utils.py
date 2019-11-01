import datetime
from pprint import pprint


def get_age():
    time_founded = datetime.datetime(year=1920, month=1, day=1, hour=0)
    now = datetime.datetime.now()
    return (now - time_founded).days // 365


def drink_parse(file):
    with open(file, 'r') as drink_file:
        drinks = drink_file.read().split('\n\n')

    drinks_list = []
    drinks_dict = {}
    one_drink = {}

    for row in drinks:
        if '#' in row:
            drinks_dict['title'] = row.split('# ')[-1]
            drinks_dict['drinks'] = []

        if 'Название' in row:
            drink = row.split('\n')
            for line in drink:
                if 'Название' in line:
                    one_drink['name'] = line.split(': ')[-1]
                if 'Сорт' in line:
                    one_drink['sort'] = line.split(': ')[-1]
                if 'Цена' in line:
                    one_drink['price'] = line.split(': ')[-1]
                if 'Выгодное предложение' in line:
                    one_drink['good_offer'] = True
                if 'Картинка' in line:
                    one_drink['image'] = line.split(': ')[-1]

            drinks_dict['drinks'].append(one_drink)
            one_drink = {}

        if len(drinks_dict['drinks']) == 3:
            drinks_list.append(drinks_dict)
            drinks_dict = {}

    return drinks_list


if __name__ == '__main__':
    pprint(drink_parse('wine'))
