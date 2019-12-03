import time
f = open('input.txt', 'r')
total = 0
start_time = time.time()
def calcFuel(currentValue):
	global total
	val = currentValue//3-2
	if(val > 0):
		total += val
		calcFuel(val)
	
for x in f:
	calcFuel(int(x))

print(total)

print("--- %s seconds ---" % (time.time() - start_time))