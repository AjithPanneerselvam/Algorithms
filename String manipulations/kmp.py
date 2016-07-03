"""
KMP -> Knuth - Morris - Pratt
To find whether the given pattern(P) is present in the string(S), if present return the start of the index in string(S)
Brute force approach will have the runnung time complexity of O(n*m), where n and m are string S length and Pattern P length respectively.
KMP algorithm will have running time complexity of O(n+m). 
"""

# Create prefix table
def prefix_table(P,F,m):
	F.append(0)
	j = 0
	for i in range(1,m):
		if (P[j] == P[i]):
			F.append(j+1)
			i += 1
			j += 1
		elif j > 0:
			j = F[j-1]
		else:
			F.append(0) 
			i +=1

def kmp(S,P):
	
	m = len(P)
	n = len(S)
	F = []
	prefix_table(P,F,m)					# Call prefix_table function
	j = 0
	for i in range(n):
		if (S[i] == P[j]):
			if j == m-1:
				return i-j 				# return the start of the index matched in string S.
			else:
				i += 1
				j += 1
		elif j>0:
			j = F[j-1]
		else:
			i += 1

	return -1							# return -1, if no match


	
S = raw_input()
P = raw_input()
print kmp(S,P)




