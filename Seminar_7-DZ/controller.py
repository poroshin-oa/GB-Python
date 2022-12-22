import model as core
import view as interface

def check_user_input(user_input_str):
    true_list = ["1", "2", "3", "4", "5"]
    
    if user_input_str in true_list:
        return True
    else:
        return False

def user_select(user_select_item):
    if user_select_item == "1":
        contacts_list = core.get_contacts_list()
        interface.show_contacts_list(contacts_list)
    elif user_select_item == "2":
        new_contact_input = interface.input_new_contact()
        core.add_new_contact(new_contact_input[0], new_contact_input[1])
    elif user_select_item == "3":
        core.del_contact()
    elif user_select_item == "4":
        core.import_csv()
    elif user_select_item == "5":
        core.export_csv()










