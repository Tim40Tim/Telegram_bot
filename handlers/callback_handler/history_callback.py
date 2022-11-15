from telebot.types import CallbackQuery
from message_sample.mess_dictionary import bot_mess
from users.user_add import Users
from db.history_act import del_history
from loader import bot


@bot.callback_query_handler(
    func=lambda call: call.data in [keys for key in bot_mess.values() for keys in key['operations_for_history']])
def operation_for_history(call: CallbackQuery) -> None:
    """Обработка сообщений истории поиска (скрыть, очистить)"""
    user = Users.get_user(call.message.chat.id)
    if call.data in [keys[0] for key in bot_mess.values()
                     for keys in key.values() if keys == key['operations_for_history']]:
        del_history(call.message.chat.id)
    for i_message_id in user.mess_list:
        bot.delete_message(chat_id=call.message.chat.id, message_id=int(i_message_id))
    user.mess_list = []
