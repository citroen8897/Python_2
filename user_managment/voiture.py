import re


class Voiture:
    def __init__(self, marka, model, numero, probeg, status):
        self.marka = marka
        while not self.marka.isalpha():
            self.marka = (input('Введите марку автомобиля: ')).title()

        self.model = model
        while re.findall(r'[^a-zA-Zа-яА-Я0-9, \s]', self.model):
            self.model = input('Введите модель автомобиля: ')

        self.numero = numero
        while not re.search(r'[a-zA-Z]{2}\d{4}[a-zA-Z]{2}', self.numero):
            self.numero = input('Введите гос. номер автомобиля: ')

        self.probeg = probeg
        while not self.probeg.isdigit():
            self.probeg = input('Введите пробег автомобиля: ')

        self.status = status

    def __str__(self):
        if self.status == 0:
            voiture_status = 'автомобиль у пользователя'
        elif self.status == 1:
            voiture_status = 'автомобиль доступен к выдаче'
        return f'Марка: {self.marka}\nМодель: {self.model}\n' \
               f'Гос. номер: {self.numero}\nТекущий пробег: {self.probeg}\n' \
               f'Статус: {voiture_status}'

    def faire_dict(self):
        return {'marka': self.marka,
                'model': self.model,
                'numero': self.numero,
                'probeg': self.probeg,
                'status': self.status}

    @classmethod
    def faire_object_voiture(cls, dict_data: dict):
        return cls(
            dict_data['marka'],
            dict_data['model'],
            dict_data['numero'],
            dict_data['probeg'],
            dict_data['status']
        )
