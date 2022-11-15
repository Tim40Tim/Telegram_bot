from users.user_add import Users
from telebot.types import Message
from message_sample.mess_dictionary import bot_mess, error_mess
from keyboards.inline.city_keyboard import cities_keyboard
from keyboards.inline.yes_no_keyboard import photo_needed
from botrequests.receiving_requests import get_city, get_hotel
from handlers.publishing_functions import publication
from loguru import logger
from loader import bot
import re


@bot.message_handler(commands=['bestdeal', 'highprice', 'lowprice'])
def start_script(message: Message) -> None:
    """
    Запуск сценария вопросв по поиску отелей, регистрация следующего шага (запрос города).
    :param message:сообщение в телеграм.
    :return: None
    """
    user = Users.get_user(message.chat.id)
    if user.commands is not None:
        user.user_param_reset()
    user.commands = message.text.replace('/', '')
    logger.info(f'START set user_param\nSet commands: userID = {user.user_id}, param: {user.commands}')
    bot.send_message(message.chat.id, bot_mess[user.language]['ask_for_city'])
    bot.register_next_step_handler(message, ask_city)


def ask_city(message):
    """
    Регистрация ответа (запрос города), поиск города, создание инлайн клавиатуры в случае положительного сценария.
    :param message:сообщение в телеграм.
    :return:None
    """
    user = Users.get_user(message.chat.id)
    temp_mess = bot.send_message(message.chat.id, bot_mess[user.language]['search'])
    city_dict = get_city(city_name=message.text, user=user)
    if 'error' in city_dict:
        bot.edit_message_text(chat_id=message.chat.id, message_id=temp_mess.id,
                              text=error_mess[user.language]['fetch_error'])
        logger.warning(f'{city_dict}')
    elif len(city_dict) == 0:
        bot.edit_message_text(chat_id=message.chat.id, message_id=temp_mess.id,
                              text=bot_mess[user.language]['no_options'])
    else:
        bot.edit_message_text(chat_id=message.chat.id, message_id=temp_mess.id,
                              text=bot_mess[user.language]['city_results'], reply_markup=cities_keyboard(city_dict))


def ask_for_dist_range(message: Message) -> None:
    """
    Запрос дистанции от центра города, в случае успеха регистраци следующего шага (запрос цены)
    :param message:сообщение в телеграм.
    :return:None
    """
    user = Users.get_user(message.chat.id)
    dist_range = list(set(map(float, map(lambda string: string.replace(',', '.'),
                                         re.findall(r'\d+[.,]\d+|\d+', message.text)))))
    if len(dist_range) != 2:
        bot.send_message(chat_id=message.chat.id, text=error_mess[user.language]['dist_err'])
        bot.register_next_step_handler(message, ask_for_dist_range)
    else:
        user.dist_range = dist_range
        bot.send_message(chat_id=message.chat.id, text=bot_mess[user.language]['ask_price'].format(cur=user.currency))
        bot.register_next_step_handler(message, ask_for_price_range)


def ask_for_price_range(message: Message) -> None:
    """Запрос ценового диапазона у пользователя, определение следующего шага обработчика (кол-во отелей)"""
    user = Users.get_user(message.chat.id)
    price_range = list(set(map(int, map(lambda string: string.replace(',', '.'),
                                        re.findall(r'\d+[.,]\d+|\d+', message.text)))))
    if len(price_range) != 2:
        bot.send_message(chat_id=message.chat.id, text=error_mess[user.language]['price_err'])
        bot.register_next_step_handler(message, ask_for_price_range)
    else:
        user.price_range = price_range
        bot.send_message(chat_id=message.chat.id, text=bot_mess[user.language]['hotels_value'])
        bot.register_next_step_handler(message, ask_for_hotels_value)


def ask_for_hotels_value(message: Message) -> None:
    """
    Запрос кол-ва отелей, в случае успеха создадим клавиатуру для определения с необходимостью вывода фотографий.
    :param message:сообщение в телеграм.
    :return:None
    """
    user = Users.get_user(message.chat.id)
    amount = re.search(r'\d+', message.text)
    if amount is None\
            or 0 == int(amount[0]) \
            or 10 < int(amount[0]):
        bot.send_message(chat_id=message.chat.id, text=error_mess[user.language]['val_err'])
        bot.register_next_step_handler(message, ask_for_hotels_value)
    else:
        user.hotel_amount = amount[0]
        bot.send_message(chat_id=message.chat.id, text=bot_mess[user.language]['photo_needed'],
                         reply_markup=photo_needed(user.language))


def number_of_photo(message: Message) -> None:
    """
    Установка кол-ва выводимых фотографий, в случае положительно ответа на необходимость их вывода.
    :param message:сообщение в телеграм.
    :return:None
    """
    user = Users.get_user(message.chat.id)
    amount = re.search(r'\d', message.text)
    if amount is None\
            or 0 == int(amount[0]) \
            or 5 < int(amount[0]):
        bot.send_message(chat_id=message.chat.id, text=error_mess[user.language]['photo_err'])
        bot.register_next_step_handler(message, number_of_photo)
    else:
        user.photo_amount = amount[0]
        logger.info(f'END set user_param {user}')
        result(message)


def result(message: Message) -> None:
    """
    Запускается процесс поиска отелей по параметрам полученных от пользователя, передача в публикацию.
    :param message: сообщение в телеграм.
    :return:None
    """
    user = Users.get_user(message.chat.id)
    temp = bot.send_message(chat_id=message.chat.id, text=bot_mess[user.language]['search'])
    hotels_lst = get_hotel(user=user)
    publication(hotels_lst, user, temp)
