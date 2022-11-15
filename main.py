from loguru import logger
from utils.misc.log_configurate import logger_config
from utils.set_bot_commands import set_default_commands
from loader import bot
import handlers


logger.configure(**logger_config)


if __name__ == '__main__':
    try:
        set_default_commands(bot)
        bot.polling(none_stop=True, interval=0)
    except Exception as e:
        logger.opt(exception=True).error(f'Unexpected error: {e}')
