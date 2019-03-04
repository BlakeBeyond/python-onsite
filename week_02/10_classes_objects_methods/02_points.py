'''
Work through the chapter "Classes and Objects" in Think Python 2e:
http://greenteapress.com/thinkpython2/html/thinkpython2016.html and
build out the Point class example.

'''

# Thanks Arno !
import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


    def __str__(self):
        return(f"this [pont had an abscisse of {self,x} and an ordinate of {self.y}")



    def distance(self, other_point):
        a = abs(self.x - other_point.x)
        b = abs(self.y - other_point.y)
        distance = math.sqrt(a**2+b**2)


class Rectangle:
    def __init__(self, width, height, corner):
        self.width = width
        self.height = height
        self.corner = corner


    def find_center(self):
        p = Point()
        p.x = (self.corner.x + self.width) / 2
        p.y = (self.corner.y +self.height) / 2
        return p

    def grow_rectangle(self, dwidth, dheight):
        self.width += dwidth
        self.height += dheight
