valid_pws = 0
all_increasing = []
all_rep = []
for x in range(156218, 652527 + 1):
	valid = True
	curr = str(x)
	for i in range(len(curr)):
		if i == 0:
			continue
		if int(curr[i]) < int(curr[i - 1]):
			valid = False
			break
	if valid:
		all_increasing.append(x)
		
for x in all_increasing:
	rep = 0
	curr = str(x)
	valid = False
	for i in range(len(curr)):
		if i == 0:
			continue
		if int(curr[i]) == int(curr[i - 1]):
			valid = True
			break
	if valid:
		all_rep.append(x)
k=0
for x in all_increasing:
	if x in all_rep:
		k += 1
print(k)