import csv


def csv_data_open():      # 1 - показать все
    with open('d:\Geek\Введение в Python\HomeWork\Seminars\DZ8\phone.csv', encoding='utf-8') as file:
        file_csv = csv.reader(file, delimiter=";")
        res = list(file_csv)
    return res


def add_info(list):  # 2 - добавление информации
    with open('d:\Geek\Введение в Python\HomeWork\Seminars\DZ8\phone.csv', 'a', encoding="utf8", newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(list)


def del_info(index):  # 3 - удаление информации
    list_csv = csv_data_open()
    del list_csv[index]
    with open('d:\Geek\Введение в Python\HomeWork\Seminars\DZ8\phone.csv', 'w', encoding="utf8", newline='') as file:
        writer = csv.writer(file, delimiter=';')
        for row in list_csv:
            writer.writerow(row)


def update_info(index, tel):  # 4 - изменить номер телефона
    list_csv = csv_data_open()
    list_csv[index][2] = tel
    with open('d:\Geek\Введение в Python\HomeWork\Seminars\DZ8\phone.csv', 'w', encoding="utf8", newline='') as file:
        writer = csv.writer(file, delimiter=';')
        for row in list_csv:
            writer.writerow(row)


def writing_csv():   # 5 - экспорт в новый файл
    with open('d:\Geek\Введение в Python\HomeWork\Seminars\DZ8\phone.csv', encoding="utf8") as file, open('new_phone.csv', 'w', encoding="utf8", newline='') as new_file:
        text = csv.reader(file)
        writer = csv.writer(new_file)
        for row in text:
            writer.writerow(row)


