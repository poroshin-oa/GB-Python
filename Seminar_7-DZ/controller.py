def check_user_input(user_input_str):
    true_list = ["1", "2", "3"]
    
    if user_input_str in true_list:
        return True
    else:
        return False

def user_select(user_select_item):
    if user_select_item == "1":
        print("Show_list")
    elif user_select_item == "2":
        print("Add record")
    elif user_select_item == "3":
        print("Del record")










