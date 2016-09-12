"""
Print all the string permutations using backtracking
"""
def permutations(string,index,size):

	if index == size:
		print ''.join(string)
		return

	for i in range(index,size):
		string[i], string[index] = string[index], string[i]
		permutations(string,index+1,size,itr)
		string[i], string[index] = string[index], string[i]

if __name__ == '__main__':
	string = raw_input()
	string = list(string)
	size = len(string)
	print permutations(string,0,size,0)
