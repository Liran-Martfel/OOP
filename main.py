#creating class, exersice within class 25/10/2026
from unittest import result


#class point
#-x : float
#-y : float
# + X: {read only}
# + y: {read only}

#create point1 [x=9.44,y=-10]
#print(point1.X)
#print(point2.Y),

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
        return Point(self._x + other._x,self._y + other._y)

    def __sub__(self,other):
        return Point(self._x - other._x, self._y - other._y)

point1 = Point(x = 9.44,y = -10)
print(f'Point1: {point1}')
print('X:',point1.X)
print('Y:',point1.Y)
p1 = Point(4.51,-0.3)
p2 = Point (0.7,1)
p3 = p1 + p2
p4 = p1 - p2
print(f'Point 3: {p3}\nPoint 4: {p4}')
