from lab_python_oop.circle import Circle
from lab_python_oop.rectangle import Rectangle
from lab_python_oop.square import Square

def main():
    rectangle = Rectangle(5, 4, 'Синий')
    circle = Circle(5, 'Зелёный')
    square = Square(5, 'Красный')
    
    print('{0!r}'.format(rectangle))
    print('{0!r}'.format(circle))
    print('{0!r}'.format(square))

if __name__ == "__main__":
    main()
