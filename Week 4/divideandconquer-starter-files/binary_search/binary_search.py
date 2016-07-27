# Uses python3
import sys

def binary_search(a, x):
    left, right = 0, len(a)-1
    length = len(a)
    while length >= 1:
        half_idx = (right - left) // 2 + left
        half_element = a[half_idx]
        if x == half_element:
            return half_idx
        elif x > half_element:
            left = half_idx+1
            length = right - half_idx
        elif x < half_element:
            right = half_idx
            length = right - left
    return -1


def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        # print(linear_search(a, x), end = ' ')
        print(binary_search(a, x), end = ' ')
