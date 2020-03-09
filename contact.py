class Contact:
    def __init__(self, first_name, last_name, phone_number, favourites=False, *args, **kwargs):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.favourites = favourites
        self.additional_info = kwargs
        self.additional_phone = list(args)[:-1]

    def __str__(self):
        divider = '\n'
        tab = '\t'
        main = (f'\n  Имя: {self.first_name}'
                f'\n  Фамилия: {self.last_name}'
                f'\n  Телефон: {self.phone_number}'
                f'\n  В избранных: {"да" if self.favourites else "нет"}')
        if len(self.additional_phone):
            additional_num = f'\n  Дополнительные номера:\n{divider.join([f"{tab} {phone}" for phone in self.additional_phone])}'
        else:
            additional_num = ''
        if len(self.additional_info):
            additional_info = f'\n  Дополнительная информация:\n{divider.join([f"{tab} {key}: {value}" for key, value in self.additional_info.items()])}'
        else:
            additional_info = ''
        fin = '\n\n\t --- \n'
        result = main + additional_num + additional_info + fin
        return result
