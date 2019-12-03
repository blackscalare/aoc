import time
start_time = time.time()
f = open('input.txt', 'r')
total = 0
for x in f:
	total += int(x)//3-2
print(total)
print("--- %s seconds ---'" % (time.time() - start_time))