def countdown(num):
	for i in range(num, -1, -1):
		print(i)
#countdown(9)

def pr(num1, num2):
	print(num1)
	return num2
#print(pr(5, 8))

def fpl(tlist):
	return tlist[0] + len(tlist)
#print(fpl([1, 2, 3, 4, 5]))

def greater(arr):
	newArr = []
	count = 0
	for i in range(len(arr)):
		if arr[i] > arr[1]:
			count += 1		
			newArr.append(arr[i])
	if count < 2:
		return False
	else:
		print(count)
		return newArr
#print(greater([5, 2, 3, 2, 1, 4, 9]))

def tltv(size, val):
	newArr = []
	for i in range(size):
		newArr.append(val)
	return newArr
print(tltv(4, 7))

	