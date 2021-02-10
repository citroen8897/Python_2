import mysql.connector
from mysql.connector import Error

try:
    conn = mysql.connector.connect(user='root',
                                   host='localhost',
                                   database='mysql')
    if conn.is_connected():
        print('Соединение с базой данных установлено....')
except Error as error:
    print(error)
finally:
    conn.close()
