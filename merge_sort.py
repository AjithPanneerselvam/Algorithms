"""
Merge sort:
Time Complexity - O(nlogn) 
Space Complexity - O(n)
"""


def mergesort(ls):

	n = len(ls)

	if  n > 1:
		A = ls[:(n/2)-1]
		B = ls[n/2: ]
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

	if i == nA:
		while j < nB:
			ls[k] = B[j]
			j += 1
			k += 1

	else:
		while i < nA:
			ls[k] = A[i]
			i += 1
			k += 1


	"""

	while i <  nA:
		ls[k] = A[i]
		i += 1
		k += 1

	while j < nB:
		ls[k] = A[j]
		j += 1
		k += 1
	"""


if __name__ == '__main__':

	# Enter the elements to be sorted
	ls = raw_input().split()
	ls = [int(i) for i in ls]
	mergesort(ls)
	print ls		# Print the sorted elements.
