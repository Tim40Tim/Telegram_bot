from telebot.types import Message
from message_sample.mess_dictionary import bot_mess
from users.user_add import Users
from loader import bot


@bot.message_handler(commands=['help'])
def bot_help(message: Message):
    """
    Вывод команд с описанием
    :param message:
    :return:
    """
    user = Users.get_user(message.chat.id)
    bot.reply_to(message, text=bot_mess[user.language]['help_message'])
