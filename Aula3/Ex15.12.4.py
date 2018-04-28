# Felipe Martins Gomes
# Comp 20
# Exercício 15.12.4
# Programa compilado com PyCharm 2018.1.2


class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self, x=0, y=0):
        """ Create a new point at the origin """
        self.x = x
        self.y = y

    def slope_from_origin(self):
        return print("{}".format(self.y/self.x))

    def get_line_to(self, m):
        a = (self.y - m.y)/(self.x - m.x)
        b = m.y - a*m.x
        return print("({0:},{1:})".format(a, b))

print("Point(4,11).get_line_to(Point(6,15))")
Point(4, 11).get_line_to(Point(6, 15))

print("\nPoint(5,5).get_line_to(Point(10,10))")
Point(5, 5).get_line_to(Point(10, 10))