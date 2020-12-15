def run(starting_numbers, length):
    numbers = []
    for number in starting_numbers:
        for n in number:
            numbers.append(int(n))
    previous_spoken = {}
    last_spoken_number = spoken_number = 0
    occurances = []
    for i in range(len(numbers)):
        last_spoken_number = numbers[i]
        previous_spoken[last_spoken_number] = [i + 1]

    for i in range(len(numbers) + 1, length+1):
        if len(previous_spoken[last_spoken_number]) <= 1:
            spoken_number = 0
            previous_spoken[spoken_number].append(i)
        else:
            vals = previous_spoken[last_spoken_number]
            spoken_number = vals[-1] - vals[-2]
            try:
                previous_spoken[spoken_number].append(i)
            except:
                previous_spoken[spoken_number] = [i]
        last_spoken_number = spoken_number
    print(spoken_number)


starting_numbers = [line.rstrip('\r\n').split(',') for line in open('input.txt')]
run(starting_numbers, 2020)
run(starting_numbers, 30000000)