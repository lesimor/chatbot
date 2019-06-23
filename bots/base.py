# Code by ByungWook.Kang @lesimor
import abc


class Bot(metaclass=abc.ABCMeta):
    def __init__(self):
        pass

    @abc.abstractmethod
    def response(self, text) -> str:
        return ''
