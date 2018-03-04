def isPal(s):
    i = 0
    j = len(s)-1

    while(i < j):
        if(s[i] != s[j]):
            return 0
        i += 1
        j -= 1
    return 1


def createTable(s):
    n = len(s)
    rows = [0 for i in range(n)]
    T = []
    for i in range(n):
        T.append(rows)
    return T


def palPartition(s):
    if (len(s) == 0):
        return 0
    T  = createTable(s)
    n = len(s)

    for l in range(n):
        for i in range(n - l):
            j = i + l

            if(isPal(s[i:j+1])):
                T[i][j] = 0
                continue
            for k in range(i, j):
                # This is the correct one
                if (T[i][j] == 0):
                    T[i][j] = 1 + T[i][k] + T[k+1][j]
                else:
                    T[i][j] = min(T[i][j], 1 + T[i][k] + T[k+1][j])


    # print (T)
    return T[0][n-1]


print(palPartition("ababbb"))
print(palPartition(""))
print(palPartition("ababbbabbababa"))
