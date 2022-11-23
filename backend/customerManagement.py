import sys
from backend import connection


def Register(customerInfo):
    conn = None
    sql = """INSERT INTO customer VALUES (%s,%s, %s, %s, %s, %s, %s, %s)"""
    values = (customerInfo.getCid(), customerInfo.getFullName(), customerInfo.getAddress(),
              customerInfo.getEmail(), customerInfo.getNumber(), customerInfo.getPassword(), customerInfo.getPayment(), customerInfo.getStatus())
    result = False
    try:
        conn = connection.connect()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        result = True
    except:
        print("Error : ", sys.exc_info())
    finally:
        del sql
        del conn
        return result
        return values
