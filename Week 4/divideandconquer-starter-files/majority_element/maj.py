# Uses python3
import sys

def get_majority_element(k):
    myMap = {}
    maximum = ( '', 0 ) # (occurring element, occurrences)
    for n in k:
        if n in myMap: myMap[n] += 1
        else: myMap[n] = 1

        # Keep track of maximum on the go
        if myMap[n] > maximum[1]: maximum = (n,myMap[n])

    if maximum[1] > ((len(k)) // 2):
        return 1
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if (n >= 1) and (n <= 10**5):
        if get_majority_element(a) != -1:
            print(1)
        else:
            print(0)
