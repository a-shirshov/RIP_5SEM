from .geomFigure import GeomFigure
from .color import Color

class Rectangle(GeomFigure):
    def __init__(self,width,height,color):
        self._width = width
        self._height = height
        self._color = Color(color) 
    
    def square(self):
        return self._width * self._height

    def __repr__(self):
        return 'Прямоугольник с высотой:'+str(self._height) + '.Шириной:'+str(self._width) + '.Цвет:' + str(self._color._color)
