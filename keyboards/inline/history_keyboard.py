from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from message_sample.mess_dictionary import bot_mess


def clear_history(lang) -> InlineKeyboardMarkup:
    """
    Клавиатура с городами
    :param lang:
    :param city_dict:
    :return:
    """
    keyword = InlineKeyboardMarkup(row_width=2)
    buttons = [InlineKeyboardButton(text=text, callback_data=text)
               for text in bot_mess[lang]['operations_for_history']]
    keyword.add(*buttons)
    return keyword
