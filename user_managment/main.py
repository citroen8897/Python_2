import user
import cartotheque
import os.path
import json

list_des_users = []
users_path = 'DB_des_users.json'
if os.path.exists(users_path):
    with open(users_path, 'r') as data_base_des_users:
        list_des_users = json.load(data_base_des_users)

for element in list_des_users:
    for k, v in element.items():
        element[k] = user.User.faire_object_user(v)

current_cartotheque = cartotheque.Cartotheque(list_des_users)

while True:
    user_input_1 = input('S.P.Q.R.\n1 - добавить пользователя\n'
                         '2 - открыть картотеку\n'
                         '0 - выход\n'
                         'Введите номер команды: ')

    if user_input_1 == '1':
        new_user = user.User('', '', '', '')
        current_cartotheque.plus_user(new_user)

    elif user_input_1 == '2':
        current_cartotheque.get_all_users()

    elif user_input_1 == '0':
        with open(users_path, 'w') as data_base_des_users:
            for element in list_des_users:
                for k, v in element.items():
                    element[k] = v.faire_dict()
            data_pour_ecrire = json.dumps(list_des_users, indent=4)
            data_base_des_users.write(data_pour_ecrire)
        input('Нажмите Enter для выхода...')
        break