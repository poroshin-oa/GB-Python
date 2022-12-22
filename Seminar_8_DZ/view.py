import controller as cont
import tkinter as tk

def show_main_form():
    main_window = tk.Tk()  
    main_window.title("Телефонный справочник")  
    main_window.resizable(False, False)

    # Для отображения окна по центру
    set_width = (main_window.winfo_screenwidth() // 2) - 200
    set_height = (main_window.winfo_screenheight() // 2) - 300
    main_window.geometry('400x600+{}+{}'.format(set_width, set_height))

    main_window.mainloop() 

def show_contacts_list(contacts_list):
    contacts_list_length = len(contacts_list)

    for i in range(contacts_list_length):
        print(f"{contacts_list[i][1]} | {contacts_list[i][2]}")

def input_new_contact():
    new_contact_list = []
    new_contact_list.append(input("Введите имя> "))
    new_contact_list.append(input("Введите номер> "))

    return new_contact_list

def input_id_del_contact():
    id_del_contact = int(input("Введите id удаляемого контакта> "))
    return id_del_contact