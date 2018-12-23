import pyodbc
import connections as c
import time
from datetime import datetime


def exec_single_query(thread_name, sql='select getdate()', idle_time=0):
    time.sleep(idle_time)
    startTime = datetime.now()

    cnxn = pyodbc.connect(c.get_aze_db_conn_string())
    cursor = cnxn.cursor()
    obtain_cnx_time = datetime.now() - startTime
    cursor.execute(sql)
    for row in cursor:
        ret = row

    print('{}, {}, cn = {}, idle = {}'.format(obtain_cnx_time,
                                              thread_name,
                                              ret,
                                              idle_time))

    time.sleep(idle_time)
    try:
        cursor.execute(sql)
    except Exception as e:
        print('Error, {}, idle = {}, {}'.format(idle_time,
                                                thread_name,
                                                obtain_cnx_time - startTime))
        raise e
    finally:
        cnxn.close


if __name__ == '__main__':
    exec_single_query('t1', idle_time=5)
