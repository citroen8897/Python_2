import mysql.connector
from mysql.connector import Error


def users_de_data_base():
    list_des_users = []
    list_des_users_id = []
    try:
        conn = mysql.connector.connect(user='root',
                                       host='localhost',
                                       database='mysql')
        if conn.is_connected():
            print('Соединение с базой данных пользователей установлено....')
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM market_10_02")
            row = cursor.fetchone()
            while row is not None:
                list_des_users.append([row[1], row[2]])
                list_des_users_id.append([row[0], row[1], row[2]])
                row = cursor.fetchone()
    except Error as error:
        print(error)
    finally:
        conn.close()
        cursor.close()

    return list_des_users, list_des_users_id
