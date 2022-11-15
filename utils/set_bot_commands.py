from telebot.types import BotCommand
from config_data.config import DEFAULT_COMMANDS


def set_default_commands(bot):
    """
    Меню бота в виде кнопки
    :param bot: Бот
    :return:
    """
    bot.set_my_commands(
        [BotCommand(command=com, description=des) for com, des in DEFAULT_COMMANDS.items()]
    )
