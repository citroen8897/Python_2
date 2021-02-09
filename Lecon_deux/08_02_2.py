class User:
    def __init__(self, name, password):
        self.name = name.title()
        self.password = password
        self.list_des_users = [['Иван', '1234'], ['Владимир', '0000'],
                               ['Василий', '9876']]
        self.basket = []
        self.history_des_achetes = []

    def autorization(self):
        if [self.name, self.password] in self.list_des_users:
            print('Вы успешно авторизовались в системе!')
            return True
        else:
            print('Пользователь с такими данными не найден!')
            return False

    def history_de_user(self):
        for element in self.history_des_achetes:
            print(element)


class Products(User):
    def __init__(self, name, password):
        User.__init__(self, name, password)
        self.list_des_products = [['яблоки', 30], ['груши', 45],
                                  ['арбузы', 20]]

    def catalogue(self):
        print(f'Список товаров:\n1 - {self.list_des_products[0][0]}\n'
              f'2 - {self.list_des_products[1][0]}\n'
              f'3 - {self.list_des_products[2][0]}\n')

    def plus_basket(self):
        user_input_1 = input('Для добавления в корзину, введите цифровой код '
                             'товара через запятую\nВыберите товары которые '
                             'нужно оформить: ')
        for i in user_input_1.split(','):
            if i in ['1', '2', '3']:
                self.basket.append(self.list_des_products[int(i) - 1])
            else:
                print('Неверный выбор!')
        self.get_basket()

        user_input_2 = input('Удалить товар из корзины?')
        if user_input_2 == 'Y':
            temp_list_basket = self.basket.copy()
            user_input_3 = input('Через запятую введите номера товаров для '
                                 'удаления: ')
            for j in user_input_3.split(','):
                self.basket.remove(temp_list_basket[int(j) - 1])

        self.get_basket()
        self.history_des_achetes.append(self.basket.copy())
        self.basket.clear()

    def get_basket(self):
        if len(self.basket) != 0:
            print('Заказ оформлен!\nВаш заказ:')
            j = 1
            for element in self.basket:
                print(f'{j}. {element[0]}')
                j += 1


print('Приветствуем Вас в нашем магазине!\nДля входа в магазин, пожалуйста '
      'авторизируйтесь...')
current_user = Products(input('Введите Ваше имя: '),
                        input('Введите Ваш пароль: '))

if current_user.autorization():
    while True:
        print('Основное меню\n'
              '____________________________________\n'
              '1 - посмотреть каталог\n'
              '2 - добавить товар в корзину\n'
              '3 - посмотреть историю заказов\n'
              '0 - выход\n'
              '____________________________________\n')
        user_input_main = input('Введите цифровую команду: ')

        if user_input_main == '1':
            current_user.catalogue()
        elif user_input_main == '2':
            current_user.plus_basket()
        elif user_input_main == '3':
            current_user.history_de_user()
        elif user_input_main == '0':
            input('Для выхода нажмите Enter...')
            break
