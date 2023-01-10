import sys
from backend.connection import connect


def totalbooking():
    sql = """SELECT COUNT(bookingid) from booking"""
    bookingresult = None
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        bookingresult = cursor.fetchall()
        cursor.close()
        conn.close()
    except:
        print("Error", sys.exc_info())
    finally:
        del sql, conn
        return bookingresult


def totalcustomers():
    sql = """SELECT COUNT(cid) from customer"""
    customerresult = None
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        customerresult = cursor.fetchall()
        cursor.close()
        conn.close()
    except:
        print("Error", sys.exc_info())
    finally:
        del sql, conn
        return customerresult


def totaldrivers():
    sql = """SELECT COUNT(did) from driver"""
    driverresult = None
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        driverresult = cursor.fetchall()
        cursor.close()
        conn.close()
    except:
        print("Error", sys.exc_info())
    finally:
        del sql, conn
        return driverresult


def monthbookingcount():
    sql = """select count(bookingid) from booking where pickup_date=YEAR(NOW()) and MONTH(NOW())"""
    monthresult = None
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        monthresult = cursor.fetchall()
        cursor.close()
        conn.close()
    except:
        print("Error", sys.exc_info())
    finally:
        del sql, conn
        return monthresult
