import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="127.0.0.1",   # ← change from localhost
        user="root",
        password="1234567890",
        database="order_db",
        auth_plugin='mysql_native_password'   # ← ADD THIS LINE
    )
