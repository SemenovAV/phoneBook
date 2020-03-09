from app.contact import Contact


class PhoneBook:
    def __init__(self, book_title):
        self.title = book_title
        self.book = {}

    def view_contacts(self):
        contacts = f'{self.title}:'
        if len(self.book) > 0:
            for contact in self.book.values():
                contacts += contact.__str__()
        else:
            contacts += f'\n  Не найдено ни одного контакта!'
        return contacts

    def add_contact(self, first_name, last_name, phone_number, *args, favourites=False, **kwargs):
        self.book[phone_number] = Contact(first_name, last_name, phone_number, *args, favourites, **kwargs)

    def del_contact(self, number):
        self.book.pop(number, False)

    def get_favourites(self):
        result = 'В избранноми ни чего нет!'
        for contact in filter(lambda x: x.favourites, self.book.values()):
            result = 'Избранные контакты:\n'
            result += contact.__str__()
        return result

    def search_for_name(self, first_name, last_name):
        result = 'Контакт не найден'
        for contact in filter(lambda x: x.first_name == first_name and x.last_name == last_name, self.book.values()):
            result = 'Результат поиска:'
            result += contact.__str__()
        return result
