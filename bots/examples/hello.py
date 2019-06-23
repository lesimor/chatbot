# Code by ByungWook.Kang @lesimor
from bots.base import Bot


class HelloBot(Bot):
    def response(self, text):
        return '안녕'
