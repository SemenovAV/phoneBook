from app.adv_print import adv_print
from app.phone_book import PhoneBook


def get_info(**kwargs):
    count = 0
    result = {}
    keys = [item for item in kwargs.keys()]
    title = kwargs['title']
    options = keys[1:]
    print(f'\n{title}:\n')
    while count < len(options):
        active_key = options[count]
        message = input(f'\t{kwargs[active_key]}: ').strip()
        if message == 'q':
            break
        elif message:
            count += 1
            result[active_key] = message
        else:
            print('Введите значение или ":q" для выхода')
    return result


add_contact_props = {
    'title': 'Создание контакта',
    'first_name': 'Имя',
    'last_name': 'Фамилия',
    'phone_number': 'Основной телефонный номер',
    'favourites': 'Добавить в избранное (Y/N)',
    'additional_info': 'Дополнительная информация (в формате: " ключ: значение; ключ 2: значение 2;" или "N" чтобы пропустить поле)',
    'additional_number': 'Дополнительные номера',
}
del_contact_props = {
    'title': 'Удаление контакта',
    'number': 'Основной номер контакта',
}
search_for_name_props = {
    'title': 'Поиск контакта',
    'first_name': 'Имя',
    'last_name': 'Фамилия'
}
commands = {
    'H': lambda: print('"q" - выход\n'
                       '"n" - новый контакт\n'
                       '"f" - показать избранные контакты\n'
                       '"s" - поиск по имени\n')

}


def frontend(title):
    book = PhoneBook(title)
    adv_print(book.view_contacts())

    while True:
        command = get_info(title='', command='Введите команду или "H" для помощи')
        commands[command['command']]()


if __name__ == '__main__':
    frontend('MyPhoneBook')
