from Bots.Bot import Bot
from DAO import DAO


class BotDAO(DAO):
    def __init__(self):
        super().__init__('Bots.pkl')

    def add(self, bot: Bot):
        if (isinstance(bot.nome, str)) and (bot is not None) and isinstance(bot, Bot):
            super().add(bot.nome, bot)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key: str):
        if isinstance(key, str):
            return super().remove(key)
