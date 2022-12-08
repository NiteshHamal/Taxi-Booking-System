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


def customerManage():
    sql = """SELECT * FROM customer"""
    customertable = None
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        customertable = cursor.fetchall()
        cursor.close()
        conn.close()
    except:
        print("Error : ", sys.exc_info())
    finally:
        del sql
        return customertable


def test(name):
    sql = """SELECT * FROM customer WHERE fullname LIKE '%{}%'""".format(name)
    testname = None
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        testname = cursor.fetchall()
        cursor.close()
        conn.close()
    except:
        print("Error : ", sys.exc_info())
    finally:
        del sql
        return testname
