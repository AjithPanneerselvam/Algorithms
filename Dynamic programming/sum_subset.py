"""
Sum of subset problems using dynamic programming

Time complexity - O(sum * size_of_subset)
Space complexity - O(sum * size_of_subset)
"""


def backtrack(matrix,subset,target):
	indices = list()
	j = target

	for i in range(len(subset),0,-1):
		if matrix[i][j] != matrix[i-1][j]:
			indices.append(i-1)
			j -= subset[i-1]

	return indices


def sum_subset(target,subset):
	n = len(subset)
	matrix = [ (target + 1) * [False] for i in range(n+1)]

	j = 0
	for i in range(n+1):
		matrix[i][j] = True

	for i in range(1,n+1):
		for j in range(1,target+1):
			if subset[i-1] > j:
				matrix[i][j] = matrix[i-1][j]
			else:
				matrix [i][j] = matrix[i-1][j-subset[i-1]]

	# print matrix
	indices = backtrack(matrix, subset, target)
	result_set = list()

	for i in indices:
		result_set.append(subset[i])

	return result_set[::-1],matrix[n][target]



								### Testcases ###
# print sum_subset(10, [1,2,3,5,7])
