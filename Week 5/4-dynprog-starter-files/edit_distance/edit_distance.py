# Uses python3
def edit_distance(a, b):
    # #write your code here
    # # return 0
    # d = [[0,1,2],[2],[3]]
    # n = len(s)
    # m = len(t)
    # for j in range(0, len(t)):
    #     # if not d:
    #     #     d.append([])
    #     # d[0].append(j)
    #
    #     for i in range(0, len(s)):
    #         # d.insert(i,[])
    #         # d[i].insert(0,i)
    #
    #         print('----------')
    #         print('j',j)
    #         print('i',i)
    #         insertion = d[i][j-1] + 1
    #         deletion  = d[i-1][j] + 1
    #         match     = d[i-1][j-1]
    #         mismatch  = d[i-1][j-1] + 1
    #
    #         if s[i] == t[j]:
    #             d[i][j] = min(insertion, deletion, match)
    #         else:
    #             d[i][j] = min(insertion, deletion, mismatch)
    #     print(d)
    # return d

    # "Calculates the Levenshtein distance between a and b."
    n, m = len(a), len(b)
    if n > m:
        # Make sure n <= m, to use O(min(n,m)) space
        a, b = b, a
        n, m = m, n

    current_row = range(n+1) # Keep current and previous row, not entire matrix
    for i in range(1, m+1):
        previous_row, current_row = current_row, [i]+[0]*n
        for j in range(1,n+1):
            add, delete, change = previous_row[j]+1, current_row[j-1]+1, previous_row[j-1]
            if a[j-1] != b[i-1]:
                change += 1
            current_row[j] = min(add, delete, change)

    return current_row[n]

if __name__ == "__main__":
    a = input()
    b = input()
    n = len(a)
    m = len(b)
    if (n >= 1) and (n <= 100) and (m >= 1) and (m <= 100):
        print(edit_distance(a, b))
