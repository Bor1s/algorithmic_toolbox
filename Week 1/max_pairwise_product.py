# Uses python3
import random
n = int(input())
a = [int(x) for x in input().split()]

# Set random values
def naive(n,a):
    result = 0

    for i in range(0, n):
        for j in range(i+1, n):
            if a[i]*a[j] > result:
                result = a[i]*a[j]

    return result

def fast(n,a):
    # Find two max values and
    # then multiply
    max_1 = 0
    for i in range(0,n):
        if a[i] > max_1:
            max_1 = a[i]
            max_1_idx = i

    max_2 = 0
    for i in range(0,n):
        if a[i] > max_2 and i != max_1_idx:
            max_2 = a[i]

    return(max_1 * max_2)


# Actual code
#n = 10000
#a = []
#for i in range(0, n):
    #a.append(random.randint(0, 10**5))

# Check for input validity
assert(len(a) == n)
assert(n >= 2)
assert(n <= 2*10**5)

# Check that range is 0 <= a0 ... an-1 <= 10**5
for i in range(0, n):
    assert(a[i] >= 0)
    assert(a[i] <= 10**5)

#naive_result = naive(n,a)
fast_result = fast(n,a)
print(fast_result)

#if naive_result != fast_result:
    #print(a)
    #print("Wrong result: naive: {naive}; fast: {fast}".format(naive = str(naive_result), fast = str(fast_result)))
#else:
    #print('Ok')
