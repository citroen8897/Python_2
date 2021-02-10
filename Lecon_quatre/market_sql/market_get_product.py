import mysql.connector
from mysql.connector import Error


def products_de_data_base():
    list_des_products = []
    try:
        conn = mysql.connector.connect(user='root',
                                       host='localhost',
                                       database='mysql')
        if conn.is_connected():
            print('Соединение с базой данных установлено....')
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM market_products")
            row = cursor.fetchone()
            while row is not None:
                print(f'id: {row[0]}    товар: {row[1]}    цена за кг: {row[2]}')
                list_des_products.append([row[1], row[2]])
                row = cursor.fetchone()
    except Error as error:
        print(error)
    finally:
        conn.close()
        cursor.close()

    return list_des_products
