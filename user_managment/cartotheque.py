import user


class Cartotheque:
    def __init__(self, data_base_des_users):
        self.data_base_des_users = data_base_des_users

    def plus_user(self, user: user.User):
        list_des_telephones = []
        list_des_email = []
        for element in self.data_base_des_users:
            for v in element.values():
                list_des_telephones.append(v.telephone)
                list_des_email.append(v.e_mail)

        if user.telephone in list_des_telephones or \
                user.e_mail in list_des_email:
            print('Пользователь с таким номером телефона или e-mail '
                  'уже зарегистрирован!')
        else:
            if len(self.data_base_des_users) == 0:
                user_id = 1
            else:
                list_des_id = []
                for element in self.data_base_des_users:
                    for k in element.keys():
                        list_des_id.append(k)
                user_id = int(list_des_id[-1]) + 1
            self.data_base_des_users.append({str(user_id): user})
            print('Пользователь успешно добавлен!')

    def ajouter_status_user(self, info_input, change_code):
        list_des_telephones = []
        list_des_email = []
        list_des_id = []
        for element in self.data_base_des_users:
            for k, v in element.items():
                list_des_telephones.append(v.telephone)
                list_des_email.append(v.e_mail)
                list_des_id.append(k)

        if '@' in info_input:
            if info_input not in list_des_email:
                print('Пользователь с таким e-mail не найден!')
            else:
                for element in list_des_email:
                    if element == info_input:
                        temp_user_id = list_des_email.index(element)
                        if change_code == 0:
                            self.data_base_des_users[temp_user_id][
                                f'{temp_user_id + 1}'].status = 0
                            print('Аккаунт успешно деактивирован!')
                        elif change_code == 1:
                            self.data_base_des_users[temp_user_id][
                                f'{temp_user_id + 1}'].status = 1
                            print('Аккаунт успешно активирован!')
        elif '+38' in info_input:
            if info_input not in list_des_telephones:
                print('Пользователь с таким телефоном не найден!')
            else:
                for element in list_des_telephones:
                    if element == info_input:
                        temp_user_id = list_des_telephones.index(element)
                        if change_code == 0:
                            self.data_base_des_users[temp_user_id][
                                f'{temp_user_id + 1}'].status = 0
                            print('Аккаунт успешно деактивирован!')
                        elif change_code == 1:
                            self.data_base_des_users[temp_user_id][
                                f'{temp_user_id + 1}'].status = 1
                            print('Аккаунт успешно активирован!')
        elif info_input.isdigit():
            if info_input not in list_des_id:
                print('Пользователь с таким id не найден!')
            else:
                for element in list_des_id:
                    if element == info_input:
                        temp_user_id = list_des_id.index(element)
                        if change_code == 0:
                            self.data_base_des_users[temp_user_id][
                                f'{temp_user_id + 1}'].status = 0
                            print('Аккаунт успешно деактивирован!')
                        elif change_code == 1:
                            self.data_base_des_users[temp_user_id][
                                f'{temp_user_id + 1}'].status = 1
                            print('Аккаунт успешно активирован!')
        else:
            print('По заданному запросу информация не найдена!')

    def get_all_users(self):
        if len(self.data_base_des_users) != 0:
            print('\n____________В системе зарегистрированы:____________\n')
            for element in self.data_base_des_users:
                for k, v in element.items():
                    print(f'ID: {k}\n{str(v)}\n')
            print('___________________________________________________')
        else:
            print('Картотека пуста!')
