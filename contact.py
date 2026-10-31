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

    @staticmethod
    def _distance_from_origin(Point):
        return math.sqrt(Point._x ** 2 + Point._y ** 2)

    def __lt__(self,other): #lt is less than
        if not isinstance(other,Point):
            return NotImplemented
        return Point._distance_from_origin(self) < Point._distance_from_origin(other)

    def __gt__(self,other): #lt is less than
        return not self.__lt__(other)

    def __len__(self):
        return int(Point._distance_from_origin(self))

    def __str__(self):
        return f'Point({self._x},{self._y})'

    def __repr__(self):
        pass


point1 = Point(9.44,-10)
#print(f'Point1: {point1}')
#print('X:',point1.X)
#print('Y:',point1.Y)
p1 = Point(4.51,-0.3)
p2 = Point (0.7,1)
p3 = Point(0.7,1)
p4 = Point (3,4)
p5 = Point(2.5,3.5)
#p5 = p1 + 5 = Type_error
#print(f'Point 3: {p3}\nPoint 4: {p4}')
#print(len(p4))
#print(p4)
# __radd__ (Right Addition) - A magic method for reflected addition.
# Python automatically calls this when the object on the left side of the '+' operator
# does not know how to add a Point (for example: 5 + p1).

class Contact:

    count : int = 0 #class-member

    #instance member
    def __init__(self, name, number):
        self._name = name
        self._number = number
        Contact.count += 1
        self._index = Contact.count
        self.color = 'yellow'

    # 1. Getter עבור name (חייב להופיע ראשון)
    @property
    def name(self):
        return "**" + self._name + "**"

    # 2. Setter עבור name
    @name.setter
    def name(self, value):
        value = value.strip()
        if value:
          self._name = value
        else:
          raise ValueError("Name cannot be empty")

    # 3. Getter עבור number
    @property
    def number(self):
        return self._number

    # 4. Setter עבור number
    @number.setter
    def number(self, value):
        value = value.strip()
        if value:
          self._number = value
        else:
          raise ValueError("Number cannot be empty")

    def describe(self):
        print(f'Name: {self._index}, Number: {self._number}')

    @staticmethod
    def from_string(txt):
        name,number = txt.strip().split(':')
        return Contact(name,number)

    @classmethod
    def from_str(cls,txt):
        name,number = txt.strip().split(':')
        return cls(name,number)

    def __str__(self):
        return f'Contact({self._index})'

danny = Contact("Danny", "050-2372361")
danny.number = "050-2372361"
danny.name = "Danny"
print(danny.describe())
print(danny.name)



######################################################## Parent Child #######################################################
class Parent:
    @classmethod
    def identify(cls):
        print(f'This method is bound to: {cls.__name__}')

class Child(Parent):
    pass
Parent.identify()
Child.identify()