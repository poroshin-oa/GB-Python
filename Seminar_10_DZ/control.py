import model as core
import view as bot_interface

VALID_COMMAND_LIST = ["/show", "/add", "/rem", "/exp_csv", "/exp_xml"]

def check_valid_command(inp_command):
    if inp_command not in VALID_COMMAND_LIST:
        return False
    else:
        main_menu(inp_command)
        return True

def check_add_item(input_string):
    pass

def main_menu(menu_item):
    if menu_item == "show":
        contact_list = core.get_contacts_list()
        table = bot_interface.show_contacts_list(contact_list)

        return table
    elif menu_item == "add":
        core.add_contact("name", "phone")
    elif menu_item == "rem":
        core.del_contact("1")
    elif menu_item == "exp_csv":
        core.export_list_csv()
    elif menu_item == "exp_xml":
        core.export_list_xml()
