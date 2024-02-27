# Using TEMP Variable

# A = [2,8,5,3,9,4,12,14,11,22,19,18,5]

# for i in range(1,len(A)):

# 	j = i

# 	while j > 0 and A[j-1] > A[j]:
# 		temp = A[j-1]
# 		A[j-1] = A[j]
# 		A[j] = temp
# 		j = j-1
# print(A)


# Without using TEMP Variable

A = [2,8,5,3,9,4]

print(A)
for i in range(1,len(A)):

	j = i
	key = A[i]

	while j > 0 and A[j-1] > key:
		A[j] = A[j-1]
		j = j-1
		A[j] = key
print(A)
