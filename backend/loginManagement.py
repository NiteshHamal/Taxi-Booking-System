import sys
from backend.connection import connect


def login(customerInfo):
    sql = "SELECT * FROM customer WHERE email=%s and password = %s"
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
        del sql
        return user
        return values
