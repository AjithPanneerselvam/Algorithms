"""
Dynamic Programming - 0/1 Knapsack Problem

Input:
 Values (stored in array v)
 Weights (stored in array w)
 Number of distinct items (n)
 Knapsack capacity (W)

Time Complexity - O(nW)
Space Complexity - O(nW)

Reference : https://en.wikipedia.org/wiki/Knapsack_problem
"""

def sort_list(item_values,item_weights,n):

    # Sort the items in ascending order with value/weight - Bubble Sort(Not an efficient algorithm though)
    for i in range(n-1):
        flag = False
        for j in range(n-i-1):
            if(item_weights[j] >= item_weights[j + 1]):
                if item_weights[j] == item_weights[j+1]:
                    if(item_values[j]/item_weights[j]) < (item_values[j+1]/item_weights[j+1]):
                        flag = True
                        item_values[j],item_values[j+1] = item_values[j+1], item_values[j]
                        item_weights[j],item_weights[j+1] = item_weights[j+1],item_weights[j]
                else:
                    flag = True
                    item_values[j],item_values[j+1] = item_values[j+1], item_values[j]
                    item_weights[j],item_weights[j+1] = item_weights[j+1],item_weights[j]

        if(not(flag)):
            # Sorted. It's time to break out of the loop and return!
            return

def backtrack(sack,knapsack_capacity,item_weights,n):
    j = knapsack_capacity
    indices = list()

    for i in range(n, 0, -1):
        if sack[i][j] != sack[i-1][j]:
            indices.append(i-1)
            j -= item_weights[i-1]

    return indices



def knapsack(item_weights,item_values,n,knapsack_capacity):

    sort_list(item_values, item_weights, n)

    sack = [[0] for i in range(n+1)]

    # Make all the values of the first row as zero, for intial condition
    for i in range(1,knapsack_capacity+1):
        sack[0].append(0)

    for i in range(1, n + 1):
        for j in range(1,knapsack_capacity + 1):
            if item_weights[i-1] > j:
                sack[i].append(sack[i-1][j])
            else:
                sack[i].append(max((item_values[i-1]+sack[i-1][j-item_weights[i-1]]),sack[i-1][j]))

    # print sack[n][knapsack_capacity]

    indices = backtrack(sack,knapsack_capacity,item_weights,n)
    items = list()

    for i in indices:
        items.append((item_weights[i],item_values[i]))

    return items[::-1],sack[n][knapsack_capacity]


                                ### Testcases ###
# print knapsack([3,2,1,4,5],[1,3,4,2,6],5,7)
