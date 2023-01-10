from backend.connection import connect
import sys


def insert(bookingInfo):
    sql = """INSERT INTO booking VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"""
    values = (bookingInfo.getBookingid(), bookingInfo.getPickup_Address(),
              bookingInfo.getDrop_Address(), bookingInfo.getPickup_Date(), bookingInfo.getPickup_Time(),
              bookingInfo.getStatus(), bookingInfo.getCid(), bookingInfo.getDid())
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


def customer_edit_booking(book):
    conn = None
    sql = """UPDATE booking SET pickup_address=%s, drop_address=%s, pickup_date=%s, pickup_time=%s WHERE bookingid=%s"""
    values = (book.getPickup_Address(), book.getDrop_Address(),
              book.getPickup_Date(), book.getPickup_Time(), book.getBookingid())
    updateResult = False

    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        updateResult = True
    except:
        print("Error : ", sys.exc_info())
    finally:
        del conn, values, sql
        return updateResult


def requestBooking(requestb):
    sql = """SELECT booking.cid, booking.bookingid, customer.fullname, booking.pickup_address, booking.drop_address, booking.pickup_date, 
    booking.pickup_time, booking.status FROM booking LEFT JOIN customer ON booking.cid = customer.cid 
    WHERE booking.cid=%s booking.status = 'Pending' """
    values = (requestb, )
    request = None
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        request = cursor.fetchall()
        cursor.close()
        conn.close()
    except:
        print("Error : ", sys.exc_info())
    finally:
        del values, sql
        return request


def requestSearch(name):
    sql = """SELECT * FROM booking WHERE fullname LIKE '%{}%' OR email LIKE '%{}%' OR address LIKE '%{}%'""".format(
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


def cusdastable(book):
    sql = """SELECT bookingid, pickup_address, drop_address, pickup_date, pickup_time FROM booking WHERE cid=%s AND status=%s """
    values = (book.getCid(), book.getStatus())
    cuspending = None
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        cuspending = cursor.fetchall()
        cursor.close()
        conn.close()
    except:
        print("Error : ", sys.exc_info())
    finally:
        del values, sql
        return cuspending


def cancelreqBooking(bid):
    sql = """DELETE FROM booking WHERE bookingid=%s"""
    values = [bid, ]
    cancelreq = False
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        cancelreq = True
    except:
        print("Error : ", sys.exc_info())
    finally:
        del values, sql
        return cancelreq


def requestBooking1167():
    sql = """SELECT booking.cid, booking.bookingid, customer.fullname, booking.pickup_address, booking.drop_address,
    booking.pickup_date, booking.pickup_time, booking.status FROM booking LEFT JOIN customer ON 
    booking.cid = customer.cid WHERE booking.status = 'Pending' AND booking.pickup_date >= CURDATE()"""
    request = None
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        request = cursor.fetchall()
        cursor.close()
        conn.close()
    except:
        print("Error : ", sys.exc_info())
    finally:
        del sql
        return request


def admin_update_booking(Info):
    sql = """UPDATE booking SET status=%s, did=%s WHERE bookingid=%s """
    values = (Info.getStatus(), Info.getDid(), Info.getBookingid())
    updateResult = False

    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        updateResult = True

    except:
        print("Error", sys.exc_info())

    finally:
        del values, sql, conn
        return updateResult


def customerbookinghistory_table(cid):
    sql = """SELECT bookingid, pickup_address, drop_address, pickup_date, pickup_time FROM booking WHERE cid=%s AND status='Completed'"""
    values = (cid,)
    historyResult = None
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        historyResult = cursor.fetchall()
        cursor.close()
        conn.close()
    except:
        print("Error : ", sys.exc_info())
    finally:
        del values, sql
        return historyResult


def completetripbydriver(bid):
    sql = """UPDATE booking SET status=%s WHERE bookingid=%s"""
    values = (bid.getStatus(), bid.getBookingid())
    completetripbydriverresult = False
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        completetripbydriverresult = True
    except:
        print('Error : ', sys.exc_info())
    finally:
        del values, sql
        return completetripbydriverresult


def admincancelbooking():
    sql = """SELECT booking.cid, booking.bookingid, customer.fullname, booking.pickup_address, booking.drop_address, booking.pickup_date, booking.pickup_time, booking.status FROM booking LEFT JOIN customer ON booking.cid = customer.cid WHERE booking.status = 'Pending' AND booking.pickup_date < CURDATE()"""
    request = None
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        request = cursor.fetchall()
        cursor.close()
        conn.close()
    except:
        print("Error : ", sys.exc_info())
    finally:
        del sql
        return request


def cancelbookingbyadmin(bookingid):
    sql = """DELETE FROM booking WHERE bookingid=%s """
    values = (bookingid,)
    cancelbookingbyadminresult = False
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        cancelbookingbyadminresult = True
    except:
        print("Error :", sys.exc_info())
    finally:
        del sql
        return cancelbookingbyadminresult


def requestBooking11672():
    sql = """SELECT booking.cid, booking.bookingid, customer.fullname, booking.pickup_address, booking.drop_address, booking.pickup_date, 
    booking.pickup_time, booking.status FROM booking LEFT JOIN customer ON booking.cid = customer.cid 
    WHERE  booking.status = 'Pending'"""
    request = None
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        request = cursor.fetchall()
        cursor.close()
        conn.close()
    except:
        print("Error : ", sys.exc_info())
    finally:
        del sql
        return request
