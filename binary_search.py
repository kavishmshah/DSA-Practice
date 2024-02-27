def binary_search(start, mid, end, lst, element):

	if start <= end:
		
		
		if lst[mid] == element:
			return mid

		elif lst[mid] < element:
			start = mid + 1
			mid = (start + end)//2
			return binary_search(start, mid, end, lst, element)

		elif lst[mid] > element:
			end = mid - 1
			mid = (start + end)//2
			return binary_search(start, mid, end, lst, element)	

	else: 
		return -1



if __name__ == "__main__":

	lst = [1,2,3,4,5,6,7,8,10]
	element = 4
	mid = len(lst)//2
	start = 0
	end = len(lst)-1
	pos = binary_search(start, mid, end, lst, element)
	print(pos)
