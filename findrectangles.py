import math
class point:
    def __init__(self, l):
        self.x = l[0]
        self.y = l[1]
    def equals(self,point):
        if self.x == point.x and self.y == point.y:
            return True
        return False

class diagonal:
    x1, x2, y1, y2 = None, None, None, None
    point1, point2 = None, None
    def __init__(self,point1,point2):
        x1, y1 = point1.x, point1.y
        x2, y2 = point2.x, point2.y
        if x1 != x2 and y1 != y2:
            self.x1 = x1
            self.x2 = x2
            self.y1 = y1
            self.y2 = y2
            self.point1 = point1
            self.point2 = point2
    def unpack(self):
        return (self.x1, self.y1, self.x2, self.y2)
    def listofpoints(self):
        return [self.point1, self.point2]

def form_diagonals(point_objects):
    diagonals = []
    for i in range(len(point_objects)):
        for j in range(i,len(point_objects)):
            d = diagonal(point_objects[i], point_objects[j])
            # if any of the attributes is not none, then its
            # a valid diagonal as per the diagonal constructor
            if d.x1:
                diagonals.append(d)
    return list(set(diagonals))

def findnumberofrectangles(diagonals):
    count = 0
    for i in range(len(diagonals)):
        for j in range(i, len(diagonals)):
            x1,y1,x2,y2 = diagonals[i].unpack()
            lop = diagonals[j].listofpoints()
            p1 = point([x1,y2])
            p2 = point([x2,y1])
            if p1.equals(lop[0]) or p1.equals(lop[1]):
                if p2.equals(lop[0]) or p2.equals(lop[1]):
                    count += 1
    return math.floor((count*(count-1))/2)

points = [[3,4], [6,5], [5,4], [3,0], [5,0], [3,0]]
point_objects = list(map(point,points))
diagonals = form_diagonals(point_objects)
for item in diagonals:
    print(item.unpack())
print(findnumberofrectangles(diagonals))
