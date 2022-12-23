import sqlite3
import view
import csv

BASE_FILE_NAME = "contacts.db"
EXPORT_CSV_FILE_NAME = "export.csv"
IMPORT_CSV_FILE_NAME = "import.csv"

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

    contacts_list = get_list_execute.fetchall()
    contacts_list_result = []

    for i in range(len(contacts_list)):
        contacts_list_result.append(f"{contacts_list[i][1]}, {contacts_list[i][2]}")

    return contacts_list_result

def add_new_contact(new_name, new_phone):
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

def import_csv():
    try:
        with open(IMPORT_CSV_FILE_NAME) as csv_import_file:
            csv_reader = csv.reader(csv_import_file)

            for i in csv_reader:
                split_list = i[0].split(";")
                split_list_name = split_list[0]
                split_list_phone = split_list[1]

                add_new_contact(split_list_name, split_list_phone)
        
        print("Успешный импорт!")

    except:
        print("Ошибка импорта!")

def export_csv():
    try:
        export_list = get_contacts_list()
        export_list_length = len(export_list)

        with open(EXPORT_CSV_FILE_NAME, "w") as csv_export_file:
            csv_writer = csv.writer(csv_export_file)

            for i in range(export_list_length):
                export_line = f"{export_list[i][1]}; {export_list[i][2]}"
                csv_writer.writerow([export_line])

        print("Экспорт выполнен успешно!")
    except:
        print("Ошибка экспорта!")
    
