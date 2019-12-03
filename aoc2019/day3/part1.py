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
distance1 = []

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
		
	if lastPosX != posX:
		if posX < lastPosX:
			zz = lastPosX
			xx = posX
		else:
			zz = posX
			xx = lastPosX
		distance.append([list(range(xx, zz+1)), posY])
	elif lastPosY != posY:
		if posY < lastPosY:
			zz = lastPosY
			xx = posY
		else:
			zz = posY
			xx = lastPosY
		distance.append([posX, list(range(xx, zz+1))])

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
		
	if lastPosX1 != posX1:
		if posX1 < lastPosX1:
			zz = lastPosX1
			xx = posX1
		else:
			zz = posX1
			xx = lastPosX1
		distance1.append([list(range(xx, zz+1)), posY1])
	elif lastPosY1 != posY1:
		if posY1 < lastPosY1:
			zz = lastPosY1
			xx = posY1
		else:
			zz = posY1
			xx = lastPosY1
		distance1.append([posX1, list(range(xx, zz+1))])
print(distance1)



print('End position\nx: {}, y: {}'.format(posX, posY))
print('End position 2\nx: {}, y: {}'.format(posX1, posY1))