import controller as cont

def show_main_menu():
    print("\nВыберите действие:\n")
    print("1: Показать список")
    print("2: Добавить запись")
    print("3: Удалить запись")
    print("4: Импорт записей из csv")
    print("5: Экспорт записей в csv\n")

def get_main_action():
    main_action = input("> ")

    while not cont.check_user_input(main_action):
        main_action = input("Ошибка! Повторите ввод > ")
    else:
        cont.user_select(main_action)

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