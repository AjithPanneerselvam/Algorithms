"""
Sum of subset problems using dynamic programming (To find whether the target is present as the sum of the subset given)
Time complexity - O(sum * size_of_subset)
Space complexity - O(sum * size_of_subset)
"""

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
			elif subset[i-1] == j:
				matrix[i][j] = True
			else:
				matrix [i][j] = matrix[i-1][j-subset[i-1]]
	
	return matrix[n][target]


if __name__ == '__main__':
	target = input()
	subset = []
	subset = map(int,raw_input().strip().split())
	print sum_subset(target,subset)

