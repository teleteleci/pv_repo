import pyodbc
from random import randint


def sql_db_call(print_result=False):
    cnxn = pyodbc.connect("Driver=ODBC Driver 13 for SQL Server;"
                          "Server=abx-de.database.windows.net;"
                          "Database=abx-de;"
                          "UID=arg;"
                          "PWD=ar_dbuser33_de;")

    cursor = cnxn.cursor()
    sql_code = \
        'select a.currencyCode, cast(a.created as date), count(1) as cc ' + \
        'from arg_accountNumber a ' + \
        'group by a.currencyCode, cast(a.created as date )' + \
        'having count(1) > ' + \
        str(randint(1, 53))
    # print(sql_code)

    cursor.execute(sql_code)

    if print_result:
        for row in cursor:
            print('row = %r' % (row,))

    cnxn.close


for i in list(range(100)):
    # print(i)
    sql_db_call()
