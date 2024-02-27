def swap(array, start, end):
	if start != end:
		print(array, start, end)
		array[start], array[end] = array[end], array[start]	


def partition(array, start, end):
	
	pivot_index = start
	pivot = array[pivot_index]
	while  end > start:

		while array[start] <= pivot:
			start += 1

		while  array[end] > pivot:
			end -= 1

		if end > start:	
			swap(array, start, end)

	print("Pivot change")
	swap(array, pivot_index, end)
	
	return end


def quick_sort(array, start, end):
	
	if start < end:
		pi = partition(array, start, end)
		quick_sort(array, start, pi-1)
		quick_sort(array, pi+1, end)
	


if __name__ == "__main__":

	array = [4,8,1,6,3,3,5]
	start = 0
	end = len(array)-1
	quick_sort(array, start, end)
	print("Sorted Array : ", array)


