import os
from message_sample.mess_dictionary import bot_mess
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit('Переменные окружения не загружены т.к отсутствует файл .env')
else:
    load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
RAPID_API_KEY = os.getenv('RAPID_API_KEY')
RAPID_HOST = os.getenv('RAPID_HOST')
DEFAULT_COMMANDS = bot_mess['ru_RU']['default_commands']
