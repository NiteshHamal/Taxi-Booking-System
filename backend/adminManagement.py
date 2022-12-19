from backend.connection import connect
import sys


def adminhistory():
    sql = """SELECT * FROM booking WHERE status='Completed'"""
    historyResult = None
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        historyResult = cursor.fetchall()
        cursor.close()
        conn.close()
    except:
        print("Error : ", sys.exc_info())
    finally:
        del sql
        return historyResult


def admin_change_password(adminInfo):
    sql = """UPDATE admin SET password=%s WHERE adminid=%s"""
    values = (adminInfo.getPassword(), adminInfo.getAdminid())
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


def activebookingtable720():
    sql = """SELECT * FROM booking WHERE status='Confirmed'"""
    activeResult = None
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        activeResult = cursor.fetchall()
        cursor.close()
        conn.close()
    except:
        print("Error : ", sys.exc_info())
    finally:
        del sql
        return activeResult
