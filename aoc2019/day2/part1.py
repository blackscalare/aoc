with open('input.txt', 'r') as f:
    codes = f.readlines()
	
sanitizedList = codes[0].split(',')
sanitizedList[1] = 40
sanitizedList[2] = 19
for i in range(len(sanitizedList)):
	if i % 4 == 0:
		if int(sanitizedList[i]) == 1:
			sanitizedList[int(sanitizedList[i+3])] = int(sanitizedList[int(sanitizedList[i+1])]) + int(sanitizedList[int(sanitizedList[i+2])])
		elif int(sanitizedList[i]) == 2:
			sanitizedList[int(sanitizedList[i+3])] = int(sanitizedList[int(sanitizedList[i+1])]) * int(sanitizedList[int(sanitizedList[i+2])])
		elif int(sanitizedList[i]) == 99:
			break
	
print(sanitizedList[0])