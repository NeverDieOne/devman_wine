import datetime
from pprint import pprint


def get_age():
    time_founded = datetime.datetime(year=1920, month=1, day=1, hour=0)
    now = datetime.datetime.now()
    return (now - time_founded).days // 365


# def read_file(file):
#     wines_list = []
#     wines_dict = {}
#     wine = {}
#
#     with open(file, 'r') as wine_file:
#         wines = wine_file.read().split('\n')
#
#     for row in wines:
#         if '#' in row:
#             title = row.split('# ')[-1]
#             wines_dict['title'] = title
#             wines_dict['wines'] = []
#         if 'Название' in row:
#             wine['name'] = row.split(': ')[-1]
#         if 'Сорт' in row:
#             wine['sort'] = row.split(': ')[-1]
#         if 'Цена' in row:
#             wine['price'] = row.split(': ')[-1]
#         if 'Выгодное предложение' in row:
#             wine['predlog'] = True
#         if 'Картинка' in row:
#             wine['image'] = row.split(': ')[-1]
#             wines_dict['wines'].append(wine)
#             wine = {}
#
#             if len(wines_dict['wines']) == 3:
#                 wines_list.append(wines_dict)
#                 wines_dict = {}
#
#     return wines_list


def drink_parse(file):
    with open(file, 'r') as drink_file:
        drinks = drink_file.read().split('\n\n')

    drinks_list = []

    for row in drinks:
        if '#' in row:
            title = row.split('# ')[-1]

        if 'Название' in row:
            drink = row.split('\n')
            for line in drink:
                if 'Название' in line:
                    wine['name'] = line.split(': ')[-1]
                if 'Сорт' in line:
                    wine['sort'] = line.split(': ')[-1]
                if 'Цена' in line:
                    wine['price'] = line.split(': ')[-1]
                if 'Выгодное предложение' in line:
                    wine['predlog'] = True
                if 'Картинка' in line:
                    wine['image'] = line.split(': ')[-1]


    return drinks


if __name__ == '__main__':
    print(drink_parse('wine'))
