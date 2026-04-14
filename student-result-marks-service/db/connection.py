import mysql.connector

def get_connection():

    conn = mysql.connector.connect(
        host="localhost",   # changed from localhost
        user="root",
        password="1234567890",
        database="university_db",
        auth_plugin='mysql_native_password'   # added authentication plugin
    )

    return conn