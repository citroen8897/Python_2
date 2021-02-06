class A:
    def __init__(self, name, years):
        self.name = name
        self.years = years
        print('Hello class A!')

    def test(self):
        print(f'Hello {self.name}\nYou are {self.years} years...')

    def test_2(self):
        self.name = input('Введите имя: ')
        self.years = input('Ваш возраст: ')
        self.test()

    def test_3(self):
        print(self.surname)


t_1 = A('Ivan', 25)
t_1.test()
t_1.test_2()
print(t_1.name)
t_1.name = 'Vasya'
print(t_1.name)
t_1.surname = 'Jackson'
print(t_1.surname)
t_1.test_3()
