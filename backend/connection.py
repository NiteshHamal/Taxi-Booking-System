import sys
import mysql.connector


def connect():
    conn = None
    try:
        conn = mysql.connector.connect(
            host="localhost", port='3306', user='root', password='', database='taxibooking')
    except:
        print("Error : ", sys.exc_info())
    finally:
        return conn
