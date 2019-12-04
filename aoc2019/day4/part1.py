valid_pws = 0
for x in range(156218, 652527):
	curr = str(x)
	last_c = 0
	rep = 0
	valid = True
	for i, c in enumerate(curr):
		if i == 0:
			last_c = c
			continue
		if last_c < c:
			valid = False
			break
		last_c = c
	if valid:
		print(x)
		valid_pws += 1
print(valid_pws)
