import mysql.connector
from mysql.connector import Error

product_nom = input('Введите название товара: ')
product_price = input('Введите цену товара: ')

try:
    conn = mysql.connector.connect(user='root',
                                   host='localhost',
                                   database='mysql')

    if conn.is_connected():
        print('Соединение с базой данных товаров установлено....')
        new_user = "INSERT INTO market_products(product, price) " \
                   "VALUES(%s,%s)"
        cursor = conn.cursor()
        cursor.execute(new_user, (product_nom, product_price))

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
