def show_menu():
    print('1 - показать все')
    print('2 - добавить запись')
    print('3 - удалить запись')
    print('4 - изменить телефон')
    print('5 - экспортировать в новый файл')
    return int(input('Введите цифру: '))


def show_res(res):
    for i, row in enumerate(res):
        print(i, ' '.join(row))


def add_info():
    print('Введите фамилию, имя, телефон и комментарий через пробел: ')
    in_info = input().split()
    return in_info


def delete():
    print('Введите индекс для удаления')
    return int(input())


def change_tel():
    print('Введите индекс для изменения')
    print('Введите новый телефон')
    return int(input()), input()

def writing_csv():
    print('Новый файл создан с именем new_phone.csv')

