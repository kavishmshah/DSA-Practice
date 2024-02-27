def split(arr):
	
	if len(arr) <= 1:
		return 
	
	else: 
		mid = len(arr) // 2
		left = arr[0:mid]
		split(left)
		right = arr[mid:]
		split(right)
		merge(left, right, arr)
			 

def merge(left, right, sorted_arr):

	len_l = len(left)
	len_r = len(right)
	i = j = k = 0
	while i < len_l and j < len_r:
		if left[i] < right[j]:
			sorted_arr[k] = left[i]
			i += 1
		else: 
			sorted_arr[k] = right[j]
			j += 1
		k += 1 

	while i < len_l:
		sorted_arr[k] = left[i]
		i += 1
		k += 1
	
	while j < len_r:
		sorted_arr[k] = right[j]
		j += 1
		k += 1
		


if __name__ == "__main__":

	test_cases = [[1, 41, 76, 3, 2, 9, 23, 5], [1], [7,6,5,4,3],[]]
	
	for test_list in test_cases: 
		split(test_list)
		print(test_list)
