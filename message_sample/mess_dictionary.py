emoji = {'low': '\U00002198',
         'high': '\U00002197',
         'best': '\U00002705',
         'history': '\U0001F4D3',
         'hotel': '\U0001F3E8',
         'address': '\U0001F4CD',
         'price': '\U0001F4B0',
         'landmarks': '\U0001F3AF',
         'link': '\U0001F4CE',
         'settings': '\U0001F527',
         'finger_down': '\U0001F447',
         'ok': '\U0001F534'}

error_mess = {
    'ru_RU': {
        'date_error': 'Проверьте корректность данных:'
                      '\n1) Дата заезда не может быть прошедшей датой.'
                      '\n2) Дата выезда не может быть раньше даты заезда.',
        'photo_err': 'Необходимо ввести целое число (не больше 5):',
        'val_err': 'Необходимо ввести целое число (не больше 10):',
        'crt_err': 'Что-то пошло не так, перезагружаюсь...',
        'dist_err': 'Необходимо ввести два целых положительных отличных друг от друга числа:'
                    '\n(Например: "от 1 до 3" / "1-3" / "1 3")',
        'price_err': 'Необходимо ввести два целых положительных отличных друг от друга числа:'
                     '\n(Например: "от 1000 до 2000", "1000-2000", "1000 2000")',
        'fetch_error': "Ошибка получения данных, попробуйте позже.",
    },

    # =================================================================================================================

    'en_US': {
        'date_error': 'Check the correctness of the data:'
                      '\n1) Check-in date cannot be past date.'
                      '\n2) The check-out date cannot be earlier than the check-in date.',
        'photo_err': 'You must enter an integer (no more than 5):',
        'val_err': 'You must enter an integer (no more than 10):',
        'crt_err': 'Something went wrong, restart...',
        'dist_err': 'It is necessary to enter two positive integers that are different from each other:'
                    '\n(As example: "from 1 to 3" / "1-3" / "1 3"',
        'price_err': 'It is necessary to enter two positive integers that are different from each other:'
                     '\n(As example: "from 1000 to 2000", "1000-2000", "1000 2000")',
        'fetch_error': "Error fetching data, maybe later.",
    }
}

