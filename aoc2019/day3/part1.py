with open('testinput2.txt', 'r') as f:
	lines = f.readlines()

line1 = lines[0].split(',')
line2 = lines[1].split(',')

def distance_calc(line):
	dx = 0
	dy = 0
	distance = []
	for a in line:
		if a.startswith('R'):
			dx += int(a[1:])
		elif a.startswith('U'):
			dy += int(a[1:])
		elif a.startswith('L'):
			dx -= int(a[1:])
		elif a.startswith('D'):
			dy -= int(a[1:])
		distance.append([dx, dy])
	return distance

def all_points(distance):
	allPoints = []
	lastPoint = [0, 0]
	for point in distance:
		reverse = 1
		if point[0] != lastPoint[0]:
			if lastPoint[0] > point[0]:
				reverse = -1
			allPoints.append([list(range(lastPoint[0], point[0] + reverse, reverse)), lastPoint[1]])
		else:
			if lastPoint[1] > point[1]:
				reverse = -1
			allPoints.append([lastPoint[0], list(range(lastPoint[1], point[1] + reverse, reverse))])
		lastPoint = point
	
	return allPoints
	
def find_intersections(allPoints, allPoints1):
	steps = len(allPoints)
	for x in allPoints:
		print('Steps left: {}'.format(steps))
		for y in allPoints1:
			if type(x[0]) == list:
				for i in x[0]:
					if type(y[0]) == list:
						for j in y[0]:
							if i == y[0] and x[1] == j:
								print('X')
		steps -= 1
	
	
distance = distance_calc(line1)
distance1 = distance_calc(line2)
allPoints = all_points(distance)
allPoints1 = all_points(distance1)
#print(distance)
#print(allPoints)
intersections = find_intersections(allPoints, allPoints1)

#print(allPoints)
#print(allPoints1)
#print(distance)
#print(distance1)
print(intersections)
for x in allPoints:
	if x in allPoints1:
		ans = abs(0-x[0])+abs(0-x[1])
		print(ans)

print('End position\n{}'.format(distance[len(distance) - 1]))
print('End position 2\n{}'.format(distance1[len(distance) - 1]))