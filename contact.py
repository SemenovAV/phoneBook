class Contact:
    def __init__(self, first_name, last_name, phone_number, favourites=False, *args, **kwargs):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.favourites = favourites

    def __str__(self):
        return (f'Имя: {self.first_name}\n'
                f'Фамилия: {self.last_name}\n'
                f'Телефон: {self.phone_number}\n'
                f'В избранных: {"да" if self.favourites else "нет"}')


jhon = Contact('Jhon', 'Smith', '+71234567809')
print(jhon)
