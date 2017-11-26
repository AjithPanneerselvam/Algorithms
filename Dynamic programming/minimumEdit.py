"""
Minimum edit - Minimum number of operations to convert a string of length 'n' to a string of length 'm' or vice-versa.
The operations can be - Insert, Replace, Delete

Time Complexity - O(n*m)
Space Complexity - O(n*m)
"""

def minimumEdit(string1, string2):

    n,m = len(string1), len(string2)

    if n == 0 and m == 0:
        return 0
    elif n == 0:
        return m
    elif m == 0:
        return n
    else:
        dyn_array = [[] for i in range(n+1)]

        for i in range(n+1):
            dyn_array[i].append(i)
        for j in range(1,m+1):
            dyn_array[0].append(j)

        for i in range(1,n+1):
            for j in range(1,m+1):
                if string1[i-1] == string2[j-1]:
                    dyn_array[i].append(dyn_array[i-1][j-1])
                else:
                    dyn_array[i].append(1 + min(
                    dyn_array[i-1][j-1], #Replace
                    dyn_array[i-1][j], #Delete
                    dyn_array[i][j-1] #Insert
                    ))

        return dyn_array[n][m]


                                    ### Testcases ###
# print minimumEdit("ajith", "ajatp")
# print minimumEdit("Microsoft", "Macrohard")
