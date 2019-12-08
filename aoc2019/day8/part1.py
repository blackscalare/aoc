with open('input.txt', 'r') as f:
    input = int(f.readline())
o = open('images.txt', 'w')

pixels = [int(x) for x in str(input)]
image_number = 0
for i, pixel in enumerate(pixels):
	if i % 150 == 0:
		image_number += 1
		if image_number > 1:
			o.write(',')
	o.write(str(pixel))
	
with open('images.txt', 'r') as f:
    input = f.readline()

images = input.split(',')
fewest_zeroes = 99999
answer = 0
for i, image in enumerate(images):
	zeroes = 0
	for pixel in image:
		if int(pixel) == 0:
			zeroes += 1
	if zeroes < fewest_zeroes:
		fewest_zeroes = zeroes
		answer = i

number_of_ones = 0
number_of_twos = 0
pixels = [int(x) for x in str(images[answer])]
for pixel in pixels:
	if pixel == 1:
		number_of_ones += 1
	elif pixel == 2:
		number_of_twos += 1
print(number_of_ones*number_of_twos)