#  File: Geometry.py

#  Description: Classes for point, line, and circle are defined. Main function uses these classes to check various things. 

#  Student Name: Garner Vincent

#  Student UT EID: GV4353

#  Date Created:2-10-15

#  Date Last Modified: 2-13-15

import math

class Point (object):
  # constructor with default values
  def __init__ (self, x = 0, y = 0):
    self.x = x
    self.y = y

  # get distance to another Point object
  def dist (self, other):
    return (math.sqrt(abs(self.x - other.x)**2 + abs(self.y - other.y)**2))

  # create a string representation of a Point (x, y)
  def __str__ (self):
    return ('(' + str(self.x) + ', ' + str(self.y) + ')')

  # test for equality between two points
  def __eq__ (self, other):
    tol = 1.0e-18
    return (abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol)

class Line (object):
  # constructor assign default values if user defined points are the same
  def __init__ (self, p1_x = 0, p1_y = 0, p2_x = 1, p2_y = 1):
    tol = 1.0e-18
    if (abs(p1_x - p2_x) < tol) and (abs(p1_y - p2_y) < tol):
      self.p1 = Point(0, 0)
      self.p2 = Point(1, 1)
    else:
      self.p1 = Point(p1_x, p1_y)
      self.p2 = Point(p2_x, p2_y)

  # determine if line is parallel to x axis
  def is_parallel_x (self):
    tol = 1.0e-18
    return (abs(self.p1.y - self.p2.y) < tol) 

  # determine if line is parallel to y axis
  def is_parallel_y (self):
    tol = 1.0e-18
    return (abs(self.p1.x - self.p2.x) < tol)

  # determine slope for the line
  # return float ('inf') if line is parallel to the y-axis
  def slope (self):
    if self.is_parallel_y():
      return float ('inf')
    else:
      return (self.p1.y - self.p2.y) / (self.p1.x - self.p2.x)

  # determine the y-intercept of the line
  # y = mx + b     b = y - mx
  def y_intercept (self):
    return (self.p1.y - self.slope() * self.p1.x)

  # determine the x-intercept of the line
  # -b = mx 
  # -b / m = x
  def x_intercept (self):
    return (-1 * self.y_intercept() / self.slope())

  # determine if two lines are parallel
  #two lines are parallel if their slopes are equal
  def is_parallel (self, other):
    tol = 1.0e-18
    return(abs(self.slope() - other.slope()) < tol)


  # determine if two lines are perpendicular to each other
  # two lines are perpendicular if their slopes are inverse
  def is_perpendicular (self, other):
    tol = 1.0e-18
    return (abs(self.slope() * -1 - other.slope() < tol))

    #add condition for x/y parallality

  # determine if a point is on the line or on an extension of it
  # a point is on the line if it fits into the equation y = mx + b 
  def is_on_line (self, p):
    tol = 1.0e-18
    if (self.is_parallel_y()):
      return (abs(p.x - self.x_intercept()) < tol)
    else:
      return(abs(self.slope() * p.x + self.y_intercept() - p.y) < tol)



  # determine the perpendicular distance of a point to the line
  # point will have a point matching on the intersection with a slope that is -1/m of the original slope
  def perp_dist (self, p):
    if self.is_parallel_y():
      dist = abs(self.p1.x - p.x)
      return dist
    else:
      slope2 = -1 / self.slope()
      #y = mx + b
      #b = y - mx
      y2int2 = p.y - slope2 * p.x
      x = (y2int2 - self.y_intercept()) / (self.slope() - slope2)
      y = self.slope() * x + self.y_intercept()
      p2 = Point(x, y)
      return p.dist(p2)


  # determine the intersection point of two lines if not parallel
  #x = b2 - b1 / m1 - m2
  #y = mx + b
  def intersection_point (self, other):
    if not self.is_parallel(other):
      x = (other.y_intercept() - self.y_intercept()) / (self.slope() - other.slope())
      y = self.slope() * x + self.y_intercept()
      return (Point(x, y))


  # determine if two points are on the same side of the line
  # return False if one or both points are on the line
  def on_same_side (self, p1, p2):
    y1 = self.slope() * p1.x + self.y_intercept()
    y2 = self.slope() * p2.x + self.y_intercept()
    return (p1.y > y1 and p2.y > y2) or (p1.y < y1 and p2.y < y2)


  # string representation of the line - one of three cases
  # y = c
  # x = c
  # y = m * x + b
  def __str__ (self):
    if self.is_parallel_x():
      return 'y ' + ' = ' + str(self.p1.y)
    elif self.is_parallel_y():
      return 'x ' + ' = ' + str(self.p1.x)
    else:
      return 'y = ' + str(self.slope()) + ' x + ' + str(self.y_intercept())

    
