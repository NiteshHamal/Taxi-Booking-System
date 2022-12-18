from backend.connection import connect
import sys
from middleware.driver import Driver


def add(driverInfo):
    sql = """INSERT INTO driver VALUES(%s,%s,%s,%s,%s,%s,%s)"""
    values = (driverInfo.getDid(), driverInfo.getFullname(), driverInfo.getAddress(
    ), driverInfo.getEmail(), driverInfo.getLicenseno(), driverInfo.getStatus(), driverInfo.getPassword())
    result = True
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
    except:
        print("Error : ", sys.exc_info())
    finally:
        del values, sql
        return result


def statusUpdate(updatestatus):
    sql = """UPDATE driver SET status=%s WHERE did = %s"""
    values = (updatestatus.getStatus(), updatestatus.getDid())
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


def searchDriver(did):
    sql = """SELECT * FROM driver WHERE did = %s"""
    values = (did,)
    driverinfo = None
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        driverinfo = cursor.fetchone()
        cursor.close()
        conn.close()
    except:
        print("Error : ", sys.exc_info())
    finally:
        del values, sql
        return driverinfo


def driverManage():
    sql = """SELECT * FROM driver"""
    drivertable = None
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        drivertable = cursor.fetchall()
        cursor.close()
        conn.close()
    except:
        print("Error : ", sys.exc_info())
    finally:
        del sql
        return drivertable


def driverSearch(name):
    sql = """SELECT * FROM driver WHERE fullname LIKE '%{}%' OR email LIKE '%{}%' OR address LIKE '%{}%'""".format(
        name, name, name)
    sdriver = None
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        sdriver = cursor.fetchall()
        cursor.close()
        conn.close()
    except:
        print("Error : ", sys.exc_info())
    finally:
        del sql
        return sdriver


def editDri(driver):
    sql = """ Update driver SET fullname=%s, address=%s, email=%s, licenseno=%s WHERE did=%s """
    values = [driver.getFullname(), driver.getAddress(), driver.getEmail(),
              driver.getLicenseno(), driver.getDid()]
    edriver = False
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        edriver = True
    except:
        print("Error : ", sys.exc_info())
    finally:
        del values, sql
        return edriver


def deleteDri(did):
    sql = """DELETE FROM driver WHERE did = %s"""
    values = [did.getDid()]
    ddriver = False
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        ddriver = True
    except:
        print("Error : ", sys.exc_info())
    finally:
        del values, sql
        return ddriver


def drivertablead():
    sql = """SELECT did, fullname, address  FROM driver WHERE status='Active'"""
    driverad = None
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        driverad = cursor.fetchall()
        cursor.close()
        conn.close()
    except:
        print("Error : ", sys.exc_info())
    finally:
        del sql
        return driverad


def upcoming_trip(cusname):
    sql = """"""
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


def driver_booking_table():
    conn = None
    sql = """select booking.bookingid, customer.fullname, customer.number, booking.pickup_address, 
    booking.drop_address, booking.pickup_date, booking.pickup_time, booking.status from booking 
    left join customer on booking.cid = customer.cid where not booking.status='Pending' order by booking.status desc"""
    result = None
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        conn.close()

    except:
        print("Error", sys.exc_info())

    finally:
        del sql, conn
        return result

# def driver_update_booking(didInfo):
#     sql = """UPDATE driver SET status=%s WHERE did = %s"""
#     values = (didInfo.getStatus(), didInfo.getDid())
#     result = False
#     try:
#         conn = connect()
#         cursor = conn.cursor()
#         cursor.execute(sql, values)
#         conn.commit()
#         cursor.close()
#         conn.close()
#         result = True
#     except:
#         print("Error : ", sys.exc_info())
#     finally:
#         del values, sql
#         return result
