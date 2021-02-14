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

    temp_1 = [list_des_achetes[0]]
    for i in list_des_achetes[1:]:
        if i[0] == temp_1[-1][0]:
            temp_1[-1].append(i[1])
        else:
            temp_1.append(i)
    list_des_achetes = temp_1

    return list_des_achetes
