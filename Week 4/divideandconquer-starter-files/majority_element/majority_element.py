# Uses python3
import sys

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]

    sorted_array = merge_sort(a)

    # Merge Sort search
    # res = 1
    # i = 0
    # while i <= len(sorted_array)-1:
    #     if i == len(sorted_array)-1:
    #         return -1
    #     if sorted_array[i] == sorted_array[i+1]:
    #         res += 1
    #         # print('i->', sorted_array[i], 'res', res)
    #         if res > (len(sorted_array) // 2):
    #             return 1
    #     else:
    #         res = 1
    #     i += 1
    # return -1

    # n**2 linear search
    # n = len(a) // 2
    # for i in range(len(a)):
    #     if (i >= 1) and (a[i] == a[i-1]):
    #         continue
    #     current_element = a[i]
    #     current_element_amount = 1
    #     for j in range(len(a)):
    #         if j <= i:
    #             continue
    #         if a[j] == current_element:
    #             current_element_amount += 1
    #     if current_element_amount > n:
    #         return 1
    # return -1

    # Merge sort approach

def merge_sort(a):
    if len(a) == 1:
        return a
    array_half = len(a) // 2
    a1 = a[:array_half]
    a2 = a[array_half:]

    _a1 = merge_sort(a1)
    _a2 = merge_sort(a2)
    # print(_a1)
    # print(_a2)
    # print('=====')
    # print(merge(_a1, _a2))
    # print('---end--')
    return merge(_a1, _a2)


def merge(a,b):
    new_array = []
    j = 0
    i = 0
    while i <= (len(a)-1):
        if a[i] < b[j]:
            new_array.append(a[i])
            if i == len(a)-1:
                new_array = new_array + b[j:]
                break
            else:
                i += 1

        elif a[i] > b[j]:
            new_array.append(b[j])
            if j == len(b)-1:
                new_array = new_array + a[i:]
                break
            else:
                j += 1

        elif a[i] == b[j]:
            new_array.append(a[i])
            new_array.append(b[j])
            if i == len(a)-1:
                new_array = new_array + b[j+1:]
                break
            else:
                i += 1
                j += 1
    return new_array

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
