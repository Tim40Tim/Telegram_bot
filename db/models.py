from peewee import (SqliteDatabase, Model, CharField, ForeignKeyField, DateTimeField,
                    TextField, DateField, IntegerField, BooleanField)
from playhouse.sqlite_ext import JSONField

db = SqliteDatabase('db/database.db')


class BaseModel(Model):
    """Базовый класс определяющий с какой базой данных работать"""
    class Meta:
        """Класс peewee определяет базу данных"""
        database = db


class User(BaseModel):
    """Класс создаёт колонку в ДБ с id пользователя из телеграмм"""
    chat_id = CharField(unique=True, null=False)

    class Meta:
        """Класс библиотеки peewee создающий таблицу users в database """
        db_table = 'users'


class Request(BaseModel):
    """
    Класс создающий колонки в ДБ с параметрами запроса пользователя.
    Класс создающий колонки:
         user - id юзера из телеграмм
         date - дата время запроса на поиск
         commands - команда запроса
         city - id города
         check_in - дата заезда
         check_out - дата выезда
         hotel_amount - кол-во отелей
         photo_needed - необходимость вывода фотографий
         photo_amount - кол-во фотографий
         price_range - диапазон цен
         dist_range - диапазон дистанции
         language - язык
         currency - валюта
         request_code - специальный, уникальный код для связки с базой найденных отелей.
            Состоит из id пользователя из телеграмм + дата и время запроса
    """
    user = ForeignKeyField(User, field=User.chat_id, backref='users')
    date = DateTimeField(formats='%Y-%m-%d %H:%M:%S')
    commands = CharField()
    city = TextField()
    check_in = DateField()
    check_out = DateField()
    hotel_amount = IntegerField()
    photo_needed = BooleanField()
    photo_amount = IntegerField()
    price_range = JSONField(null=True)
    dist_range = JSONField(null=True)
    language = CharField()
    currency = CharField()
    request_code = CharField(unique=True)

    class Meta:
        """Класс библиотеки peewee создающий таблицу requests в database """
        db_table = 'requests'


class History(BaseModel):
    """
    Класс создающий колонки в ДБ с найденными отелями.
    Класс создающий колонки:
        request - Внешний ключ, ссылка на объект в таблице requests
        hotel_id - id отеля
        name - название отеля
        address - адрес
        landmarks - центр города с расстоянием от отеля
        price - цена за сутки
        total_price - цена за пребывания учитывая дату заезда-выезда
        hotel_link - внешняя ссылка на отель
        photo - список со ссылками на фото отеля
    """
    request = ForeignKeyField(Request, field=Request.request_code, backref='histories')
    hotel_id = CharField()
    name = TextField()
    address = TextField()
    landmarks = TextField()
    price = TextField()
    total_price = TextField()
    hotel_link = TextField()
    photo = JSONField(null=True)

    class Meta:
        """Класс библиотеки peewee создающий таблицу histories в database """
        db_table = "histories"
