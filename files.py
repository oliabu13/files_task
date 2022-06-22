import os
from pprint import pprint

# Задание 1
def book_reader(file_name):
    with open(file_name, encoding='utf-8') as book:
        final_book = {}
        for dish in book:
            dish = dish.strip()
            ingredients_count = int(book.readline().strip())
            dish_dict = []
            for item in range(ingredients_count):
                ingredient_name, quantity, measure = book.readline().strip().split('|')
                dish_dict.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
            final_book[dish] = dish_dict
            book.readline()

# Задание 2

def shop_list_by_dishes(dishes, person_count, cook_book):
    result = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                if ingredient['ingredient_name'] in result:
                    result[ingredient['ingredient_name']]['quantity'] += ingredient['quantity'] * person_count
                else:
                    result[ingredient['ingredient_name']] = {'measure': ingredient['measure'],
                                                          'quantity': (ingredient['quantity'] * person_count)}
        else:
            print(f'Блюда "{dish}" нет в книге рецептов')
            pass
    return result

#Задание 3
def line_count(*files):
    texts_dict = {}
    for file in files:
        with open(file, encoding='utf-8') as file_obj:
            lines = len(file_obj.readlines())
            texts_dict.setdefault(file, lines)
    sorted_text_keys = sorted(texts_dict, key=texts_dict.get)
    sorted_text_dict = {}
    for s in sorted_text_keys:
        sorted_text_dict[s] = texts_dict[s]
    return sorted_text_dict

def merge_files(dictionary):
    base_path = os.getcwd()
    text_name = 'res_file.txt'

    full_path = os.path.join(base_path, text_name)
    text = {}
    for key, value in dictionary.items():
        with open(key, encoding='utf-8') as file_obj:
            text.setdefault(key, file_obj.read().strip())

    with open(full_path, 'a', encoding='utf-8') as new_file:
        for k, v in text.items():
            new_file.write(f'{k}\n')
            new_file.write(f'{str(dictionary[k])}\n')
            new_file.write(f'{v}\n')


texts = line_count('1.txt', '2.txt', '3.txt')
merge_files(texts)