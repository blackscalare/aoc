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
	groups = 0
	print(x)
	for i in range(len(curr)):
		print(curr[i] == curr[i - 1])
		if curr[i] == curr[i-1]:
			rep += 2
		else:
			if rep == 2:
				groups += 1
			rep = 0
		if i == len(curr) - 1 and rep == 2:
			groups += 1
	if groups > 0:
		all_rep.append(x)
print(all_rep)
print(len(all_rep))