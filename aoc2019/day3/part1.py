with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

line1 = lines[0].split(',')
line2 = lines[1].split(',')

def get_intersections(points1, points2):
    intersections = []
    steps_set = set()
    steps_set2 = set()
    for i in range(len(points1)):
        direction = 1
        if i == 0:
            continue
        if points1[i][0] != points1[i - 1][0]:
            if points1[i-1][0] > points1[i][0]:
                direction = -1
            for j in range(points1[i - 1][0], points1[i][0] + direction, direction):
                steps_set.add((j, points1[i][1]))
        elif points1[i][1] != points1[i - 1][1]:
            if points1[i-1][1] > points1[i][1]:
                direction = -1
            for j in range(points1[i - 1][1], points1[i][1] + direction, direction):
                steps_set.add((points1[i][0], j))

    for i in range(len(points2)):
        direction = 1
        if i == 0:
            continue
        if points2[i][0] != points2[i - 1][0]:
            if points2[i-1][0] > points2[i][0]:
                direction = -1
            for j in range(points2[i - 1][0], points2[i][0] + direction, direction):
                steps_set2.add((j, points2[i][1]))
        elif points2[i][1] != points2[i - 1][1]:
            if points2[i-1][1] > points2[i][1]:
                direction = -1
            for j in range(points2[i - 1][1], points2[i][1] + direction, direction):
                steps_set2.add((points2[i][0], j))
    for x in steps_set:
        if x in steps_set2:
            intersections.append(x)
    return intersections
    
def get_points(line):
    dx = 0
    dy = 0
    points = []
    points.append([0,0])
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
intersections = get_intersections(points1, points2)

lowest = 99999999
for intersection in intersections:
    ans = abs(0-intersection[0])+abs(0-intersection[1])
    if ans < lowest and ans != 0:
        lowest = ans
print(lowest)
