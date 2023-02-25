# Replying to "def new_record(book)..."

# Задача №49. Решение в группах
# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной

# Обязательное ДЗ - доделать телефонный справочник с внешним хранилищем информации, дополнить функционалом добавления информации, удаления и редактирования.
# Необязательное ДЗ - сделать как тг-бот , может подключить БД SQLITE3. Грамотно надо оформить ридми к вашему проекту.

import json

db_path = 'phone_book.json'
welcome = 'Enter command: 1 - read & show | 2 - add record | 3 - search | 4 - init DB | 5 - delete | q - Quit\n'

db_file_name = ''
db = []
global_id = 0

phone_book = {}


def print_book(book):
    for k, v in book.items():
        print(k, " - ", end=" | ")
        for i, j in v.items():
            print(i, j, end=" | ")
        print()


def save_db(path, db):
    with open(path, 'w', encoding='utf-8') as fh:  # открываем файл на запись
        # преобразовываем словарь data в unicode-строку и записываем в файл
        fh.write(json.dumps(db, ensure_ascii=False))
        print('БД успещно сохранена')


def load_db(path):
    # загрузить из json
    with open(path, 'r', encoding='utf-8') as fh:  # открываем файл на чтение
        BD_local = json.load(fh)  # загружаем из файла данные в словарь data
    print('БД успещно загружена')
    return BD_local


def new_record(book):
    k = input("Put new name: ")
    a = {}
    a['phone'] = list(input('put phone: ').split())
    a['birthday'] = input('put birthday: ')
    book[k] = a


def search_db(book):
    result = []
    for k,v in book.items():
        if book[k] == book:
            print(book[k])
        return result


def delete(id=''):
    global global_id
    global db
    global db_file_name
    if (id == ''):
        print('specify id for delete')
        return

    for row in db:
        if (row[0] == id):
            db.remove(row)
            break

    # with open(db_file_name, 'w', newline='') as csv_file:
    #     writer = csv.writer(csv_file, delimiter=',',
    #                         quotechar='\'', quoting=csv.QUOTE_MINIMAL)
    #     for row in db:
    #         writer.writerow(row)


def init_db(path, db):
    with open(path, 'w', encoding='utf-8') as fh:  # открываем файл на запись
        # преобразовываем словарь data в unicode-строку и записываем в файл
        fh.write(json.dumps(db, ensure_ascii=False))
        print('БД успещно сохранена')


try:
    phone_book = load_db(db_path)
except:
    phone_book = {
        'Миша гараж': {'phone': ['72443351195', '72627397543'], 'birthday': '11-02-2010', 'email': "mail@mail.ru"},
        'Sasha': {'phone': ['78436840045', '77554802591']}}
    print('Базу данных не найдена, создаём тестовую БД')


def action():
    action = None
    while action != 'q':
        action = input(f'({welcome}').lower()
        if action == '1':
            print(phone_book)
        elif action == '2':
            # print(action, ' -> ', db_path)
            new_record(phone_book)
        elif action == '3':
            search_db(input('Put the name: '))
        elif action == '4':
            init_db(db_path, phone_book)
        elif action == '5':
            delete()
            print('1. Найти номер по фамилии.')
            print('2. Найти номер по имени.')
            print('3. Поиск по номеру телефона.')
            deleting = (input('Введите номер пункта: '))

            if deleting == 1:
                search = input('Введите фамилию: ')
                user_id = input('Введите id записи: ')
            elif deleting == 2:
                search = input('Введите имя: ')
                user_id = input('Введите id записи: ')

            elif deleting == 3:
                search = input('Введите номер телефона: ')
                user_id = input('Введите id записи: ')
                new_number = input('Введите новый номер телефона: ')

            else:
                print(
                    '\nТакого пункта меню не существует.\nВведите цифру, соответствующую пункту меню.')


action()
save_db(db_path, phone_book)
