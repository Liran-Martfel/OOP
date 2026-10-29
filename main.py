#creating class, exersice within class 25/10/2026

#class point
#-x : float
#-y : float
# + X: {read only}
# + y: {read only}

#create point1 [x=9.44,y=-10]
#print(point1.X)
#print(point2.Y),

import math
from functools import total_ordering
@total_ordering
class Point:
    def __init__(self,x : float,y : float):
        self._x=x
        self._y=y

    def __repr__(self):
        return f'Point({self._x},{self._y})'

    @property
    def X(self):
        return self._x
    @property
    def Y(self):
        return self._y

    def __add__(self,other):
        if isinstance(other,(int,float)):
            return Point(self._x+other,self._y+other)
        elif not isinstance(other,Point):
            return NotImplemented
        return Point(self._x + other._x,self._y + other._y)

    def __sub__(self,other):
        if isinstance(other,(int,float)):
            return Point(self._x-other,self._y-other)
        elif not isinstance(other,Point):
            return NotImplemented
        return Point(self._x - other._x, self._y - other._y)

    def __mul__(self, other):
        if isinstance(other,(int,float)):
            return Point(self._x * other, self._y * other)
        elif not isinstance(other,Point):
            return NotImplemented
        return Point(self._x * other._x,self._y * other._y)

    def __div__(self,other):
        if isinstance(other,(int,float)):
            return Point(self._x / other, self._y / other)
        elif not isinstance(other,Point):
            return NotImplemented
        return Point(self._x / other._x,self._y / other._y)

    def __eq__(self,other):
        if not isinstance(other,Point):
            return NotImplemented
        return Point._distance_from_origin(self) == Point._distance_from_origin(other)

    def __neq__(self,other):
        return not self.__eq__(other)

    def _distance_from_origin(self):
        return math.sqrt(self._x ** 2 + self._y ** 2)

    def __lt__(self,other): #lt is less than
        if not isinstance(other,Point):
            return NotImplemented
        return Point._distance_from_origin(self) < Point._distance_from_origin(other)

    def __gt__(self,other): #lt is less than
        return not self.__lt__(other)

    def __len__(self):
        return int(Point._distance_from_origin(self))

point1 = Point(x = 9.44,y = -10)
print(f'Point1: {point1}')
print('X:',point1.X)
print('Y:',point1.Y)
p1 = Point(4.51,-0.3)
p2 = Point (0.7,1)
p3 = Point(0.7,1)
p4 = Point (0.7,1)
#p5 = p1 + 5 = Type_error
print(f'Point 3: {p3}\nPoint 4: {p4}')
print(len(p4))
# __radd__ (Right Addition) - A magic method for reflected addition.
# Python automatically calls this when the object on the left side of the '+' operator
# does not know how to add a Point (for example: 5 + p1).