from typing import Optional, Any
from loguru import logger


class Users:
    """Класс Users установка параметров пользователя

        Основное применение - установки параметров поиска и языка

    Attributes:

        user_id (int): уникальный номер пользователя в телеграмм
        commands (str): команда пользователя (lowprice, basedeal либо highprice)
        city (str): id города
        check_in (class 'datetime.date'): дата заезда
        check_out (class 'datetime.date'): дата выезда
        hotel_amount (str): кол-во отелей
        photo_needed (class 'bool'): требуются ли фотографии
        photo_amount (str): кол-во фотографий
        price_range (list): диапазон цен
        dist_range (list): диапазон дистанции от центра города
        language (str): язык пользователя, по умолчанию русский
        currency (str): валюта, по умолчанию рубли
        mess_list (list): временно хранение id сообщений истории поиска отправленные пользователю
            (нужно для скрытия истории в телеграмм)
        """
    __all_user = dict()

    def __init__(self, user_id: int) -> None:
        self.user_id = user_id
        self.commands = None
        self.city = None
        self.check_in = None
        self.check_out = None
        self.hotel_amount = None
        self.photo_needed = False
        self.photo_amount = None
        self.price_range = None
        self.dist_range = None
        self.language = 'ru_RU'
        self.currency = 'RUB'
        self.add_user(user_id, self)
        self.mess_list = []

    def __str__(self) -> str:
        """
        Вывод инициализатора класса User/
        :return: выводит описание пользователя
        """
        return f"ID: {self.user_id}\ncommands: {self.commands}" \
               f"\ncity: {self.city}\ncheck_in: {self.check_in}" \
               f"\ncheck_out: {self.check_out}\nhotel_amount: {self.hotel_amount}" \
               f"\nphoto_needed: {self.photo_needed}\nphoto_amount: {self.photo_amount}" \
               f"\nprice_range: {self.price_range}\ndist_range: {self.dist_range}" \
               f"\nlanguage: {self.language}\ncurrency: {self.currency}"

    @classmethod
    def add_user(cls, user_id: int, user: Any) -> None:
        """
        Добавление пользователя в словарь
        :param user_id: id пользователя
        :param user: экземпляр класса Users
        :return: None
        """
        cls.__all_user[user_id] = user
        logger.info(f'Add a new user {user_id}')

    @staticmethod
    def get_user(user_id: int) -> Optional:
        """
        Функция для передачи пользователя из словаря и проверки его налия,
        в случае отсутствия вернёт нового пользователя.
        :param user_id: id пользователя.
        :return: возвращает объект класса Users
        """
        all_users = Users.__all_user
        if all_users.get(user_id) is None:
            new_user = Users(user_id)
            return new_user
        return all_users.get(user_id)

    def user_param_reset(self) -> None:
        """Используется для сброса параметров пользователя при выборе новой команды"""
        self.commands = None
        self.city = None
        self.check_in = None
        self.check_out = None
        self.hotel_amount = None
        self.photo_needed = False
        self.photo_amount = None
        self.price_range = None
        self.dist_range = None
        self.mess_list = []

    def get_order(self) -> str:
        """
        Передача параметра сортировки в функцию осуществляющая запрос к API
        :return: команду для сортировки
        """
        if self.commands == 'lowprice':
            return 'PRICE'
        elif self.commands == 'highprice':
            return 'PRICE_HIGHEST_FIRST'
        elif self.commands == 'bestdeal':
            return 'DISTANCE_FROM_LANDMARK'
