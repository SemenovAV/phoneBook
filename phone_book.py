from contact import Contact


class PhoneBook:
    def __init__(self, book_title):
        self.title = book_title
        self.book = set()

    def view_contacts(self):
        for contact in self.book:
            print(contact)

    def add_contact(self, contact):
        if isinstance(contact, Contact):
            self.book.add(contact)

    def del_contact(self, number):
        self.book.remove(filter(lambda x: x['phone_number'] == number, self.book))

    def search_favourites(self):
        return filter(lambda x: x['favourites'], self.book)

    def search_for_name(self, first_name, last_name):
        return filter(lambda x: x['first_name'] == first_name and x['last_name'] == last_name, self.book)
