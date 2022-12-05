from backend.connection import connect
import sys


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
