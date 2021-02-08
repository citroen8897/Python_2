class User:
    def __init__(self, user_name, user_password):
        self.list_users = [['Иван', '1234'], ['Владимир', '0000'],
                           ['Василий', '9876']]
        self.list_assortiment = [['яблоки', 30], ['груши', 45], ['арбузы', 20]]
        self.history_des_achetes = []
        self.basket = []
        self.user_name = user_name.title()
        self.user_password = user_password

    def autorization(self):
        if [self.user_name, self.user_password] in self.list_users:
            print('Вы успешно авторизовались в системе!')
        else:
            print('Пользователь с такими данными не найден!')


class Products(User):
    def add_basket(self):
        print('Список товаров:\n1 - яблоки\n2 - груши\n3 - арбузы\n')
        user_input_1 = input('Для добавления в корзину, введите цифровой код '
                             'товара через запятую\nВыберите товары которые '
                             'нужно оформить: ')
        for i in user_input_1.split(','):
            if i in ['1', '2', '3']:
                self.basket.append(self.list_assortiment[int(i) - 1])
            else:
                print('Неверный выбор!')
        if len(self.basket) != 0:
            print('Заказ оформлен!\nВаш заказ:')
            j = 1
            for element in self.basket:
                print(f'{j}. {element[0]}')
                j += 1
            self.history_des_achetes.append(self.basket.copy())
            self.basket.clear()

    def history(self):
        print(self.history_des_achetes)


current_user = Products(input('Введите Ваше имя: '),
                        input('Введите Ваш пароль: '))
current_user.autorization()
current_user.add_basket()
current_user.history()
