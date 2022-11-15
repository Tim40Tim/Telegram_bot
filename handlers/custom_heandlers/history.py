from telebot.types import Message
from db.history_act import get_history
from handlers.publishing_functions import history_publication
from users.user_add import Users
from loader import bot


@bot.message_handler(commands=['history'])
def bot_histories(message: Message) -> None:
    """
    Передача истории в функцию для публикации
    :param message:
    :return:
    """
    user = Users.get_user(message.chat.id)
    history = get_history(user_id=message.chat.id)
    history_publication(history=history, user=user, message=message)

