# Code by ByungWook.Kang @lesimor
from bots.base import Bot


class EchoBot(Bot):
    def response(self, text):
        return text
