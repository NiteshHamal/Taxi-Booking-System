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
