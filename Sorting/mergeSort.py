"""
Merge sort:
Time Complexity - O(nlogn)
Space Complexity - O(n)
"""


def mergesort(ls):
	n = len(ls)
	if  n > 1:
		A = ls[:int(n/2)]
		B = ls[int(n/2): ]
		mergesort(A)
		mergesort(B)
		merge(ls,A,B)


def merge(ls,A,B):
	i = j = k = 0
	nA = len(A)
	nB = len(B)

	while i < nA and j < nB:
		if A[i] <= B[j]:
			ls[k] = A[i]
			i += 1
		else:
			ls[k] = B[j]
			j+=1
		k += 1

	while i <  nA:
		ls[k] = A[i]
		i += 1
		k += 1

	while j < nB :
		ls[k] = B[j]
		j += 1
		k += 1


# 								### Testcases ###
# #
# ls = [4,3,1,7,8,5,2,19,15,100,95,125,11]
# mergesort(ls)
# print(ls)
