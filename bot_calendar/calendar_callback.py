from users.user_add import Users
from telebot.types import CallbackQuery, ReplyKeyboardRemove
from bot_calendar.calendar_actions import calendar_query_handler
from message_sample.mess_dictionary import bot_mess
from bot_calendar.set_calendar import calendar_keyboard
from handlers.custom_heandlers.basic_query_step import ask_for_dist_range, ask_for_hotels_value
from loguru import logger
from loader import bot


@bot.callback_query_handler(
    func=lambda call: call.data.startswith(('SET-MONTH', 'MONTH', 'IGNORE', 'SET-DAY', 'PREVIOUS-MONTH', 'NEXT-MONTH')))
def callback_inline(call: CallbackQuery) -> None:
    """
    Обработка inline callback запросов календаря
    :param call: запрос
    :return: None
    """
    action, year, month, day = call.data.split(':')
    date_answer = calendar_query_handler(call=call, action=action, year=year, month=month, day=day)
    user = Users.get_user(call.message.chat.id)

    if action == "SET-DAY" and user.check_in is None:
        user.check_in = date_answer
        logger.info(f'Set check_in: userID = {user.user_id} check_in = {user.check_in}')
        bot.send_message(
            chat_id=call.message.chat.id,
            text=bot_mess[user.language]['check_out'], reply_markup=calendar_keyboard(user=user, dates=user.check_in)
        )
    elif action == "SET-DAY" and user.check_in is not None:
        user.check_out = date_answer
        logger.info(f'Set check_out: userID = {user.user_id} check_out = {user.check_out}')
        if user.commands == 'bestdeal':
            mess = bot.send_message(
                chat_id=call.message.chat.id,
                text=bot_mess[user.language]['ask_dist'], reply_markup=ReplyKeyboardRemove())
            bot.register_next_step_handler(mess, ask_for_dist_range)
        else:
            mess = bot.send_message(
                chat_id=call.message.chat.id,
                text=bot_mess[user.language]['hotels_value'], reply_markup=ReplyKeyboardRemove())
            bot.register_next_step_handler(mess, ask_for_hotels_value)
