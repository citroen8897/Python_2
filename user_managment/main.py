import user
import cartotheque
import voiture
import os.path
import json

list_des_users = []
users_path = 'DB_des_users.json'
if os.path.exists(users_path):
    with open(users_path, 'r') as data_base_des_users:
        list_des_users = json.load(data_base_des_users)

list_des_voitures = []
voitures_path = 'DB_des_voitures.json'
if os.path.exists(voitures_path):
    with open(voitures_path, 'r') as data_base_des_voitures:
        list_des_voitures = json.load(data_base_des_voitures)

for element in list_des_users:
    for k, v in element.items():
        element[k] = user.User.faire_object_user(v)

for element in list_des_voitures:
    for k, v in element.items():
        element[k] = voiture.Voiture.faire_object_voiture(v)

current_cartotheque = cartotheque.Cartotheque(list_des_users,
                                              list_des_voitures)

while True:
    user_input_1 = input('S.P.Q.R.\n'
                         '______________________________\n'
                         '1 - добавить пользователя\n'
                         '2 - открыть картотеку пользователей\n'
                         '3 - деактивировать пользователя\n'
                         '4 - активировать пользователя\n'
                         '5 - добавить автомобиль\n'
                         '6 - открыть картотеку автомобилей\n'
                         '7 - выдать автомобиль пользователю\n'
                         '8 - принять автомобиль у пользователя\n'
                         '0 - выход\n'
                         '______________________________\n'
                         'Ваш выбор: ')

    if user_input_1 == '1':
        new_user = user.User('', '', '', '', 1)
        current_cartotheque.plus_user(new_user)

    elif user_input_1 == '2':
        current_cartotheque.get_all_users()

    elif user_input_1 == '3':
        current_cartotheque.ajouter_status_user(
            input('Введите номер телефона(в формате +380ххххххххх) или e-mail '
                  'или id пользователя: '), 0)

    elif user_input_1 == '4':
        current_cartotheque.ajouter_status_user(
            input('Введите номер телефона(в формате +380ххххххххх) или e-mail '
                  'или id пользователя: '), 1)

    elif user_input_1 == '5':
        new_voiture = voiture.Voiture('', '#', '', '', 1)
        current_cartotheque.plus_voiture(new_voiture)

    elif user_input_1 == '6':
        current_cartotheque.get_all_voitures()

    elif user_input_1 == '0':
        with open(users_path, 'w') as data_base_des_users:
            for element in list_des_users:
                for k, v in element.items():
                    element[k] = v.faire_dict()
            data_pour_ecrire = json.dumps(list_des_users, indent=4)
            data_base_des_users.write(data_pour_ecrire)

        with open(voitures_path, 'w') as data_base_des_voitures:
            for element in list_des_voitures:
                for k, v in element.items():
                    element[k] = v.faire_dict()
            data_pour_ecrire_2 = json.dumps(list_des_voitures, indent=4)
            data_base_des_voitures.write(data_pour_ecrire_2)

        input('Нажмите Enter для выхода...')
        break
