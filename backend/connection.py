import sys

import mysql.connector
import pymysql.cursors


def connect():
    conn = None
    try:
        conn = mysql.connector.connect(host='localhost',
                                       port=3306,
                                       user='root',
                                       password='',
                                       database='taxi',
                                       )
    except:
        print("Error : ", sys.exc_info())
    finally:
        return conn
