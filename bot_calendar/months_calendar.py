from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from message_sample.mess_dictionary import bot_mess
from users.user_add import Users
from datetime import date


def create_months_calendar(user: Users, dates: date) -> InlineKeyboardMarkup:
    """
    Функция создаёт календарь состоящий из месяцев,
    переданные параметры позволяют при выборе месяца не попадать в прошедшую дату

    :param dates: текущая дата
    :param user: для установки языка пользователя
    :return: клавиатуру с месяцами
    """

    keyboard = InlineKeyboardMarkup()

    for i, month in enumerate(zip(bot_mess[user.language]['months'][0::2],
                                  bot_mess[user.language]['months'][1::2])):
        keyboard.add(
            InlineKeyboardButton(month[0], callback_data=f"MONTH:{dates.year}:{2 * i + 1}:{dates.day}"),
            InlineKeyboardButton(month[1], callback_data=f"MONTH:{dates.year}:{(i + 1) * 2}:{dates.day}"))

    return keyboard
