import datetime


class Market:
    # def __init__(self):
    #     self.name = input('Ваше имя: ')
    #     self.assort = [['яблоки', 30], ['манго', 45], ['бананы', 15]]

    def main_method(self):
        print(f'Здраствуйте, {self.name}!\nНаши цены на сегодня:\n')
        today = datetime.datetime.today()
        if datetime.datetime.weekday(today) == 0:
            self.lundi()
        elif datetime.datetime.weekday(today) in range(1, 4):
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

    def test(self, *args):
        print(*args)

    def test_2(self, temp_2):
        print(temp_2 ** 3)


t_1 = Market()
t_1.name = 'Jerome'
t_1.assort = [['яблоки', 30], ['манго', 45], ['бананы', 15]]
t_1.main_method()

t_1.test('c"est le test...')
t_1.test_2(22)
