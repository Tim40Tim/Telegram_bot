from telebot.types import Message
from users.user_add import Users
from message_sample.mess_dictionary import bot_mess
from keyboards.reply.command_keyboard import request_command
from loader import bot


@bot.message_handler(commands=['start'])
def bot_start(message: Message):
    """
    Стартовое сообщение, создание трёх кнопок с основными коммандами
    :param message:
    :return:
    """
    user = Users.get_user(message.chat.id)
    bot.send_message(message.chat.id, bot_mess[user.language]['start_mess'], reply_markup=request_command())

