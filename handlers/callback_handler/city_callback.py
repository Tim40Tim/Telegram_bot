from bot_calendar.set_calendar import calendar_keyboard
from message_sample.mess_dictionary import bot_mess
from users.user_add import Users
from datetime import date
from telebot.types import CallbackQuery
from loguru import logger
from loader import bot
import re


@bot.callback_query_handler(func=lambda call: call.data.startswith('call data'))
def set_city(call: CallbackQuery) -> None:
    """
    Установка id города выбранного через инлайновую клавиатуру
    :param call:
    :return:
    """
    user = Users.get_user(call.message.chat.id)
    user.city = re.findall(r'\d+', call.data)[0]
    logger.info(f'Set city: userID = {user.user_id}, param: {call.data}')
    if user.check_in is not None:
        user.check_in = None
    bot.edit_message_text(
        chat_id=call.message.chat.id, message_id=call.message.id,
        text=bot_mess[user.language]['check_in'], reply_markup=calendar_keyboard(user=user, dates=date.today()))
