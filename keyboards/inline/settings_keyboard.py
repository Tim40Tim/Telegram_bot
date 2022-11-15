from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def setting_lang_keyboard() -> InlineKeyboardMarkup:
    """
    Клавиатура с выбором языка
    :return:
    """
    lang_keyboard = InlineKeyboardMarkup(row_width=2)
    lang_buttons = [InlineKeyboardButton(text=text, callback_data=param)
                    for text, param in (('RU', 'ru_RU'), ('EN', 'en_US'))]
    lang_keyboard.add(*lang_buttons)
    return lang_keyboard


def setting_curr_keyboard() -> InlineKeyboardMarkup:
    """
    Клавиатура с выбором валюты
    :return:
    """
    curr_keyboard = InlineKeyboardMarkup(row_width=3)
    curr_buttons = [InlineKeyboardButton(text=text, callback_data=text)
                    for text in ('RUB', 'USD', 'EUR')]
    curr_keyboard.add(*curr_buttons)
    return curr_keyboard
