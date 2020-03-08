class Contact:
    def __init__(self, first_name, last_name, phone_number, *args, favourites=False, **kwargs):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.favourites = favourites
        self.additional_info = kwargs
        self.additional_phone = args

    def __str__(self):
        divider = '\n'
        tab = '\t'
        return (f'Имя: {self.first_name}\n'
                f'Фамилия: {self.last_name}\n'
                f'Телефон: {self.phone_number}\n'
                f'Дополнительные номера:\n{divider.join([f"{tab} {phone}" for phone in self.additional_phone])}\n'
                f'В избранных: {"да" if self.favourites else "нет"}\n'
                f'Дополнительная информация:\n{divider.join([f"{tab} {key}: {value}" for key, value in self.additional_info.items()])}')
