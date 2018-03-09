"""
Radix Sort - Linear sorting
Time Complexity - O((n+b)*log n base b), b is the base for representing numbers
Space Complexity - O(n+b)
"""

def radix(ls):
    mod = 10
    div = 1

    while True:
        aux = [[] for i in range(10)]
        for element in ls:
            digit = element % mod
            digit = int(digit / div)
            aux[digit].append(element)

        if len(aux[0]) == len(ls):
            return ls

        ls = []
        for outer in aux:
            for inner in outer:
                ls.append(inner)
        print(ls)

        div *= 10
        mod *= 10


#                                 ### Testcases ###
#
ls = [14,31,18,275,93,102,87,56]
print (radix(ls))
