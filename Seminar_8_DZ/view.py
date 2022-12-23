# TODO: Scroll Main List
# TODO: Disable active button

import controller as cont
import tkinter as tk
import model as core

# Глобалим переменные только из-за отсутствия ООП
# По уму, это все нужно паковать в класс

def show_main_form():
    global main_window

    main_window = tk.Tk()  
    main_window.title("Телефонный справочник")  
    main_window.resizable(False, False)

    # Для отображения окна по центру
    set_width = (main_window.winfo_screenwidth() // 2) - 200
    set_height = (main_window.winfo_screenheight() // 2) - 300
    main_window.geometry('600x300+{}+{}'.format(set_width, set_height))
    
    show_contacts_list()
    show_button_menu()
    show_dialog_frame()

    main_window.mainloop()

def show_contacts_list():
    lbox = tk.Listbox(width = 40, height = 150)
    lbox.pack(side="left", padx=5, pady=5)

    contacts_list = core.get_contacts_list()
    contacts_list.reverse()

    # Выводим в список на форму
    for i in contacts_list:
        lbox.insert(0, i)

def clear_dialog_frame():
    for widget in dialog_frame.winfo_children():
        widget.destroy()

def show_dialog_frame():
    global dialog_frame

    dialog_frame = tk.Frame(main_window, width=100, height=155)
    dialog_frame.pack(fill="x", padx=6, pady=6)

def show_add_dialog():
    clear_dialog_frame()

    tk.Label(dialog_frame, text = "Введите имя:").pack(fill="x")
    add_name = tk.Entry(dialog_frame).pack(fill="x")
    tk.Label(dialog_frame, text = "Введите номер:").pack(fill="x")
    add_phone = tk.Entry(dialog_frame).pack(fill="x")
    add_submit_button = tk.Button(dialog_frame, text = "Добавить запись").pack(fill="x")

def show_log_dialog():
    clear_dialog_frame()

    tk.Label(dialog_frame, text = "LOG-файл:").pack(fill="x")
    log_listbox = tk.Listbox(width = 40, height = 150)
    log_listbox.pack(padx=5, pady=5)

def show_import_dialog():
    clear_dialog_frame()
    tk.Label(dialog_frame, text = "Insert File Name for import").pack(fill="x", side="left")

def show_export_dialog():
    clear_dialog_frame()
    tk.Label(dialog_frame, text = "Insert File Name for export").pack(fill="x", side="left")

def show_button_menu():
    add_button = tk.Button(text="Добавить", width=100, command = show_add_dialog).pack(fill="x", padx=2)
    del_button = tk.Button(text="Удалить", width=100).pack(fill="x", padx=2)
    export_button = tk.Button(text="Экспорт списка", width=100, command = show_export_dialog).pack(fill="x", padx=2)
    import_button = tk.Button(text="Импорт списка", width=100, command = show_import_dialog).pack(fill="x", padx=2)
    log_button = tk.Button(text="Просмотреть лог", width=100, command = show_log_dialog).pack(fill="x", padx=2)

def input_new_contact():
    new_contact_list = []
    new_contact_list.append(input("Введите имя> "))
    new_contact_list.append(input("Введите номер> "))

    return new_contact_list

def input_id_del_contact():
    id_del_contact = int(input("Введите id удаляемого контакта> "))
    return id_del_contact