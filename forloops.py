for i in range(151):
	print(i)


for i in range(5, 1001, 5):
	print(i)


for i in range(1, 101):
	if i % 10 == 0:
		print("Coding Dojo")
	elif i % 5 == 0:
		print("Coding")
	else:
		print(i)


sum = 0;
for i in range(1, 500000, 2):
	sum +=i;
print(sum)


for i in range(2018, 1, -4):
	print(i)


def funct(lowNum, highNum, mult):
	for a in range(lowNum, highNum, mult):
		if lowNum% mult != 0:
			lowNum = lowNum + 1;

	for i in range(lowNum, highNum+1, mult):
		print(i)
funct(5, 20, 4)