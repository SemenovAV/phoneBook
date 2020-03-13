from app.adv_print import adv_print
from app.phone_book import PhoneBook


def get_info(**kwargs):
    count = 0
    result = {}
    keys = [item for item in kwargs.keys()]
    title = kwargs['title']
    options = keys[1:]
    print(f'{title}:')
    while count < len(options):
        active_key = options[count]
        message = input(f'{kwargs[active_key]}: ').strip()
        if message == 'q':
            return {'command': 'q'}
        elif message:
            count += 1
            result[active_key] = message
        else:
            print('Введите значение или ":q" для выхода')

    return {key: value for key, value in filter(lambda a: a[1] and a[1] != 'N', result.items())}


add_contact_props = {
    'title': 'Создание контакта',
    'first_name': 'Имя',
    'last_name': 'Фамилия',
    'phone_number': 'Основной телефонный номер',
    'favourites': 'Добавить в избранное (Y/N)',
    'additional_info': 'Дополнительная информация (в формате: " ключ: значение; ключ 2: значение 2;" или "N" чтобы пропустить поле)',
    'additional_num': 'Дополнительные номера',
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


def frontend(title):
    book = PhoneBook(title)
    commands = {
        'h': lambda: adv_print('"q" - выход\n'
                               '"n" - новый контакт\n'
                               '"f" - показать избранные контакты\n'
                               '"s" - поиск по имени\n'),
        'n': lambda: book.add_contact(**get_info(**add_contact_props)),
        'd': lambda: book.del_contact(**get_info(**del_contact_props)),
        's': lambda: adv_print(book.search_for_name(**get_info(**search_for_name_props))),
        'v': lambda: adv_print(book.view_contacts()),

    }

    while True:
        command = get_info(title='', command='Введите команду или "h" для помощи или "q" для выхода.')
        if command['command'] == 'q':
            return
        commands.get(command['command'], lambda: adv_print('Нет такой команды'))()


if __name__ == '__main__':
    frontend('MyPhoneBook')
