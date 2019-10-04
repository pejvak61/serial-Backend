import mysql.connector
from mysql.connector import Error
def db_connectivity():
    try:
        connection_config_dict = {
        'user': 'root',
        'password': 'Pejvak.61',
        'host': 'localhost',
        'port':3306,
        'database': 'dino',
        'raise_on_warnings': True,
        'use_pure': False,
        'autocommit': True,
        'pool_size': 5
        }
        connection = mysql.connector.connect(**connection_config_dict)
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("Your connected to database: ", record)
            return("Your connected to database: ", record)
    except Error as e:
        print("Error while connecting to MySQL", e)
        return("Error while connecting to MySQL", e)
    finally:
        try:
            if (connection.is_connected()):
                cursor.close()
                connection.close()
                print("MySQL connection is closed")
                return("MySQL connection is closed")
        except:
            print("Sth went wrong!")
            return("Sth went wrong!")