import market_get_product
import market_get_user
import password_generator


class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.list_des_users = market_get_user.users_de_data_base()
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
        self.list_des_products = market_get_product.products_de_data_base()

    def catalogue(self):
        print('Список товаров:\n')
        for element in self.list_des_products:
            print(f'{self.list_des_products.index(element) + 1} - '
                  f'{element[0]}   {element[1]} грн/кг')

    def get_users_all(self):
        print('Список зарегистрированных пользователей:\n')
        for element in self.list_des_users:
            print(f'{self.list_des_users.index(element) + 1} - '
                  f'login: {element[0]}   password: {element[1]}')

    def plus_basket(self):
        user_input_1 = input('Для добавления в корзину, введите цифровой код '
                             'товара через запятую\nВыберите товары которые '
                             'нужно оформить: ')
        for i in user_input_1.split(','):
            if i in [str(j) for j in range(1, len(self.list_des_products) + 1)
                     ]:
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

user_login = input('Введите Ваш логин: ')
user_password = input('Введите пароль: ')
user_password = password_generator.generator_de_password(user_password)
current_user = Products(user_login, user_password)

if current_user.autorization():
    while True:
        print('Основное меню\n'
              '____________________________________\n'
              '1 - посмотреть каталог\n'
              '2 - добавить товар в корзину\n'
              '3 - посмотреть историю заказов\n'
              '9 - посмотреть список пользователей\n'
              '0 - выход\n'
              '____________________________________\n')
        user_input_main = input('Введите цифровую команду: ')

        if user_input_main == '1':
            current_user.catalogue()
        elif user_input_main == '2':
            current_user.plus_basket()
        elif user_input_main == '3':
            current_user.history_de_user()
        elif user_input_main == '9':
            current_user.get_users_all()
        elif user_input_main == '0':
            input('Для выхода нажмите Enter...')
            break
