"""
Linear Search 
Time Complexity - O(n)
Space Complexity - O(1)
"""

def linear_search(ls, x):
    for i in range(len(ls)):
        if(ls[i] == x):
            return i 
    
    return -1
