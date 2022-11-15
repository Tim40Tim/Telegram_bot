from oll_decorator.decorators import open_connect
from users.user_add import Users
from peewee import IntegrityError
from datetime import datetime
from db.models import *

tables = [User, Request, History]
if not all(i.table_exists() for i in tables):
    db.create_tables(tables)


@open_connect
def add_in_db(us: Users, hotels: list) -> None:
    """
    Добавление пользователя в ДБ.
    :param us: Юзер
    :param hotels: Список отелей
    :return:None
    """
    try:
        User.create(
            chat_id=us.user_id,
        )
    except IntegrityError:
        pass
    add_req(us, hotels)


@open_connect
def add_req(us: Users, hotels: list) -> None:
    """
    Добавление параметров поиска в ДБ
    :param us: Юзер
    :param hotels: Отели
    :return:None
    """
    date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    Request.create(
        user=us.user_id,
        commands=us.commands,
        date=date,
        city=us.city,
        check_in=us.check_in,
        check_out=us.check_out,
        hotel_amount=us.hotel_amount,
        photo_needed=us.photo_needed,
        photo_amount=us.hotel_amount,
        price_range=us.price_range,
        dist_range=us.dist_range,
        language=us.language,
        currency=us.currency,
        request_code=f"{us.user_id}+{date}".replace(' ', '')
    )
    add_history(us, hotels, date)


@open_connect
def add_history(us: Users, hotels: list, date: str) -> None:
    """
    Добавление истории поиска (отелей) в ДБ
    :param us: Юзер
    :param hotels: Отели
    :param date: Дата
    :return:None
    """
    for hotel in hotels:
        hotel['request'] = f"{us.user_id}+{date}".replace(' ', '')
    query = History.insert_many(hotels)
    query.execute()
