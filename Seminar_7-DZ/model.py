import sqlite3

BASE_FILE_NAME = "contacts.db"

def connect_sqlite_base():
    try:
        sqlite_connect = sqlite3.connect(BASE_FILE_NAME)
        sqlite_cursor = sqlite_connect.cursor()

        return sqlite_cursor
    except:
        print("Error DB!")

def get_contacts_list():
    get_list_connect = connect_sqlite_base()
    get_list_query = "SELECT id, name, phone FROM Contacts"
    get_list_cursor = get_list_connect.execute(get_list_query)

    return get_list_cursor.fetchall()

