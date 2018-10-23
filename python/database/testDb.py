import pyodbc


def sql_db_call(print_result=False):
    cnxn = pyodbc.connect("Driver=ODBC Driver 13 for SQL Server;"
                          "Server=abx-de.database.windows.net;"
                          "Database=abx-de;"
                          "UID=arg;"
                          "PWD=ar_dbuser33_de;")

    cursor = cnxn.cursor()
    cursor.execute('select top(10) system from arg_accountNumber')

    if print_result:
        for row in cursor:
            print('row = %r' % (row,))

    cnxn.close


for i in range(1000):
    print(i)
    sql_db_call()
