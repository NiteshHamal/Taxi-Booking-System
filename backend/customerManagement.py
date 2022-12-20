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
    sql = """SELECT cid, fullname, address, email, number, payment FROM customer"""
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


def customerSearch(name):
    sql = """SELECT * FROM customer WHERE fullname LIKE '%{}%' OR email LIKE '%{}%' OR address LIKE '%{}%'""".format(
        name, name, name)
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


def editCus(customer):
    sql = """ Update customer SET fullname=%s, address=%s, email=%s, number=%s, payment=%s WHERE cid=%s """
    values = [customer.getFullName(), customer.getAddress(), customer.getEmail(
    ), customer.getNumber(), customer.getPayment(), customer.getCid()]
    ecustomer = False
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        ecustomer = True
    except:
        print("Error : ", sys.exc_info())
    finally:
        del values, sql
        return ecustomer


def deleteCus(cid):
    sql = """DELETE FROM customer WHERE cid = %s"""
    values = [cid.getCid()]
    dcustomer = False
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        dcustomer = True
    except:
        print("Error : ", sys.exc_info())
    finally:
        del values, sql
        return dcustomer


def customer_change_password(cidInfo):
    sql = """UPDATE customer SET password=%s WHERE cid=%s"""
    values = (cidInfo.getPassword(), cidInfo.getCid())
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
