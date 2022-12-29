import model as core
from prettytable import PrettyTable

def format_phone_number(non_format_phone_number):
    format_phone = f"{non_format_phone_number[0]}({non_format_phone_number[1:4]}){non_format_phone_number[4:7]}-{non_format_phone_number[7:9]}-{non_format_phone_number[9:11]}"

    return format_phone

def create_contacts_table(non_format_contact_list):
    phone = format_phone_number("89005461705")
    print(phone)

def show_contacts_list(non_format_contact_list):
    contacts_table = create_contacts_table(non_format_contact_list)
    