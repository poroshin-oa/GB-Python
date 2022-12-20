import model as core
import controller as cont

def show_main_menu():
    print("\nВыберите действие:\n")
    print("1: Показать список")
    print("2: Добавить запись")
    print("3: Удалить запись\n")

def get_main_action():
    main_action = input("> ")

    while not cont.check_user_input(main_action):
        main_action = input("Ошибка! Повторите ввод > ")
    else:
        cont.user_select(main_action)