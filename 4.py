import math


class GeometricObject:
    '''
    A class representing a geometric object with coordinates, color, and fill properties.

    Attributes:
        __x (float): The x-coordinate of the geometric object.
        __y (float): The y-coordinate of the geometric object.
        color (str): The color of the geometric object.
        fill (bool): A boolean indicating whether the geometric object is filled.
    '''
    def __init__(self, x=None, y=None, ptr=None, filled=None):
        '''
        Initialize a GeometricObject with optional parameters.

        Args:
            x (float): The x-coordinate of the geometric object.
            y (float): The y-coordinate of the geometric object.
            ptr (str): The color of the geometric object.
            filled (bool): A boolean indicating whether the geometric object is filled.
        '''
        if x is not None:
            self.__x = float(x)
        else:
            self.__x = 0.0
        if y is not None:
            self.__y = float(y)
        else:
            self.__y = 0.0
        if ptr is not None:
            self.color = ptr
        else:
            self.color = 'black'
        if filled is not None:
            self.fill = True
        else:
            self.fill = False

    def __str__(self):
        return (f'({self.__x},{self.__y}){'\n'}'
                f'color: {self.color}{'\n'}'
                f'filled: {self.fill}')

    def __repr__(self):
        if self.fill is True:
            return str(f'({int(self.__x)},{int(self.__y)}) {self.color} filled')
        return str(f'({int(self.__x)},{int(self.__y)}) {self.color} no filled')

    def set_coordinate(self, new_x, new_y):
        '''
        Set the coordinates of the geometric object.

        Args:
            new_x (float): The new x-coordinate of the geometric object.
            new_y (float): The new y-coordinate of the geometric object.
        '''
        self.__x = float(new_x)
        self.__y = float(new_y)

    def set_color(self, ptr):
        '''
        Set the color of the geometric object.

        Args:
            ptr (str): The new color of the geometric object.
        '''
        self.color = ptr

    def set_filled(self, new_filled):
        '''
        Set the fill property of the geometric object.

        Args:
            new_filled (bool): A boolean indicating whether the geometric object is filled.
        '''
        self.fill = new_filled

    def get_x(self):
        '''
        Get the x-coordinate of the geometric object.

        Returns:
            float: The x-coordinate of the geometric object.
        '''
        return self.__x

    def get_y(self):
        '''
         Get the y-coordinate of the geometric object.

        Returns:
            float: The y-coordinate of the geometric object.
        '''
        return self.__y

    def get_color(self):
        '''
        Get the color of the geometric object.

        Returns:
            str: The color of the geometric object.
        '''
        return self.color

    def is_filled(self):
        '''
        Check if the geometric object is filled.

        Returns:
            bool: True if the object is filled, False otherwise.'''
        return self.fill


class Circle(GeometricObject):
    '''
    A class representing a circle with a radius.

    Attributes:
        _radius (float): The radius of the circle.
    '''
    def __init__(self, x=None, y=None, radius=None, ptr=None, filled=None):
        '''
        Initialize a Circle object with optional parameters.

        Args:
            x (float): The x-coordinate of the circle.
            y (float): The y-coordinate of the circle.
            radius (float): The radius of the circle.
            ptr (str): The color of the circle.
            filled (bool): A boolean indicating whether the circle is filled.
        '''
        super().__init__(x, y, ptr, filled)
        if radius is not None and radius > 0:
            self._radius = float(radius)
        else:
            self._radius = 0.0

    def __str__(self):
        return (f'radius: {self._radius}{'\n'}'
                f'({self.get_x()},{self.get_y()}){'\n'}'
                f'color: {self.color}{'\n'}'
                f'filled: {self.fill}')

    def __repr__(self):
        if self.fill is True:
            return str(f'radius: {int(self._radius)} ({int(self.get_x())},{int(self.get_y())}) {self.color} filled')
        return str(f'radius: {int(self._radius)} ({int(self.get_x())},{int(self.get_y())}) {self.color} no filled')

    @property
    def radius(self):
        '''
        Get the radius of the circle.

        Returns:
            float: The radius of the circle.
        '''
        return self._radius

    @radius.setter
    def radius(self, new_rad):
        '''
        Set the radius of the circle.

        Args:
            new_rad (float): The new radius of the circle.
        '''
        if new_rad < 0:
            self._radius = 0.0
        else:
            self._radius = float(new_rad)

    @radius.getter
    def radius(self):
        '''
        Get the radius of the circle.

        Args:
            new_rad (float): The new radius of the circle.
        '''
        return self._radius

    def get_area(self):
        '''
        Calculate the area of the circle.

        Returns:
            float: The area of the circle.
        '''
        return float(math.pi * self._radius ** 2)

    def get_perimetr(self):
        '''
        Calculate the perimeter of the circle.

        Returns:
            float: The perimeter of the circle.
        '''
        return float(math.pi * self._radius * 2)

    def get_diametr(self):
        '''
        Calculate the diameter of the circle.

        Returns:
            float: The diameter of the circle.
        '''
        return float(2 * self._radius)


