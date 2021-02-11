import mysql.connector
from mysql.connector import Error

user_login = input('Введите логин: ')
user_password = input('Введите пароль: ')
user_nom = input('Введите имя: ')
user_prenom = input('Введите фамилию: ')
user_bth_jour = int(input('Введите день рождения: '))
user_bth_mois = int(input('Введите месяц рождения: '))
user_bth_an = int(input('Введите год рождения: '))
user_status = 'user'

try:
    conn = mysql.connector.connect(user='root',
                                   host='localhost',
                                   database='mysql')

    if conn.is_connected():
        print('Соединение с базой данных пользователей установлено....')
        new_user = "INSERT INTO market_10_02(login, password, nom, prenom, " \
                   "bth_jour, bth_mois, bth_an, status) " \
                   "VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor = conn.cursor()
        cursor.execute(new_user,
                       (user_login, user_password, user_nom, user_prenom,
                        user_bth_jour, user_bth_mois, user_bth_an, user_status)
                       )

        if cursor.lastrowid:
            print('успешно добавлена запись. id - >', cursor.lastrowid)
        else:
            print('какая-то ошибка...')

        conn.commit()
except Error as error:
    print(error)
finally:
    conn.close()
    cursor.close()
