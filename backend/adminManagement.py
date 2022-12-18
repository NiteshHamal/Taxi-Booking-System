from backend.connection import connect
import sys

def adminhistory():
    sql = """SELECT * FROM booking WHERE NOT status='Pending'"""
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
