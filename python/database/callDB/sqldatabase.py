class DbConn:
    def nvl(a, b):
        return a or b

    def __init__(self, server=None, database=None, user=None, pwd=None):
        self.server = server
        self.database = database
        self.__username = user
        self.__password = pwd

    def set_dev_login(self, user, pwd):
        return DbConn(server='abx-mssql-dev.database.windows.net',
                      database=(self.database or 'abx-mssqldb-dev'),
                      user=user,
                      pwd=pwd)

    def run_query(self, query):
        import pyodbc

        DRIVER = '{ODBC Driver 13 for SQL Server}'

        cnxn = pyodbc.connect(
            'DRIVER={drv};SERVER={srv};PORT=1433;DATABASE={db};'
            + 'UID={user};PWD={pwd}'.format(
                DRIVER,
                self.server,
                self.database,
                self.__username,
                self.__password
            )
        )

        cursor = cnxn.cursor()
        cursor.execute(query)
        row = cursor.fetchone()
        while row:
            print(str(row[0]) + " " + str(row[1]))
            row = cursor.fetchone()
