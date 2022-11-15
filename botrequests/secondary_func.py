from typing import Dict, List
from requests import Response
from botrequests import receiving_requests
from botrequests.search_param import hotel_search_param
from users.user_add import Users
from datetime import datetime
from loguru import logger
import json
import re


def compile_hotel(data: dict, user: Users) -> List:
    """
    Функция соберёт ответ для пользователя из словаря с отелями, с нужными параметрами
    :param data: словарь с отелями
    :param user: для получения параметров (кол-во фотографий, даты заезда-выезда)
    :return: вернёт ответ в виде обработанного словаря
    """
    hotels_list = [
        {'hotel_id': hotel.get('id', '-'),
         'name': hotel.get('name', '-'),

         'address': '{countryName} {locality} {streetAddress}'.format
         (countryName=hotel['address'].get('countryName'),
          locality=hotel['address'].get('locality'),
          streetAddress=hotel['address'].get('streetAddress')) if hotel.get('address') else '-',

         'landmarks': '{landmarks} - {distance}'.format
         (landmarks=hotel['landmarks'][0].get('label'),
          distance=hotel['landmarks'][0].get('distance')) if hotel.get('landmarks') else '-',

         'price': hotel['ratePlan']['price'].get('current') if hotel.get('ratePlan') else '-',

         'total_price': "{tot_pr} {curr}".format(tot_pr=price_per_stay(
             check_in=user.check_in, check_out=user.check_out,
             price=hotel['ratePlan']['price'].get('current')), curr=user.currency) if hotel.get('ratePlan') else '-',

         'hotel_link': 'https://hotels.com/ho' + str(hotel.get('id')),

         'photo': receiving_requests.get_photos
         (hotel_id=hotel.get('id'), photo_amount=user.photo_amount) if user.photo_needed else None}
        for hotel in data['results']]
    return hotels_list


def sort(data: dict, user: Users, response: Response, hotel_list: list = None) -> List:
    """
    Функция используется при установке команды <bestdeal>.
    Функция отсортировывает все полученные отели от API по дистанции.
    В случае если список не == требуемому кол-ву отелей.
    Вызывается следующая страница результата API, если такая имеется.
    :param data: словарь с отелями
    :param user: параметры пользователя
    :param response: ответ от API
    :param hotel_list: список с отелями требуется при рекурсии функции
    :return: список с отелями
    """
    if hotel_list is None:
        hotel_list = []
    dist_min = min(user.dist_range)
    dist_max = max(user.dist_range)

    for i in data['results']:
        try:
            b = (i.get('landmarks')[0])
            if dist_min <= float(b["distance"].strip().replace(',', '.').split()[0]) <= dist_max:
                hotel_list.append(i)
            if len(hotel_list) == int(user.hotel_amount):
                break
        except KeyError as e:
            logger.warning(f'Not found key: {e} in {i}')
    if len(hotel_list) < int(user.hotel_amount):
        next_page = get_next_page(user, response)
        if next_page:
            data = pattern_finder(patt=r'(?:\"results\".+)(?:\}{2}\])', resp=next_page)
            if data:
                sort(data, user, response=next_page, hotel_list=hotel_list)
    return hotel_list


def get_next_page(user: Users, resp: Response) -> Response:
    """
    Функция проверяет наличие следующей страницы в API запросе, отправляет запрос в случае успеха
    :param user: параметры пользователя для формирования параметров запроса к API
    :param resp: результат полученный от API
    :return: результат полученный от API
    """
    pattern = r'(?:\"pagination\").+?[\}]'
    find = re.search(pattern, resp.text)
    if find:
        data = json.loads(f"{{{find[0]}}}")
        current_page = int(data['pagination'].get('currentPage', '1'))
        next_page = int(data['pagination'].get('nextPageNumber', '1'))
        if current_page < next_page:
            resp = hotel_search_param(user=user, page=str(next_page))
            return resp


def pattern_finder(patt: str, resp: Response) -> Dict:
    """
    Функция проверяет наличи ключа в результате от API при помощи регулярного выражения
    :param patt: регулярное выражение
    :param resp: ответ от API
    :return: словарь с отелями
    """
    find = re.search(patt, resp.text)
    if find:
        data = json.loads(f"{{{find[0]}}}")
        return data


def price_per_stay(check_in: datetime, check_out: datetime, price: str) -> str:
    """
    Подсчёт общей стоимости за время проживания
    :param check_in: дата заезда
    :param check_out: дата выезда
    :param price: цена за ночь
    :return:
    """
    residence_time = check_out - check_in
    re_price = re.search(r'(?:\d{1,3},)*\d{1,3}', price)
    price_day = re_price.group(0).replace(',', '')
    total_price_str = str(int(price_day) * residence_time.days)
    formatted_price = f'{int(total_price_str):,}'.replace(',', '.')
    return formatted_price
