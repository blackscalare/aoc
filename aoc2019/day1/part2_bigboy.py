import time
f = open('bigboyinput.txt', 'r')
total = 0
start_time = time.time()
	
for x in f:
	val = int(x)//3 - 2
	while val > 0:
		total += val
		val = val // 3 - 2

print(total)

print("--- %s seconds ---" % (time.time() - start_time))