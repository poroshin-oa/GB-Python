import model as core
import control as ctrl

import telebot as tg_api

TOKEN = "5882762303:AAEzWNN7e5a9OYbeuIi8MnLtL8_vNFVF5Mk"

if __name__ == "__main__":
    bot_obj = tg_api.TeleBot(TOKEN)

    @bot_obj.message_handler(commands=["start"])
    def show_bot_menu(message):
        bot_obj.send_message(message.chat.id, 
        "Привет, выбери команду:\n\n /show - показать весь список\n /add - добавить запись\n /rem - удалить запись \n /exp_csv - экспорт списка в csv\n /exp_xml - экспорт списка в xml")
    
    @bot_obj.message_handler(content_types=["text"])
    def get_user_input(message):
        bot_obj.send_message(message.chat.id, 'Вы написали: ' + message.text)


    bot_obj.polling(none_stop=True, interval=0)