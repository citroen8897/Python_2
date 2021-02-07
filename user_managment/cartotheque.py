import user


class Cartotheque:
    def __init__(self, data_base_des_users):
        self.data_base_des_users = data_base_des_users

    def plus_user(self, user: user.User):
        list_des_telephones = []
        for element in self.data_base_des_users:
            for v in element.values():
                list_des_telephones.append(v.telephone)

        list_des_email = []
        for element in self.data_base_des_users:
            for v in element.values():
                list_des_email.append(v.e_mail)

        if user.telephone in list_des_telephones or \
                user.e_mail in list_des_email:
            print('Пользователь с таким номером телефона или e-mail '
                  'уже зарегистрирован!')
        else:
            self.data_base_des_users.append(
                {len(self.data_base_des_users) + 1: user})
            print('Пользователь успешно добавлен!')

    def get_all_users(self):
        print('\n____________В системе зарегистрированы:____________\n')
        for element in self.data_base_des_users:
            for k, v in element.items():
                print(f'ID: {k}\n{str(v)}\n')
        print('___________________________________________________')
