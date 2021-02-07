import re


class User:
    def __init__(self, nom, prenom, telephone, e_mail):
        self.nom = nom
        while not self.nom.isalpha():
            self.nom = (input('Введите имя: ')).title()

        self.prenom = prenom
        while not self.prenom.isalpha():
            self.prenom = (input('Введите фамилию: ')).title()

        self.telephone = telephone
        while len(self.telephone) < 10:
            self.telephone = input('Введите телефон: ')
        for element in self.telephone:
            if not element.isdigit():
                self.telephone = self.telephone.replace(element, "")
        if not self.telephone.startswith("+38"):
            self.telephone = "+38" + self.telephone[-10:]

        self.e_mail = e_mail
        while not re.search(r"\w+\.*\w+@\w+\.\w+", self.e_mail):
            self.e_mail = input('Введите электронный адрес: ')

    def __str__(self):
        return f'Имя: {self.nom}\nФамилия: {self.prenom}\n' \
               f'Телефон: {self.telephone}\nE-mail: {self.e_mail}'

    def faire_dict(self):
        return {'nom': self.nom,
                'prenom': self.prenom,
                'telephone': self.telephone,
                'e_mail': self.e_mail}

    @classmethod
    def faire_object_user(cls, dict_data: dict):
        return cls(
            dict_data['nom'],
            dict_data['prenom'],
            dict_data['telephone'],
            dict_data['e_mail']
        )
