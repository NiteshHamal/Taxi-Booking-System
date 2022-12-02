import sys
from backend.connection import connect


def register(customerInfo):
    sql = """INSERT INTO customer VALUES (%s,%s, %s, %s, %s, %s, %s)"""
    values = (customerInfo.getCid(), customerInfo.getFullName(), customerInfo.getAddress(),
              customerInfo.getEmail(), customerInfo.getNumber(), customerInfo.getPassword(), customerInfo.getPayment())
    result = False
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        result = True
    except:
        print("Error : ", sys.exc_info())
    finally:
        del values, sql
        return result
