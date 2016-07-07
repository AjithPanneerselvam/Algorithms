"""
Kadane Algorithm - Maximum sum array problem 
Time Complexity - O(n)
The original version of Kadane's algorithm works only if there's atleast one positive integer.
But the below code is modified to work for negative numbers as well.
"""

def kadane(ls,n):
	current_max = max_so_far = 0 
	negative = 1

	# To find whether there  is atleast one positive integer
	for i in range(n):					
		if ls[i] >= 0:
			negative = 0
			break 

	# If there is not even one postive integer
	if negative == 1:
		current_max = ls[0]
		for i in range(1,n):
			if ls[i] > current_max:
				current_max = ls[i]

		return current_max

	# This is the original version of Kadane Algorithm
	else:
		for i in range(n):
			current_max = current_max + ls[i]
			if current_max < 0:
				current_max = 0
			else:
				if current_max > max_so_far:
					max_so_far = current_max

	return  max_so_far

if __name__ == '__main__':
	s = raw_input()
	ls = [int(i) for i in s.split(" ")]
	n = len(ls)
	print kadane(ls,n)
