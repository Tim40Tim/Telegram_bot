from telebot.types import CallbackQuery
from message_sample.mess_dictionary import bot_mess
from users.user_add import Users
from handlers.custom_heandlers.basic_query_step import number_of_photo, result
from loguru import logger
from loader import bot


@bot.callback_query_handler(
    func=lambda call: call.data in [keys for key in bot_mess.values() for keys in [key['pos'], key['neg']]])
def set_photo_needed(call: CallbackQuery) -> None:
    """Обработка ответа пользователя о необходимости вывода фото, определение хода действий."""
    user = Users.get_user(call.message.chat.id)
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.id)
    if call.data in [keys for key in bot_mess.values() for keys in [key['pos']]]:
        user.photo_needed = True
        logger.info(f'Set photo_needed: userID = {user.user_id}, param: {call.data}')
        mess = bot.send_message(chat_id=call.message.chat.id,
                                text=bot_mess[user.language]['photos_amount'])
        bot.register_next_step_handler(mess, number_of_photo)
    else:
        logger.info(f'END set user_param {user}')
        result(call.message)
