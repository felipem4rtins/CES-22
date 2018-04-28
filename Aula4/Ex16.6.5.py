# Felipe Martins Gomes
# Comp 20
# Exercício 16.6.5
# Programa compilado com PyCharm 2018.1.2


class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self, x=0, y=0):
        """ Create a new point at the origin """
        self.x = x
        self.y = y

    def __str__(self):    # All we have done is renamed the method
            return "({0}, {1})".format(self.x, self.y)


class Rectangle:

    def __init__(self, posn, w, h):
        self.corner = posn
        self.width = w
        self.height = h

    def __str__(self):
        return "({}, {}, {})".format(self.corner, self.width, self.height)

    def overlapping_rectangle(self, r):
        if (self.corner.x > (r.corner.x + r.width) or r.corner.x>(self.corner.x + self.width)):
            return False

        if ((self.corner.y + self.height)< r.corner.y or (r.corner.y+r.height)<self.corner.y):
            return False

        return True

R1 = Rectangle(Point(0, 0), 10, 10)
R2 = Rectangle(Point(11, 11), 10, 10)
R3 = Rectangle(Point(5, 0), 10, 10)
R4 = Rectangle(Point(0,5), 10, 10)

print("Retangulo 1 =", R1)
print("Retangulo 2 =", R2, "\nRetangulo 3 =", R3, "\nRetangulo 4 =", R4)
print("\nTest R1.overlapping_rectangle(R2) = {}".format(R1.overlapping_rectangle(R2)))
print("\nTest R1.overlapping_rectangle(R3) = {}".format(R1.overlapping_rectangle(R3)))
print("\nTest R1.overlapping_rectangle(R4) = {}".format(R1.overlapping_rectangle(R4)))
print("\nTest R2.overlapping_rectangle(R1) = {}".format(R2.overlapping_rectangle(R1)))
print("\nTest R2.overlapping_rectangle(R3) = {}".format(R2.overlapping_rectangle(R3)))
print("\nTest R2.overlapping_rectangle(R4) = {}".format(R2.overlapping_rectangle(R4)))
print("\nTest R3.overlapping_rectangle(R1) = {}".format(R3.overlapping_rectangle(R1)))
print("\nTest R3.overlapping_rectangle(R2) = {}".format(R3.overlapping_rectangle(R2)))
print("\nTest R3.overlapping_rectangle(R4) = {}".format(R3.overlapping_rectangle(R4)))