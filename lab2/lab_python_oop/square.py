from .rectangle import Rectangle
from .color import Color

class Square(Rectangle):
    def __init__(self, side, color):
        self._width = side
        self._height = side
        self._color = Color(color)

    def __repr__(self):
        return 'Квадрат со стороной:'+str(self._width) + '.Цвет: ' + str(self._color._color)