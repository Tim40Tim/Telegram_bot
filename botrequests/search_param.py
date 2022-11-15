from requests import Response
from botrequests.query_parameter import api_result
from users.user_add import Users


def city_search_param(user: Users, city_name: str) -> Response:
    """
    Функция устанавливает параметры для поиска города
    :param user: для передачи параметров языка и валюты пользователя
    :param city_name: название искомого города
    :return: вернёт результат запроса
    """
    querystring = {"query": city_name, "locale": user.language, "currency": user.currency}
    url = "https://hotels4.p.rapidapi.com/locations/v2/search"
    result = api_result(querystring=querystring, url=url)
    return result


def hotel_search_param(user: Users, page: str = '1') -> Response:
    """
    Функция устанавливает параметры для поиска отелей.
    :param user: для передачи параметров.
    :param page: страница для поиска.
    :return: вернёт результат запроса
    """
    querystring = {"destinationId": user.city, "pageNumber": page, "pageSize": user.hotel_amount,
                   "check_in": user.check_in, "check_out": user.check_out, "adults1": "1",
                   "locale": user.language, "currency": user.currency, "sortOrder": user.get_order()}
    url = 'https://hotels4.p.rapidapi.com/properties/list'
    if user.commands == 'bestdeal':
        querystring["priceMin"] = min(user.price_range)
        querystring["priceMax"] = max(user.price_range)
        querystring["pageNumber"] = page
        querystring["pageSize"] = "25"
    result = api_result(querystring=querystring, url=url)
    return result


def photo_search_param(hotel_id: int) -> Response:
    """
    Функция устанавливает параметры для поиска фотографий
    :param hotel_id: id отеля
    :return: вернёт результат запроса
    """
    querystring = {"id": hotel_id}
    url = "https://hotels4.p.rapidapi.com/properties/get-hotel-photos"
    result = api_result(querystring=querystring, url=url)
    return result
