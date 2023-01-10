import sys
from backend.connection import connect


def login(customerInfo):
    sql = "SELECT * FROM customer WHERE email=%s AND password = %s"
    values = (customerInfo.getEmail(), customerInfo.getPassword())
    user = None
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        user = cursor.fetchone()
        cursor.close()
        conn.close()
    except:
        print("Error : ", sys.exc_info())
    finally:
        del values, sql
        return user


def dlogin(driverInfo):
    sql = """SELECT * FROM driver WHERE email=%s AND password=%s"""
    values = (driverInfo.getEmail(), driverInfo.getPassword())
    duser = None
    try:
        conn = connect()
        cursor = conn. cursor()
        cursor.execute(sql, values)
        duser = cursor.fetchone()
        cursor.close()
        conn.close()
    except:
        print("Error : ", sys.exc_info())
    finally:
        del values, sql
        return duser


def alogin(adminInfo):
    sql = """SELECT * FROM admin WHERE email=%s AND password=%s"""
    values = (adminInfo.getEmail(), adminInfo.getPassword())
    auser = None
    try:
        conn = connect()
        cursor = conn. cursor()
        cursor.execute(sql, values)
        auser = cursor.fetchone()
        cursor.close()
        conn.close()
    except:
        print("Error : ", sys.exc_info())
    finally:
        del values, sql
        return auser
