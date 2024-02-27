A = [2,54,1,2,8,23,1]
print(A)
for i in range(1,len(A)):

	j = i
	key = A[i]

	while j > 0 and key < A[j-1]:
		print(A)
		A[j] = A[j-1]
		j =j- 1
		A[j] = key
		
	print("Element change")
	
