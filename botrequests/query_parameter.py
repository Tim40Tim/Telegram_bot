from typing import Dict
from botrequests.api_limit import limit_control
import requests
import os


headers = {'X-RapidAPI-Key': os.getenv('RAPID_API_KEY'),
           'X-RapidAPI-Host': os.getenv('RAPID_HOST')}


def api_result(url: str, querystring: dict) -> Dict or requests.models.Response:
    """
    Функция возвращает ответ от Апи запроса
    :param url: ссылка на запрос
    :param querystring: параметры запроса
    :return: ответ от Апи запроса или ошибку в виде словаря
    """
    try:
        response = requests.request(
            "GET", url=url, headers=headers, params=querystring, timeout=10
        )
    except requests.exceptions.RequestException:
        return {"error": "RequestException"}

    limit_control(response.headers)
    if response.status_code == 200:
        return response
    else:
        return {"error": f"Data retrieval error [{response.status_code}]\nHeaders: {response.headers}\n{response.text}"}
