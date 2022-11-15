from typing import Dict, List
from requests import Response
from users.user_add import Users
from botrequests.search_param import city_search_param, hotel_search_param, photo_search_param
from botrequests.secondary_func import sort, compile_hotel
import json
import re


def get_city(city_name: str, user: Users) -> Dict or Response:
    """
    Функция для поиска города.
    :param city_name: Название искомого города.
    :param user: для передачи параметров пользователя в параметры запроса.
    :return: словарь с ошибкой или с результатом полученный от апи
    """
    resp = city_search_param(user=user, city_name=city_name)
    if 'error' in resp:
        return resp
    pattern = r'(?<="CITY_GROUP",).+?[\]]'
    find = re.search(pattern, resp.text)
    if find:
        data = json.loads(f"{{{find[0]}}}")
        try:
            cities_dict = {
                re.sub('<([^<>]*)>', '', city.get('caption')): city.get('destinationId')
                for city in data['entities']}
            return cities_dict
        except (TypeError, KeyError) as e:
            return {"error": f"Key {e} not found in {get_city.__name__}"}
    else:
        return {"error": f"Pattern <{pattern}> not found"}


def get_hotel(user: Users, resp: Response = None) -> Dict or Response:
    """
    Функция для поиска отелей.
    :param resp: ответ от Api
    :param user: для передачи параметров пользователя в параметры запроса
    :return: словарь с ошибкой или с результатом полученный от апи
    """
    if resp is None:
        resp = hotel_search_param(user=user)
    if 'error' in resp:
        return resp
    pattern = r'(?:\"results\".+)(?:\}{2}\])'
    find = re.search(pattern, resp.text)
    if find:
        data = json.loads(f"{{{find[0]}}}")
        if user.commands == 'bestdeal':
            hotels = sort(data, user, response=resp)
            data['results'] = hotels
        hotels_list = compile_hotel(data, user)
        return hotels_list
    else:
        return []


def get_photos(hotel_id: int, photo_amount: str) -> List or Dict:
    """
    Функция для получения фотографий
    :param hotel_id: id отеля
    :param photo_amount: необходимое кол-во фотографий
    :return: вернёт список с фотографиями или словарь с ошибкой
    """
    if isinstance(hotel_id, int):
        resp = photo_search_param(hotel_id=hotel_id)
        if 'error' in resp:
            return resp
        try:
            photo_data = json.loads(resp.text)
            photos_address = photo_data["hotelImages"][:int(photo_amount)]
            photo = [i['baseUrl'].format(size='w') for i in photos_address]
            return photo
        except KeyError as e:
            return {"error": f"key {e} not found"}
