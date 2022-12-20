import sqlite3

BASE_FILE_NAME = "contacts.db"

def connect_sqlite_base():
    try:
        sqlite_connect = sqlite3.connect(BASE_FILE_NAME)
        sqlite_cursor = sqlite_connect.cursor()
    except:
        print("Error DB!")

def get_contacts_list():
    pass

