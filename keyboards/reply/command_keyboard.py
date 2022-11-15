from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def request_command() -> ReplyKeyboardMarkup:
    """
    Клавиатура с тремя основными коммандами бота
    :return:
    """
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    but1 = KeyboardButton(text='/lowprice')
    but2 = KeyboardButton(text='/highprice')
    but3 = KeyboardButton(text='/bestdeal')
    keyboard.add(but1, but2, but3)
    return keyboard
