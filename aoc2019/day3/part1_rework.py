with open('testinput2.txt', 'r') as f:
    lines = f.read().splitlines()

line1 = lines[0].split(',')
line2 = lines[1].split(',')

print(line1)
print(line2)

def get_intersections(points1, points2):
    for i, point1 in enumerate(points1[1:]):
        for j, point2 in enumerate(points2[1:]):
            if points1[i][0] != points1[i - 1][0]:
                if points1[i][0] in range(points2[j - 1][0], points2[j][0]):
                    print(points1[i][0],points2[j][0])
            elif points2[j][0] != points2[j - 1]

def get_points(line):
    dx = 0
    dy = 0
    points = []
    for point in line:
        if point.startswith('U'):
            dx += int(point[1:])
        elif point.startswith('R'):
            dy += int(point[1:])
        elif point.startswith('D'):
            dx -= int(point[1:])
        elif point.startswith('L'):
            dy -= int(point[1:])
        points.append([dx, dy])
    return points

points1 = get_points(line1)
points2 = get_points(line2)
for x, y in zip(points1, points2):
    print(x, y)
get_intersections(points1, points2)