from users.user_add import Users
from telebot.types import CallbackQuery
from loguru import logger
from loader import bot


@bot.callback_query_handler(func=lambda call: call.data in ('ru_RU', 'en_US'))
def change_lang(call: CallbackQuery) -> None:
    """Установка языка пользователем"""
    user = Users.get_user(call.message.chat.id)
    user.language = call.data
    logger.info(f'Set lang for user: userID = {user.user_id}, param: {call.data}')
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.id)


@bot.callback_query_handler(func=lambda call: call.data in ('RUB', 'USD', 'EUR'))
def change_cur(call: CallbackQuery) -> None:
    """Установка валюты пользователем"""
    user = Users.get_user(call.message.chat.id)
    user.currency = call.data
    logger.info(f'Set curr for user: userID = {user.user_id}, param:{call.data}')
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.id)
