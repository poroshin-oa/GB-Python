import sqlite3
import view
import csv

BASE_FILE_NAME = "contacts.db"

def connect_sqlite_base():
    try:
        sqlite_connect = sqlite3.connect(BASE_FILE_NAME)

        return sqlite_connect
    except:
        print("Error DB!")

def get_contacts_list():
    get_list_connect = connect_sqlite_base()
    get_list_cursor = get_list_connect.cursor()

    get_list_query = "SELECT id, name, phone FROM Contacts"
    get_list_execute = get_list_cursor.execute(get_list_query)

    return get_list_execute.fetchall()

def add_new_contact():
    new_contact_data = view.input_new_contact()
    new_name = new_contact_data[0]
    new_phone = new_contact_data[1]
    
    try:
        add_contact_connect = connect_sqlite_base()
        add_contact_cursor = add_contact_connect.cursor()

        add_contact_query = f"INSERT INTO Contacts (name, phone) VALUES ('{new_name}', '{new_phone}')"
        add_contact_cursor.execute(add_contact_query)

        add_contact_connect.commit()

        print("Запись добавлена успешно!")
    except:
        print("Ошибка добавления данных!")


def del_contact():
    id_delete = view.input_id_del_contact()

    try:
        del_contact_connect = connect_sqlite_base()
        del_contact_cursor = del_contact_connect.cursor()

        del_contact_query = f"DELETE FROM Contacts WHERE id={id_delete}"
        del_contact_cursor.execute(del_contact_query)

        del_contact_connect.commit()
        print("Запись удалена успешно!")

    except:
        print("Ошибка удаления!")

def import_csv(csv_file_name):
    pass

def export_csv():
    try:
        export_list = get_contacts_list()
        export_list_length = len(export_list)

        with open("export.csv", "a") as csv_export_file:
            csv_writer = csv.writer(csv_export_file)

            for i in range(export_list_length):
                export_line = f"{export_list[i][1]}; {export_list[i][2]}"
                csv_writer.writerow([export_line])

        print("Экспорт выполнен успешно!")
    except:
        print("Ошибка экспорта!")
    
