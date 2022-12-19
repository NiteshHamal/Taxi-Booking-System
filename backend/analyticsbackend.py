import sys
from backend.connection import connect


def totalbooking():

    conn=None
    sql="""SELECT COUNT(bookingid) from booking"""
    bookingresult=None
    try:
        conn=connect()
        cursor=conn.cursor()
        cursor.execute(sql)
        bookingresult=cursor.fetchall()
        cursor.close()
        conn.close()


    except:
        print("Error", sys.exc_info())

    finally:
        del sql, conn
        return bookingresult


def totalcustomers():

    conn=None
    sql="""SELECT COUNT(cid) from customer"""
    customerresult=None
    try:
        conn=connect()
        cursor=conn.cursor()
        cursor.execute(sql)
        customerresult=cursor.fetchall()
        cursor.close()
        conn.close()


    except:
        print("Error", sys.exc_info())

    finally:
        del sql, conn
        return customerresult

def totaldrivers():

    conn=None
    sql="""SELECT COUNT(did) from driver"""
    driverresult=None
    try:
        conn=connect()
        cursor=conn.cursor()
        cursor.execute(sql)
        driverresult=cursor.fetchall()
        cursor.close()
        conn.close()


    except:
        print("Error", sys.exc_info())

    finally:
        del sql, conn
        return driverresult
