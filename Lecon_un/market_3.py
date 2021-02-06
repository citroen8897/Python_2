import datetime


class Market:
    def __init__(self):
        self.name = input('Ваше имя: ')
        self.assort = [['яблоки', 30], ['манго', 45], ['бананы', 15]]

    def main_method(self):
        print(f'Здраствуйте, {self.name}!\nНаши цены на сегодня:\n')

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
today = datetime.datetime.today()
if datetime.datetime.weekday(today) == 0:
    t_1.lundi()
elif datetime.datetime.weekday(today) in range(1, 4):
    t_1.mardi_jeudi()
else:
    t_1.vendredi_dimanche()
