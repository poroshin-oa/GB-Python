import model as core
from prettytable import PrettyTable

def show_contacts_list(non_format_contact_list):
    contacts_table = PrettyTable()
    contacts_table.field_names = ["ID", "ИМЯ", "ТЕЛЕФОН"]

    contacts_table.add_row(["1", "Oleg", "8(900)546-17-05"])
    print(contacts_table)