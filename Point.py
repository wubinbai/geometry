class Point:
    # The problem with this is that this defines class attributes,
    # not instance attributes, which is what I wanted to do.
    # x = 0.0
    # y = 0.0

    def __init__(self, x=0, y=0):   # Assigning x = 0 and y = 0 tells python to use 0 as default values
        # Defines instance attributes!
        self.x = x
        self.y = y
        # print("Point Constructor")
    # __str__ method is the equivalent of the toString from java...
    # Don't ever do this again --> def to_string(self):

    def __str__(self):
        return "{X: " + str(self.x) + ", Y: " + str(self.y) + "}"

    def distance(self, p):
        return ((self.x - p.x) ** 2 + (self.y - p.y) ** 2) ** .5
    def gradient(self, p):
        return (self.y - p.y)/(self.x - p.x)



# Self Made Goal:
# Try to create a quadrilateral class that takes in 4 points in its constructor to make a 4 sided polygon
# Give it the following methods:
#   ToString() --> Will print out all 4 points
#   sideLength() --> Will return the length between two points
#   perimeter() --> Will calculate the perimeter around the polygon


# Several problems with the following implementation:
#   What do I initialize p1, p2, p3, p4 to be other than 0? Should I just say Point()?
#   Doesn't that make it redundant in the constructor? Therefore is null more appropriate?
#
#   When computing side_length, is there a way to tell my function what points to use, rather than called the method
#   with q.p1 or q.p2? In other words, is there a way to just say p1 and p2 and have the function use the
#   quadrilateral's points only? Technically right now it could be a static method, but I'm trying to make it utilize
#   the quadrilateral's points.

class Quadrilateral:
    # Same issue, these are class attributes not instance attributes...
    # p1 = 0
    # p2 = 0
    # p3 = 0
    # p4 = 0

    def __init__(self, p1, p2, p3, p4):
        # This is an opportunity for a list instead.
        # self.p1 = p1
        # self.p2 = p2
        # self.p3 = p3
        # self.p4 = p4
        self.points = [p1, p2, p3, p4]
        # print("Quadrilateral Constructor")

    def __str__(self):
        total = ""
        for i in range(0, 4):
            total = total + "P" + str(i + 1) + str(self.points[i]) + " "
        return total

    def side(self, vertex_n):
        a = self.points[vertex_n]
        b = self.points[vertex_n - 1]
        return a.distance(b)

    def perimeter(self):
        total = 0
        # for loops are in range(inclusive, exclusive)
        for i in range(0, 4):
            total = total + self.side(i)
        return total
        # return sum([self.side(i) for i in range(4)])




