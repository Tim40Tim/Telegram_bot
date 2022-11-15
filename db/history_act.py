from typing import List
from db.models import *


def get_history(user_id=int) -> List:
    """
    Функция создаёт список отелей и добавляет туда команду и время запроса,
        далее отправляет список в публикацию.
    :param user_id: id пользователя.
    :return: Список отелей
    """
    query = Request.select().where(Request.user == user_id).prefetch(History)
    hotel_lst = []
    for elem in query:
        hotel_lst.append(elem.commands)
        hotel_lst.append(elem.date)
        hotel_lst.append([e.__data__ for e in elem.histories])
    return hotel_lst


def del_history(user_id: int) -> None:
    """
    Удаление истории пользователя (из таблицы параметров и из таблицы найденных отелей).
    :param user_id: id пользователя.
    :return:None
    """
    with db:
        query = History.delete().where(History.request.startswith(str(user_id)))
        query.execute()
        query = Request.delete().where(Request.user == user_id)
        query.execute()
