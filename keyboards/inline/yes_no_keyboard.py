from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from message_sample.mess_dictionary import bot_mess


def photo_needed(lang) -> InlineKeyboardMarkup:
    """Запрос необходимости вывода фото в виде Inline клавиатуры"""
    keyboard = InlineKeyboardMarkup()
    [keyboard.add(InlineKeyboardButton(x, callback_data=x)) for x in
     [bot_mess[lang]['pos'], bot_mess[lang]['neg']]]
    return keyboard