class Circle (object):
  # constructor with default values
  def __init__ (self, radius = 1, x = 0, y = 0):
    self.radius = radius
    self.center = Point(x, y)

  # compute circumference
  def circumference (self):
    return 2 * math.pi * self.radius

  # compute area
  def area (self):
    return math.pi * self.radius ** 2

  # determine if a point is inside the circle
  def is_inside_point (self, p):
    return self.center.dist(p) < self.radius

  # determine if the other circle is strictly inside self
  def is_inside_circle (self, other):
    return self.center.dist(other.center) + other.radius < self.radius

  # determine if the other circle intersects self
  def does_intersect_circle (self, other):
    return (self.center.dist(other.center) < self.radius + other.radius)

  # determine if the line intersects circle
  def does_intersect_line (self, line):
    return abs(line.perp_dist(self.center) < self.radius)

  # determine if the line is tangent to the circle
  def is_tangent (self, line):
    tol = 1.0e-18
    return abs(line.perp_dist(self.center) - self.radius) < tol


  # string representation of a circle
  # Radius: radius, Center: (x, y)
  def __str__ (self):
    return 'Radius: ' + str(self.radius) + ', Center: ' + str(self.center)


def main():
  # open file "geometry.txt" for reading
  inFile = open('./geometry.txt', 'r')

  # read the coordinates of the first Point P
  line = inFile.readline().strip()
  x = ''
  y = ''
  space = 0
  for ch in line:
    if ch == ' ':
      space = line.index(ch)
      break
    else:
      x += ch

  for ch in line[space + 1:]:
    if ch == ' ':
      break
    else:
      y += ch

  P = Point(float(x), float(y))

  # read the coordinates of the second Point Q
  line = inFile.readline().strip()
  x = ''
  y = ''
  space = 0
  for ch in line:
    if ch == ' ':
      space = line.index(ch)
      break
    else:
      x += ch

  for ch in line[space + 1:]:
    if ch == ' ':
      break
    else:
      y += ch

  Q = Point(float(x), float(y))

  # print the coordinates of points P and Q
  print ('Coordinates of P: ' + str(P))
  print ('Coordinates of Q: ' + str(Q))

  # print distance between P and Q
  dist = P.dist(Q)
  print ('Distance between P and Q:', dist)

  # print the slope of the line PQ
  lyne = Line(P.x, P.y, Q.x, Q.y)
  print('Slope of PQ: ' + str(lyne.slope()))

  # print the y-intercept of the line PQ
  print('Y-Intercept of PQ: ' + str(lyne.y_intercept()))

  # print the x-intercept of the line PQ
  print('X-Intercept of PQ: ' + str(lyne.x_intercept()))

  # read the coordinates of the third Point A
  line = inFile.readline().strip()
  x = ''
  y = ''
  space = 0
  for ch in line:
    if ch == ' ':
      space = line.index(ch)
      break
    else:
      x += ch

  for ch in line[space + 1:]:
    if ch == ' ':
      break
    else:
      y += ch

  A = Point(float(x), float(y))
	
  # read the coordinates of the fourth Point B
  line = inFile.readline().strip()
  x = ''
  y = ''
  space = 0
  for ch in line:
    if ch == ' ':
      space = line.index(ch)
      break
    else:
      x += ch

  for ch in line[space + 1:]:
    if ch == ' ':
      break
    else:
      y += ch

  B = Point(float(x), float(y))

  # print the string representation of the line AB
  lyne2 = Line(A.x, A.y, B.x, B.y)
  print('Line AB: ' + str(lyne2))

  # print if the lines PQ and AB are parallel or not
  if lyne.is_parallel(lyne2):
    print('PQ is parallel to AB')
  else:
    print('PQ is not parallel to AB')

  # print if the lines PQ and AB (or extensions) are perpendicular or not
  if lyne.is_perpendicular(lyne2):
    print('PQ is perpendicular to AB')
  else:
    print('PQ is not perpendicular to AB')

  # print coordinates of the intersection point of PQ and AB if not parallel
  if not lyne.is_parallel(lyne2):
    print ('Intersection point of PQ and AB: ' + str(lyne.intersection_point(lyne2)))

  # read the coordinates of the fifth Point G
  line = inFile.readline().strip()
  x = ''
  y = ''
  space = 0
  for i in range(len(line)):
    if line[i] == ' ':
      firstEnd = i
      break
    else:
      x += line[i]

  for i in range(firstEnd + 1, len(line)):
    if line[i] == ' ':
      break
    else:
      y += line[i]

  G = Point(float(x), float(y))

  # read the coordinates of the sixth Point H
  line = inFile.readline().strip()
  x = ''
  y = ''
  space = 0
  for i in range(len(line)):
    if line[i] == ' ':
      firstEnd = i
      break
    else:
      x += line[i]

  for i in range(firstEnd + 1, len(line)):
    if line[i] == ' ':
      break
    else:
      y += line[i]

  H = Point(float(x), float(y))

  # print if the the points G and H are on the same side of PQ
  if lyne.on_same_side(G, H):
    print('G and H are on the same side of PQ')
  else:
    print('G and H are not on the same side of PQ')

  # print if the the points G and H are on the same side of AB
  if lyne2.on_same_side(G, H):
    print('G and H are on the same side of AB')
  else:
    print('G and H are not on the same side of AB')

  # read the radius of the circleA and the coordinates of its center
  line = inFile.readline().strip()
  x = ''
  y = ''
  radius = ''
  space = 0

  for i in range(len(line)):
    if line[i] == ' ':
      firstEnd = i
      break
    else:
      radius += line[i]

  for i in range(firstEnd + 1, len(line)):
    if line[i] == ' ':
      secondEnd = i
      break
    else:
      x += line[i]

  for i in range(secondEnd + 1, len(line)):
    if line[i] == ' ':
      break
    else:
      y += line[i]

  circleA = Circle(float(radius), float(x), float(y))

  # read the radius of the circleB and the coordinates of its center
  line = inFile.readline().strip()
  x = ''
  y = ''
  radius = ''
  space = 0

  for i in range(len(line)):
    if line[i] == ' ':
      firstEnd = i
      break
    else:
      radius += line[i]

  for i in range(firstEnd + 1, len(line)):
    if line[i] == ' ':
      secondEnd = i
      break
    else:
      x += line[i]

  for i in range(secondEnd + 1, len(line)):
    if line[i] == ' ':
      break
    else:
      y += line[i]

  circleB = Circle(float(radius), float(x), float(y))

  # print the string representation of circleA and circleB
  print('circleA: ' + str(circleA))
  print('circleB: ' + str(circleB))

  # determine if circleB is inside circleA
  if circleA.is_inside_circle(circleB):
    print('circleB is inside circleA')
  else:
    print('circleB is not inside circleA')

  # determine if circleA intersects circleB
  if circleA.does_intersect_circle(circleB):
    print('circleA does intersect circleB')
  else:
    print('circleA does not intersect circleB')

  # determine if line PQ (or extension) intersects circleA
  if circleA.does_intersect_line(lyne):
    print('PQ does intersect circleA')
  else:
    print('PQ does not intersect circleA')

  # determine if line AB (or extension) is tangent to circleB
  if circleB.is_tangent(lyne2):
    print('AB is a tangent to circleB')
  else:
    print('AB is not a tangent to circleB')

  # close file "geometry.txt"
  inFile.close()


main()
