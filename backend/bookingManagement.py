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


def requestBooking():
    sql = """SELECT booking.cid, customer.fullname, booking.pickup_address, booking.drop_address, booking.pickup_date, 
    booking.pickup_time, booking.status FROM booking LEFT JOIN customer ON booking.cid = customer.cid 
    WHERE booking.status = 'Pending'"""
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
