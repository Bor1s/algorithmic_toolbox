# Uses python3
# def calc_fib(n):
#     if (n <= 1):
#         return n
#
#     return calc_fib(n - 1) + calc_fib(n - 2)
#
# n = int(input())
# print(calc_fib(n))


h = {0: 0, 1: 1, 2: 1}
def fib(n):
    if (n >= 0) and (n <= 45):
        if (n <= 1):
            return n
        if (n not in h):
            h[n] = fib(n-1) + fib(n-2)
            return h[n]
        else:
            return h[n]

n = int(input())
print(fib(n))
