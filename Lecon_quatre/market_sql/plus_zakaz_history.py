import mysql.connector
from mysql.connector import Error


def get_last_numero_de_zakaz():
    list_des_numeros = []
    try:
        conn = mysql.connector.connect(user='root',
                                       host='localhost',
                                       database='mysql')
        if conn.is_connected():
            print('Соединение с базой данных товаров установлено....')
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM market_history_des_achetes")
            row = cursor.fetchone()
            while row is not None:
                list_des_numeros.append(row[1])
                row = cursor.fetchone()
    except Error as error:
        print(error)
    finally:
        conn.close()
        cursor.close()
    if len(list_des_numeros) == 0:
        last_numero = 0
    else:
        last_numero = int(list_des_numeros[-1])
    return last_numero + 1


def plus_product_history_de_user(zakaz_numero, id_product,
                                 nom_product, id_user):
    try:
        conn = mysql.connector.connect(user='root',
                                       host='localhost',
                                       database='mysql')

        if conn.is_connected():
            print('Соединение с базой данных товаров установлено....')
            new_position = "INSERT INTO market_history_des_achetes(" \
                           "numero_de_zakaz, product_id, product_nom," \
                           " id_user) VALUES(%s,%s,%s,%s)"
            cursor = conn.cursor()
            cursor.execute(new_position, (zakaz_numero, id_product,
                                          nom_product, id_user))

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
