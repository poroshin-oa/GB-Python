import model as core
import view as bot_interface

VALID_COMMAND_LIST = ["/show", "/add", "/rem", "/exp_csv", "/exp_xml"]

def check_user_input(user_message):
    if user_message not in VALID_COMMAND_LIST:
        return False
    else:
        main_menu(user_message)

def main_menu(menu_item):
    if menu_item == "/show":
        contact_list = core.get_contacts_list()
        bot_interface.show_contacts_list(contact_list)
    elif menu_item == "/add":
        core.add_contact("name", "phone")
    elif menu_item == "/rem":
        core.del_contact("1")
    elif menu_item == "/exp_csv":
        core.export_list_csv()
    elif menu_item == "/exp_xml":
        core.export_list_xml()
