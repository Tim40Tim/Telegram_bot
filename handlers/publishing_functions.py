from users.user_add import Users
from telebot.types import Message, InputMediaPhoto
from message_sample.mess_dictionary import bot_mess, emoji, error_mess
from keyboards.inline.history_keyboard import clear_history
from db.create import add_in_db
from loguru import logger
from loader import bot


def history_publication(history: list, user: Users, message: Message) -> None:
    """
    Функция отвечает за вывод истории
    :param history: история поиска (отелей) в виде списка с датой запроса и командой
    :param user: пользователь
    :param message: Сообщений телеграм
    :return: None
    """
    if history:
        for mess in history:
            if not isinstance(mess, list):
                comm_and_date = bot.send_message(chat_id=message.chat.id, text=f'{mess}')
                user.mess_list.append(comm_and_date.id)
            elif isinstance(mess, list):
                publication_constructor(hotels_lst=mess, user=user, message=message, history_flag=True)
        bot.edit_message_reply_markup(chat_id=message.chat.id, message_id=int(user.mess_list[-1]),
                                      reply_markup=clear_history(user.language))
    else:
        bot.send_message(chat_id=message.chat.id,
                         text=bot_mess[user.language]['clr_history'])


def publication(hotels_lst: list, user: Users, message: Message) -> None:
    """
    Вывод результатов пользователю полученных от API.
    :param hotels_lst: Список отелей
    :param user: Пользователь
    :param message: Сообщение телеграм
    :return: None
    """
    if 'error' in hotels_lst:
        bot.edit_message_text(chat_id=message.chat.id, message_id=message.id,
                              text=error_mess[user.language]['fetch_error'])
        logger.warning(f'{hotels_lst}')
    elif hotels_lst:
        bot.edit_message_text(chat_id=message.chat.id, message_id=message.id,
                              text=bot_mess[user.language]['ready_to_result'])
        publication_constructor(hotels_lst, user, message)
        add_in_db(us=user, hotels=hotels_lst)
    else:
        bot.edit_message_text(chat_id=message.chat.id, message_id=message.id,
                              text=bot_mess[user.language]['no_options'])


def publication_constructor(hotels_lst: list, user: Users, message: Message, history_flag: bool = False):
    """
    Собирает сообщение для пользователя фильтруя не нужные элементы например: id отеля
    :param hotels_lst: Список отелей
    :param user: Пользователь
    :param message: Сообщение
    :param history_flag: history_flag: флаг включается если передаётся история. В этом случае будут
        сохранятся все id сообщений для дальнейшего скрытия или удаления
    :return: None
    """
    for hotel in hotels_lst:
        if isinstance(hotel['photo'], list):
            photo_group = [InputMediaPhoto(elem) for elem in hotel['photo']]
            temp_photo = bot.send_media_group(message.chat.id, photo_group)
            if history_flag:
                user.mess_list.extend([photos_id.id for photos_id in temp_photo])
        result_mess = bot_mess[user.language]['main_results'].format(name=hotel['name'],
                                                                     address=hotel['address'],
                                                                     distance=hotel['landmarks'],
                                                                     price=hotel['price'],
                                                                     total_price=hotel['total_price'],
                                                                     e_ok=emoji['ok'],
                                                                     address_link=hotel['hotel_link'])
        temp = bot.send_message(message.chat.id, result_mess, parse_mode='HTML', disable_web_page_preview=True)
        user.mess_list.append(temp.id)
