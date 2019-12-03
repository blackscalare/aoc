with open('testinput2.txt', 'r') as f:
	lines = f.readlines()

line1 = lines[0].split(',')
line2 = lines[1].split(',')
posX = 0
lastPosX = 0
lastPosY = 0
posY = 0
posX1 = 0
posY1 = 0
lastPosX1 = 0
lastPosY1 = 0
pastPositions = []
pastPositions1 = []
pastPositions.append([0,0])
pastPositions1.append([0,0])

distance = []

distanceX1 = []
distanceY1 = []

for a in line1:
	if a.startswith('R'):
		a = a.split('R')
		lastPosX = posX
		posX += int(a[1])
	elif a.startswith('U'):
		a = a.split('U')
		lastPosY = posY
		posY += int(a[1])
	elif a.startswith('L'):
		a = a.split('L')
		lastPosX = posX
		posX -= int(a[1])
	elif a.startswith('D'):
		a = a.split('D')
		lastPosY = posY
		posY -= int(a[1])
	
	distance.append([list(range(lastPosX, posX+1)), list(range(lastPosY, posY + 1))])

print(distance)

for a in line2:
	if a.startswith('R'):
		a = a.split('R')
		lastPosX1 = posX1
		posX1 += int(a[1])
	elif a.startswith('U'):
		a = a.split('U')
		lastPosY1 = posY1
		posY1 += int(a[1])
	elif a.startswith('L'):
		a = a.split('L')
		lastPosX1 = posX1
		posX1 -= int(a[1])
	elif a.startswith('D'):
		a = a.split('D')
		lastPosY1 = posY1
		posY1 -= int(a[1])
		
	distanceX1.append(list(range(lastPosX1, posX1+1)))
	distanceY1.append(list(range(lastPosY1, posY1+1)))
		
	#pastPositions1.append([posX1, posY1])
print(distanceX1)
print(distanceY1)

print('End position\nx: {}, y: {}'.format(posX, posY))
print('End position 2\nx: {}, y: {}'.format(posX1, posY1))