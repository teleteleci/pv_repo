from sqldatabase import DbConn

if __name__ == '__main__':
    dbConn = DbConn()
    x = dbConn.set_dev_login(user='unoadmin', pwd='ZEV-AxL-qGT-5WP')

    x.run_query(query='SELECT getdate()')
