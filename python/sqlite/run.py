import sqlite3
import csv


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Exception as e:
        print(e)
        raise e

    return conn


def select_all_tasks(conn, select_condition):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """

    cur = conn.cursor()
    cur.execute(select_condition)

    columns_names_list = list(map(lambda x: x[0], cur.description))

    csvWriter = csv.writer(open("test.csv", "w"))
    csvWriter.writerow(columns_names_list)
    rows = cur.fetchall()
    for row in rows:
        csvWriter.writerow(list(row))


def main():
    database = '/Users/pav/Documents/worka/gitRepo/pv_repo/python/sqlite/svod.sqlite'

    # create a database connection
    conn = create_connection(database)
    with conn:
        print("2. Query all tasks")
        select_all_tasks(conn, 'SELECT * FROM incmort')


if __name__ == '__main__':
    main()
