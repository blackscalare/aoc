import time
start_time = time.time()
with open('input.txt', 'r') as f:
    codes = f.readlines()

for x in range(100):
	for y in range(100):
		sanitizedList = codes[0].split(',')
		sanitizedList[1] = x
		sanitizedList[2] = y
		for i in range(len(sanitizedList)):
			if i % 4 == 0:
				if int(sanitizedList[i]) == 1:
					sanitizedList[int(sanitizedList[i+3])] = int(sanitizedList[int(sanitizedList[i+1])]) + int(sanitizedList[int(sanitizedList[i+2])])
				elif int(sanitizedList[i]) == 2:
					sanitizedList[int(sanitizedList[i+3])] = int(sanitizedList[int(sanitizedList[i+1])]) * int(sanitizedList[int(sanitizedList[i+2])])
				elif int(sanitizedList[i]) == 99:
					break
			if int(sanitizedList[0]) == 19690720:
				print('x: {}, y: {}'.format(x,y))
				print(100*int(x)+int(y))
				
print("TIME {}".format(time.time()-start_time))