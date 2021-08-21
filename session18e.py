import math

class Point:

    def __init__(self,label, x,y):
        self.label = label
        self.x = x
        self.y = y

    def show(self):
        print("point{}: {}|{}".format(self.label, self.x, self.y))
    #using self as point1 means renamed self as point 1

    def calculate_distance(point1, point2):
        distance =math.sqrt((point2.y - point1.y)**2 + (point2.x - point1.x)**2)
        print("distance between {} and {} is {}".format(point1.label, point2.label, distance))
    @staticmethod
    def create_points_from_files():
        print("create points")

        points = []

        file = open("points.csv", "r")
        lines = file.readlines()

        lbl = 1
        for line in lines:
            point = line.split(",")
            points.append(Point(lbl, float(point[0]), float(point[1])))
            lbl += 1

        return points

def main():
    p1 = Point("a", 10, 20)
    p2 = Point("b", 30 , 40)
    #p1.calculate_distance(p2)
    Point.calculate_distance(p1, p2)
    points = Point.create_points_from_files()
    for point in points:
          point.show()


if __name__ == '__main__':
    main()


