from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def cities_keyboard(city_dict: dict) -> InlineKeyboardMarkup:
    """
    Клавиатура с городами
    :param city_dict:
    :return:
    """
    city_keyboard = InlineKeyboardMarkup(row_width=1)
    city_buttons = [InlineKeyboardButton(text=city_name, callback_data=f'call data, {city_id}')
                    for city_name, city_id in city_dict.items()]
    city_keyboard.add(*city_buttons)
    return city_keyboard
