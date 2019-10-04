#1
def Biggie(arr):
	for i in range(len(arr)):
		if arr[i] > 0:
			arr[i] = "big"
	return arr		
#print(Biggie([-1, 3, 5, -5]))
#2 
def Count(arr):
	count = 0
	for i in range(len(arr)):
		if arr[i] > 0:
			count += 1
	arr[len(arr)-1] = count
	return arr
#print(Count([-1,1,1,1]))		
#3
def SumT(arr):
	sum = 0
	for i in range(len(arr)):
		sum += arr[i]
	return sum
#print(SumT([1, 2, 3, 5]))
#4
def Average(arr):
	sum = 0
	for i in range(len(arr)):
		sum += arr[i]
	average = sum / len(arr)
	return average
#print(Average([2, 4, 9, 5]))
#5
def Length(arr):
	return len(arr)
#print(Length([37, 2, 1, -9]))
#6
def Minimum(arr):
	min = arr[0]
	if len(arr) == 0:
		return false
	else:
		for i in range(len(arr)):
			if min > arr[i]:
				min = arr[i]
	return min
#print(Minimum([3, 2, 9, 1]))
#7
def Maximum(arr):
	max = arr[0]
	if len(arr) == 0:
		return false
	else:
		for i in range(len(arr)):
			if max < arr[i]:
				max = arr[i]
	return max
#print(Maximum([3, 2, 9, 1]))
#8
def Ultimate(arr):
	sum = 0
	max = arr[0]
	min = arr[0]
	length = len(arr)
	for i in range(length):
		sum += arr[i]
		if max < arr[i]:
			max = arr[i]
		if min > arr[i]:
			min = arr[i]
	avg = sum / length
	newDict = {
		'sumTotal': sum,
		'average': avg,
		'minimum': min,
		'maximum': max,
		'length': length
	}
	return newDict
#print(Ultimate([3, 7, 1, 9, 5]))
#9
def Reverse(arr):
	j = len(arr)-1
	a = int(len(arr)/2)
	for i in range(a):
		temp = arr[i]
		arr[i] = arr[j]
		arr[j] = temp
		j -= 1
		return arr
print(Reverse([1, 2, 3, 4]))






	


