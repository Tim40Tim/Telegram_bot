import functools
from db.models import *


def open_connect(func):
    """
    Декоратор связи с БД. Декорирует функции добавления информации в БД.
    :param func: Декорируемая функция
    :return: Обёртка
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if func.__name__ == "add_history":
            with db.atomic():
                func(*args, **kwargs)
        else:
            with db:
                func(*args, **kwargs)
    return wrapper
