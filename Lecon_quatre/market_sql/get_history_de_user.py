import mysql.connector
from mysql.connector import Error


def get_zakaz(id_user):
    list_des_achetes = []
    try:
        conn = mysql.connector.connect(user='root',
                                       host='localhost',
                                       database='mysql')
        if conn.is_connected():
            print('Соединение с базой данных пользователей установлено....')
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM market_history_des_achetes "
                           f"WHERE id_user = {id_user}")
            row = cursor.fetchone()
            while row is not None:
                list_des_achetes.append([row[1], row[3]])
                row = cursor.fetchone()
    except Error as error:
        print(error)
    finally:
        conn.close()
        cursor.close()

    return list_des_achetes
