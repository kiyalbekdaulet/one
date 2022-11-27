# import sqlite3
#
# try:
#     sqliteConnection = sqlite3.connect('dau.db')
#     sqlite_create_table_query = '''CREATE TABLE users (
#                                 id INTEGER PRIMARY KEY,
#                                 name TEXT NOT NULL,
#                                 email text NOT NULL UNIQUE,
#                                 joining_date datetime,
#                                 salary REAL NOT NULL);'''
#
#     cursor = sqliteConnection.cursor()
#     print("Successfully Connected to SQLite")
#     cursor.execute(sqlite_create_table_query)
#     sqliteConnection.commit()
#     print("SQLite table created")
#
#     cursor.close()
#
# except sqlite3.Error as error:
#     print("Error while creating a sqlite table", error)
# finally:
#     if sqliteConnection:
#         sqliteConnection.close()
#         print("sqlite connection is closed")


import sqlite3

try:
    sqliteConnection = sqlite3.connect('dau.db')
    cursor = sqliteConnection.cursor()
    print("Successfully Connected to SQLite")

    sqlite_insert_query = """INSERT INTO users
                          (id, name, email, joining_date, salary) 
                           VALUES 
                          (1,'James','james@pynative.com','2019-03-17',8000)"""

    count = cursor.execute(sqlite_insert_query)
    sqliteConnection.commit()
    print("Record inserted successfully into SqliteDb_developers table ", cursor.rowcount)
    cursor.close()

except sqlite3.Error as error:
    print("Failed to insert data into sqlite table", error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("The SQLite connection is closed")