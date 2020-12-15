starting_numbers = [line.rstrip('\n').split(',') for line in open('input.txt')]

numbers = []
for number in starting_numbers:
    for n in number:
        numbers.append(int(n))
previous_spoken = {}
last_spoken_number = spoken_number = 0
occurances = []
for i in range(len(numbers)):
    last_spoken_number = numbers[i]
    previous_spoken[last_spoken_number] = [i + 1, i + 1]
    occurances.append(last_spoken_number)

for i in range(len(numbers) + 1, 30000001):
    if occurances.count(last_spoken_number) <= 1:
        spoken_number = 0
        j = previous_spoken[spoken_number][1]
        previous_spoken[spoken_number] = [j, i]
    else:
        vals = previous_spoken[last_spoken_number]
        spoken_number = vals[1] - vals[0]
        try:
            j = previous_spoken[spoken_number][1]
            previous_spoken[spoken_number] = [j, i]
        except:
            previous_spoken[spoken_number] = [i, i]
    occurances.append(spoken_number)
    last_spoken_number = spoken_number
print(spoken_number)
