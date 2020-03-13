class Contact:
    def __init__(self, first_name, last_name, phone_number, favourites=False, *args, **kwargs):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.favourites = favourites
        self.additional_info = kwargs.get('additional_info', None)
        self.additional_phone = kwargs.get('additional_num', None)

    def __str__(self):
        divider = '\n'
        tab = '\t'
        main = (f'\n  Имя: {self.first_name}'
                f'\n  Фамилия: {self.last_name}'
                f'\n  Телефон: {self.phone_number}'
                f'\n  В избранных: {"да" if self.favourites else "нет"}')
        if self.additional_phone and len(self.additional_phone) > 0:
            phones = [item for item in self.additional_phone.split(';')]
            additional_num = f'\n  Дополнительные номера:\n{divider.join([f"{tab} {phone}" for phone in phones])}'
        else:
            additional_num = ''
        if self.additional_info and len(self.additional_info) > 0:
            elem = [item.split(':') for item in self.additional_info.split(';')[:-1]]
            additional_info = f'\n  Дополнительная информация:\n{divider.join([f"{tab} {item[0]}: {item[1]}" for item in elem])}'
        else:
            additional_info = ''
        fin = '\n\n\t ---'
        result = main + additional_num + additional_info + fin
        return result
