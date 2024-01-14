import mysql.connector

def koneksi():
    host = "localhost"
    user = "root"
    password = ""
    database = "5220411209"


    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    return connection

def tutup_koneksi(connection, cursor):
    cursor.close()
    connection.close()