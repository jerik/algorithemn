value = 0
def sum(arr):
	global  value
	# print(f'array len: {len(arr)}')
	if len(arr) > 0:
		# elem = arr.pop()
		value += arr.pop()
		# print(elem)
		sum(arr)
	else:
		print(f'sum is {value}')
		value = 0
		

def highest(arr):
	global value
	if len(arr) > 0: 
		elem = arr.pop()
		if elem > value: 
			value = elem
		# print(elem)
		highest(arr)
	else: 
		print(f'highest is {value}')
		value = 0

def binsearch(arr, val):
	arr.sort()
	print(f'search for {val}')
	# print(arr)
	
	index = len(arr) // 2
	# print(f'index: {index}')
	if arr[index] < val:
		# print('arr-index < val')
		part = arr[index:]
		binsearch(part, val)
	if arr[index] > val: 
		# print('arr-index > val')
		lastpart = (index * -1)
		part = arr[:lastpart]
		binsearch(part, val)
	else: 
		return(print(f'Found value {arr[index]} == val {val}'))
	 
def countt(arr):
	if arr == []:
		return 0
	return 1 + countt(arr[1:])
	
def maxx(arr):
	if len(arr) == 2:
		return arr[0] if arr[0] > arr[1] else arr[1]
	sub_max = maxx(arr[1:])
	return arr[0] if arr[0] > sub_max else sub_max
	
def main():
	# sum([1,2,3,4,5])
	# highest([1,2,7,3,4,5])
	# binsearch([1,2,7,3,4,5,8,9,10,11,12,13,15,19], 4)
	# print(countt([1,2,7,3,4,5]))
	print(maxx([1,2,7,3,4,5,9,11,4,6,2,5,8,9]))
	
if __name__ == '__main__':
	main()
