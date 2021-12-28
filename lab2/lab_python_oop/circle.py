from .geomFigure import GeomFigure
from .color import Color
from math import pi

class Circle(GeomFigure):
    def __init__(self,radius,color):
        self._radius = radius
        self._color = Color(color)

    def square(self):
        return pi * self._radius**2

    def __repr__(self):
        return 'Круг с радиусом:' + str(self._radius) + '.Цвет:'+str(self._color._color)
