import controller as cont
import tkinter as tk
import model as core

def show_main_form():
    main_window = tk.Tk()  
    main_window.title("Телефонный справочник")  
    main_window.resizable(False, False)

    # Для отображения окна по центру
    set_width = (main_window.winfo_screenwidth() // 2) - 200
    set_height = (main_window.winfo_screenheight() // 2) - 300
    main_window.geometry('400x300+{}+{}'.format(set_width, set_height))
    
    show_contacts_list()

    main_window.mainloop() 

def show_contacts_list():
    lbox = tk.Listbox(width = 40, height = 150)
    lbox.pack(pady = 100)

    # TODO: Scroll

    contacts_list = core.get_contacts_list()
    contacts_list_length = len(contacts_list)
    contacts_list_new = []

    # Обработка исходного списка (убираем ID)
    for i in range(contacts_list_length):
        contacts_list_new.append(f"{contacts_list[i][1]}, {contacts_list[i][2]}")

    contacts_list_new.reverse()

    # Выводим в список на форму
    for i in contacts_list_new:
        lbox.insert(0, i)


def input_new_contact():
    new_contact_list = []
    new_contact_list.append(input("Введите имя> "))
    new_contact_list.append(input("Введите номер> "))

    return new_contact_list

def input_id_del_contact():
    id_del_contact = int(input("Введите id удаляемого контакта> "))
    return id_del_contact