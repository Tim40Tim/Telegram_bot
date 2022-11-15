from telebot.types import Message
from keyboards.inline.settings_keyboard import *
from message_sample.mess_dictionary import bot_mess
from users.user_add import Users
from loader import bot


@bot.message_handler(commands=['settings'])
def bot_settings(message: Message) -> None:
    """
    Установка языка и валюты
    :param message:
    :return:
    """
    user = Users.get_user(message.chat.id)
    bot.send_message(chat_id=message.chat.id, text=bot_mess[user.language]['set_lang'],
                     reply_markup=setting_lang_keyboard())
    bot.send_message(chat_id=message.chat.id, text=bot_mess[user.language]['set_cur'],
                     reply_markup=setting_curr_keyboard())