bot_mess = {
    'ru_RU': {
        'help_message': 'Помоги мне подобрать для тебя самое выгодное предложение (выбери команду): '
                        f'\n\n {emoji["low"]} /lowprice - Узнать топ самых дешёвых отелей в городе'
                        f'\n\n {emoji["high"]} /highprice - Узнать топ самых дорогих отелей в городе'
                        f'\n\n {emoji["best"]} /bestdeal - Узнать топ отелей, наиболее подходящих по цене '
                        f'и расположению от центра (самые дешёвые и находятся ближе всего к центру)'
                        f'\n\n {emoji["history"]} /history - Узнать историю поиска отелей'
                        f'\n\n {emoji["settings"]} /settings (по желанию) - Установить параметры поиска (язык, '
                        f'валюта)',
        'default_commands': {
            'start': "Запустить бота",
            'help': "Вывести справку",
            'settings': "Настройки",
            'lowprice': "Вывод самых дешёвых отелей в городе",
            'highprice': "Вывод самых дорогих отелей в городе",
            'bestdeal': "Вывод отелей, наиболее подходящих по цене и расположению от центра",
            'history': "История поиска"
        },
        f'start_mess': f'Выберите команду{emoji["finger_down"]}',
        'set_lang': 'Установить язык по умолчанию:',
        'set_cur': 'Установить валюту по умолчанию:',
        'search': 'Выполняю поиск...',
        'ask_for_city': 'Какой город Вас интересует?',
        'input_correctness': 'Проверьте корректность ввода',
        'check_in': 'Дата заезда',
        'check_out': 'Дата выезда',
        'date_choice': 'Вы выбрали - ',
        'hotels_value': 'Сколько объектов смотрим? (не более 10)',
        'photo_needed': 'Интересуют фотографии объектов?',
        'photos_amount': 'Сколько фотографий по каждому объекту (не более 5)?',
        'city_results': 'Предлагаю немного уточнить запрос:',
        'pos': 'Да',
        'neg': 'Нет',
        'ready_to_result': 'Я нашёл для тебя следующие варианты...',
        'main_results': "\n\n{e_ok}<b>{name}</b>"
                        "\n\n{e_ok}Адрес отеля: {address}"
                        "\n\n{e_ok}Расстояние до: {distance}"
                        "\n\n{e_ok}Цена за ночь: {price}"
                        "\n\n{e_ok}'Общая стоимость за время проживание: {total_price}"
                        "\n\n<a href='{address_link}'>Перейти на страницу отеля</a>",
        'additionally': 'Не нашли подходящий вариант?\nЕщё больше отелей по вашему запросу\\: [смотреть]({link})'
                        '\nХотите продолжить работу с ботом? /help',
        'ask_price': 'Уточните ценовой диапазон за сутки ({cur}):'
                     '\n(Например: "от 1000 до 2000", "1000-2000", "1000 2000")',
        'ask_dist': 'Уточните диапазон расстояния, на котором находится отель от центра (км):'
                    '\n(Например: "от 1 до 3" / "1-3" / "1 3")',
        'no_options': 'По вашему запросу ничего не найдено...\n/help',
        'operations_for_history': ('Удалить', 'Скрыть'),
        'clr_history': 'Ваша история поиска пуста!',
        'week_days': ("Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"),
        'months': ("Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь",
                   "Ноябрь", "Декабрь")
    },

    #  ==============================================================================================================

    'en_US': {
        'help_message': 'Help me find the best offer for you (choose a command): '
                        f'\n\n {emoji["low"]} /lowprice - Find out the top cheapest hotels in the city'
                        f'\n\n {emoji["high"]} /highprice - Find out the top most expensive hotels in the city'
                        f'\n\n {emoji["best"]} /bestdeal - Find out the top hotels most suitable for the price '
                        'and location from the center (the cheapest and are closest to the center)'
                        f'\n\n {emoji["history"]} /history - Find out the history of hotel search'
                        f'\n\n {emoji["settings"]} /settings (optional) - Set search parameters (language, currency)',
        'default_commands': (
            ('start', "Start bot"),
            ('help', "Get help"),
            ('settings', "Settings"),
            ('lowprice', "Conclusion of the cheapest hotels in the city"),
            ('high price', "Conclusion of the most expensive hotels in the city"),
            ('bestdeal', "Finding the most suitable hotels in terms of price and location from the center"),
            ('history', "Search history")
        ),
        f'start_mess': f'Select command{emoji["finger_down"]}',
        'set_lang': 'Set the default language:',
        'set_cur': 'Set the default currency:',
        'search': 'Searching...',
        'ask_for_city': 'Which city are you interested in?',
        'input_correctness': 'Check the correctness of the input',
        'check_in': 'Check-in date',
        'check_out': 'Check-out date',
        'date_choice': 'You have chosen - ',
        'hotels_value': 'How many hotels are we looking at? (no more than 10)',
        'photo_needed': 'Interested in photos of the object?',
        'photos_amount': 'How many photos for each object? (no 5 more)',
        'city_results': 'I propose to clarify the request:',
        'pos': 'Yes',
        'neg': 'No',
        'ready_to_result': 'I found the following options for you...',
        'main_results': "\n\n{e_ok}{name}"
                        "\n\n{e_ok}Hotel address: {address}"
                        "\n\n{e_ok}Distance to: {distance}"
                        "\n\n{e_ok}Price per night: {price}"
                        "\n\n{e_ok}Total cost per stay: {total_price}"
                        "\n\n<a href='{address_link}'>Go to hotel page</a>",
        'additionally': "Didn't find a suitable option?\nMore hotels on your request\\: [view]({link})"
                        "\nDo you want to continue working with the bot? /help",
        'ask_price': 'Check the price range per day ({cur}):'
                     '\n(As example: "from 50 to 100", "50-100", "50 100")',
        'ask_dist': 'Specify the range of the distance at which the hotel is located from the center (mile)'
                    '\n(As example: "from 1 to 3" / "1-3" / "1 3"',
        'no_options': 'Nothing was found for your query...\n/help',
        'operations_for_history': ('Delete', 'Hide'),
        'clr_history': 'Your search history is empty!',
        'week_days': ("Su", "Mo", "Tu", "We", "Th", "Fr", "Sa"),
        "months": ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                   "November", "December")
    }
}
