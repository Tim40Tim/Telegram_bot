from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from message_sample.mess_dictionary import bot_mess
from datetime import date, timedelta
from users.user_add import Users
import calendar


def calendar_keyboard(user: Users, dates: date = None) -> InlineKeyboardMarkup:
    """
    Функция создаёт календарь
    параметры помогают вывести актуальную дату и установить нужный язык
    :param user: для установки языка и проверки даты заезда-выезда
    :param dates: получает актуальную дату
    :return: календарь
    """
    if user.check_in is not None:
        date_point = user.check_in + timedelta(days=1)
    else:
        date_point = date.today()
    keyboard = InlineKeyboardMarkup(row_width=7)

    if dates < date_point and dates.month != date_point.month:
        new_year = dates.year + 1
        dates = date(new_year, dates.month, dates.day)

    first_row_button(keyboard, user, dates)
    second_row_button(keyboard, user, dates)
    third_row_button(keyboard, date_point, dates)
    fourth_row_button(keyboard, date_point, dates)

    return keyboard


def first_row_button(keyboard: InlineKeyboardMarkup, user: Users, dates: date) -> None:
    """
    Устанавливает первый ряд календаря в виде (месяц, год)
    :param keyboard: клавиатура
    :param user: для установки языка
    :param dates: актуальная дата
    :return: None
    """
    keyboard.add(InlineKeyboardButton(
            bot_mess[user.language]['months'][dates.month - 1] + " " + str(dates.year),
            callback_data=f'SET-MONTH:{dates.year}:{dates.month}:{dates.day}'))


def second_row_button(keyboard: InlineKeyboardMarkup, user: Users, dates: date) -> None:
    """
    Устанавливает второй ряд кнопок со днями недели в виде (пн, вт, ср, чт, пт, сб, вс)
    :param keyboard: клавиатура
    :param user: для установки языка
    :param dates: актуальная дата
    :return: None
    """
    keyboard.add(*[InlineKeyboardButton(week_day, callback_data=f'IGNORE:{dates.year}:{dates.month}:{dates.day}')
                   for week_day in bot_mess[user.language]['week_days']])


def third_row_button(keyboard: InlineKeyboardMarkup, date_point: date, dates: date) -> None:
    """
    Устанавливает кнопки с числами
    :param keyboard: клавиатура
    :param date_point: опорная дата, календарь не может отображать даты до даты в date_point
    :param dates: актуальная дата
    :return: None
    """
    for week in calendar.monthcalendar(dates.year, dates.month):
        row = list()
        for day in week:
            if dates.year == date_point.year and dates.month == date_point.month:
                if day < date_point.day:
                    day = 0
            if day == 0:
                row.append(InlineKeyboardButton(" ", callback_data=f"IGNORE:{dates.year}:{dates.month}:{dates.day}"))
            else:
                row.append(InlineKeyboardButton(str(day),
                                                callback_data=f'SET-DAY:{dates.year}:{dates.month}:{day}'))
        keyboard.add(*row)


def fourth_row_button(keyboard: InlineKeyboardMarkup, date_point: date, dates: date) -> None:
    """
    Устанавливает кнопки в виде((<) (>)) для итерации календаре по месяцам
    :param keyboard: клавиатура
    :param date_point: опорная дата, календарь не может отображать даты до даты в date_point
    :param dates: актуальная дата
    :return: None
    """
    if dates.year == date_point.year and dates.month == date_point.month:
        keyboard.add(InlineKeyboardButton(">", callback_data=f"NEXT-MONTH:{dates.year}:{dates.month}:{dates.day}"))
    else:
        keyboard.add(InlineKeyboardButton("<",
                                          callback_data=f"PREVIOUS-MONTH:{dates.year}:{dates.month}:{dates.day}"),
                     InlineKeyboardButton(">", callback_data=f"NEXT-MONTH:{dates.year}:{dates.month}:{dates.day}"))