class Rectangle(GeometricObject):
    '''
    A class representing a rectangle with width and height.

    Attributes:
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.
    '''
    width = 0.0
    height = 0.0

    def __init__(self, x=None, y=None, width=None, height=None, ptr=None, filled=None):
        '''
        Initialize a Rectangle object with optional parameters.

        Args:
            x (float): The x-coordinate of the rectangle.
            y (float): The y-coordinate of the rectangle.
            width (float): The width of the rectangle.
            height (float): The height of the rectangle.
            ptr (str): The color of the rectangle.
            filled (bool): A boolean indicating whether the rectangle is filled.
        '''
        super().__init__(x, y, ptr, filled)
        if width is not None and width > 0:
            self.width = width
        else:
            self.width = 0.0
        if height is not None and height > 0:
            self.height = height
        else:
            self.height = 0.0

    def __str__(self):
        return (f'width: {self.width}{'\n'}'
                f'height: {self.height}{'\n'}'
                f'({self.get_x()}, {self.get_y()}){'\n'}'
                f'color: {self.color}{'\n'}'
                f'filled: {self.fill}')

    def __repr__(self):
        if self.fill is True:
            return str(f'width: {int(self.width)} height: {int(self.height)} '
                       f'({int(self.get_x())}, {int(self.get_y())}) '
                       f'{self.color} filled')
        return str(f'width: {int(self.width)} height: {int(self.height)} '
                       f'({int(self.get_x())}, {int(self.get_y())}) '
                       f'{self.color} no filled')

    def set_width(self, new_width):
        '''
        Set the width of the rectangle.

        Args:
            new_width (float): The new width of the rectangle.
        '''
        if new_width < 0:
            self.width = 0
        else:
            self.width = new_width

    def set_height(self, new_height):
        '''
        Set the height of the rectangle.

        Args:
            new_height (float): The new height of the rectangle.
        '''
        if new_height < 0:
            self.height = 0
        else:
            self.height = new_height

    def get_width(self):
        '''
        Get the width of the rectangle.

        Returns:
            float: The width of the rectangle.
        '''
        return float(self.width)


    def get_height(self):
        '''
        Get the height of the rectangle.

        Returns:
            float: The height of the rectangle.
        '''
        return float(self.height)


    def get_area(self):
        '''
        Calculate the area of the rectangle.

        Returns:
            float: The area of the rectangle.
        '''
        return float(self.width * self.height)


    def get_perimetr(self):
        '''
        Calculate the perimeter of the rectangle.

        Returns:
            float: The perimeter of the rectangle.
        '''
        return float(2 * self.width + 2 * self.height)


point = GeometricObject()
print(point)
print()
point.set_coordinate(-4, 9)
print(point.get_x())
print(point.get_y())
point.set_color('red')
print(point.get_color())
point.set_filled(True)
print(point.is_filled())
print()
print(point)
print()
point_2 = GeometricObject(8, -4, 'blue', True)
print(point_2)
print()
circle = Circle()
print(circle)
print()
circle.radius = -34
print(circle.radius)
circle.radius = 12
print(circle.radius)
print()
circle_2 = Circle(3, -100, 20, 'green', True)
print(circle_2)
print()
circle_2.set_color('grey')
print(circle_2.get_color())
print()
print(circle_2.get_area())
print(circle_2.get_perimetr())
print(circle_2.get_diametr())
print()
circle_3 = Circle(90, -84, -223, 'pink')
print(circle_3)
print()
rectangle = Rectangle()
print(rectangle)
print()
rectangle.set_coordinate(11, 29)
rectangle.set_color('yellow')
rectangle.set_width(-10)
rectangle.set_height(20)
print(rectangle)
print()
rectangle.set_width(100)
print(rectangle.get_width())
print(rectangle.get_height())
print()
print(rectangle.get_area())
print(rectangle.get_perimetr())
print()
rectangle_2 = Rectangle(10, 20, 30, -40, 'brown', True)
print(rectangle_2)
print()
figures = []
figures.append(point)
figures.append(circle_2)
figures.append(rectangle)
print(figures)
