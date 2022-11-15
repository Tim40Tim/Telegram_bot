from datetime import date, timedelta
from typing import Any
from bot_calendar.set_calendar import calendar_keyboard
from bot_calendar.months_calendar import create_months_calendar
from users.user_add import Users
from telebot.types import CallbackQuery
from loader import bot


def jumpUP_date(source_date: date) -> date:
    """
    Функция изменит календарь с текущего месяца на следующий

    :param source_date: выставленная дата (год, месяц)
    :return: следующую дату (год, месяц)
    """
    month = source_date.month
    year = int(source_date.year + month / 12)
    month = month % 12 + 1
    return date(year, month, 1)


def jumpDOUN_date(source_date: date) -> date:
    """
    Функция изменит календарь с текущего месяца на предыдущий

    :param source_date: выставленная дата (год, месяц)
    :return: предыдущую дату (год, месяц)
    """
    return date(source_date.year, source_date.month, 1) - timedelta(days=1)


def calendar_query_handler(call: CallbackQuery, action: str, year: str, month: str, day: str) -> Any:
    """
    Задача функции обработать команду полученную от кнопок календаря
    Функция выполняет либо игнорирует действия с календарём в зависимости от полученной команды
    Вернёт дату в случае <команда == "УСТАНОВИТЬ ДАТУ"
    Проигнорирует нажатие кнопки в календаре в случае <команда == "ИГНОРИРОВАТЬ">
    В остальных командах запускается процесс изменения календаря
    :param call: Запрос содержащий параметры ниже
    :param action: Команда
    :param year: год
    :param month: месяц
    :param day: день
    :return: <class_date> or none or False with none
    """
    user = Users.get_user(call.message.chat.id)
    current = date(int(year), int(month), 1)

    if action == "IGNORE":
        bot.answer_callback_query(callback_query_id=call.id)
        return False, None

    elif action == "SET-DAY":
        bot.delete_message(
            chat_id=call.message.chat.id, message_id=call.message.message_id)
        return date(int(year), int(month), int(day))

    elif action == "PREVIOUS-MONTH":
        preview_month = jumpDOUN_date(current)
        bot.edit_message_text(
            text=call.message.text,
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            reply_markup=calendar_keyboard(user=user, dates=preview_month))
        return None

    elif action == "NEXT-MONTH":
        next_month = jumpUP_date(current)
        bot.edit_message_text(
            text=call.message.text,
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            reply_markup=calendar_keyboard(user=user, dates=next_month))
        return None

    elif action == "SET-MONTH":
        bot.edit_message_text(
            text=call.message.text,
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            reply_markup=create_months_calendar(user=user, dates=current),
        )
        return None

    elif action == "MONTH":
        bot.edit_message_text(
            text=call.message.text,
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            reply_markup=calendar_keyboard(user=user, dates=current))
        return None
