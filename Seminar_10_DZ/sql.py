import sqlite3 as sql

BASE_FILE_NAME = "contacts.db"

def connect_sqlite_base():
    try:
        sqlite_connect = sql.connect(BASE_FILE_NAME)

        return sqlite_connect
    except:
        print("Error DB!")

def get_contacts_list():
    get_list_connect = connect_sqlite_base()
    get_list_cursor = get_list_connect.cursor()

    get_list_query = "SELECT id, name, phone FROM Contacts"
    get_list_execute = get_list_cursor.execute(get_list_query)

    contacts_list = get_list_execute.fetchall()

    return contacts_list