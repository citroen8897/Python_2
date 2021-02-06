import datetime


class Market:
    def __init__(self):
        self.name = input('Ваше имя: ')
        self.assort = [['яблоки', 30], ['манго', 45], ['бананы', 15]]

    def main_method(self):
        print(f'Здраствуйте, {self.name}!\nНаши цены на сегодня:\n')
        today = datetime.datetime.today()
        if datetime.datetime.weekday(today) == 0:
            self.lundi()
        elif datetime.datetime.weekday(today) in (1, 3):
            self.mardi_jeudi()
        else:
            self.vendredi_dimanche()

    def lundi(self):
        for i in self.assort:
            print(f'Товар: {i[0]}\nЦена: {i[1] * 0.95}')

    def mardi_jeudi(self):
        for i in self.assort:
            print(f'Товар: {i[0]}\nЦена: {i[1] * 0.85}')

    def vendredi_dimanche(self):
        for i in self.assort:
            print(f'Товар: {i[0]}\nЦена: {i[1] * 0.75}')


t_1 = Market()
t_1.main_method()
