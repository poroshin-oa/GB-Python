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
    main_window.geometry('600x300+{}+{}'.format(set_width, set_height))
    
    show_contacts_list()
    show_button_menu()

    main_window.mainloop()

def show_contacts_list():
    lbox = tk.Listbox(width = 40, height = 150)
    lbox.pack(side="left", padx=5, pady=5)

    # TODO: Scroll
    contacts_list = core.get_contacts_list()
    contacts_list.reverse()

    # Выводим в список на форму
    for i in contacts_list:
        lbox.insert(0, i)

def show_button_menu():
    tk.Button(text="Добавить", width=100).pack(fill="x", padx=2)
    tk.Button(text="Удалить", width=100).pack(fill="x", padx=2)
    tk.Button(text="Экспорт списка", width=100).pack(fill="x", padx=2)
    tk.Button(text="Импорт списка", width=100).pack(fill="x", padx=2)

def input_new_contact():
    new_contact_list = []
    new_contact_list.append(input("Введите имя> "))
    new_contact_list.append(input("Введите номер> "))

    return new_contact_list

def input_id_del_contact():
    id_del_contact = int(input("Введите id удаляемого контакта> "))
    return id_del_contact