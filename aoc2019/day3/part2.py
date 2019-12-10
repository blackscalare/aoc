import time
start_time = time.time()

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

line1 = lines[0].split(',')
line2 = lines[1].split(',')

def get_intersections(points1, points2):
    intersections = []
    steps = []
    steps2 = []

    for i in range(len(points1)):
        direction = 1
        if i == 0:
            continue
        if points1[i][0] != points1[i - 1][0]:
            if points1[i-1][0] > points1[i][0]:
                direction = -1
            for j in range(points1[i - 1][0], points1[i][0] + direction, direction):
                steps.append((j, points1[i][1]))
        elif points1[i][1] != points1[i - 1][1]:
            if points1[i-1][1] > points1[i][1]:
                direction = -1
            for j in range(points1[i - 1][1], points1[i][1] + direction, direction):
                steps.append((points1[i][0], j))

    for i in range(len(points2)):
        direction = 1
        if i == 0:
            continue
        if points2[i][0] != points2[i - 1][0]:
            if points2[i-1][0] > points2[i][0]:
                direction = -1
            for j in range(points2[i - 1][0], points2[i][0] + direction, direction):
                steps2.append((j, points2[i][1]))
        elif points2[i][1] != points2[i - 1][1]:
            if points2[i-1][1] > points2[i][1]:
                direction = -1
            for j in range(points2[i - 1][1], points2[i][1] + direction, direction):
                steps2.append((points2[i][0], j))
    steps_set = set(steps)
    steps_set2 = set(steps2)
    for x in steps_set:
        if x in steps_set2:
            intersections.append(x)
    return intersections, steps, steps2
    
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

lowest = 9999999
for intersection in intersections[0]:
    dx = 0
    dy = 0
    dx2 = 0
    dy2 = 0
    for i in range(len(intersections[1])):
        if intersections[1][i] == intersection :
            break
        if i == 0:
            continue
        if intersections[1][i][0] != intersections[1][i - 1][0]:
            dx += abs(intersections[1][i][0] - intersections[1][i - 1][0])
        else:
            dy += abs(intersections[1][i][1] - intersections[1][i - 1][1])
    for i in range(len(intersections[2])):
        if intersections[2][i] == intersection :
            break
        if i == 0:
            continue
        if intersections[2][i][0] != intersections[2][i - 1][0]:
            dx2 += intersections[2][i][0] - intersections[2][i - 1][0] 
        else:
            dy2 += intersections[2][i][1] - intersections[2][i - 1][1]
    print(dx+dy)
    print(dx2+dy2)
print(lowest)
print("TIME {}".format(time.time()-start_time))
