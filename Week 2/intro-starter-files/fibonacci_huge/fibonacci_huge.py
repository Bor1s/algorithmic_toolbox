# Uses python3
# import sys
#
# def get_fibonaccihuge(n, m):
#     # write your code here
#     return 0
#
# if __name__ == '__main__':
#     input = sys.stdin.read();
#     n, m = map(int, input.split())
#     print(get_fibonaccihuge(n, m))

# ---------

import sys

lineIn = sys.stdin.readline().split(" ")
n = int(lineIn[0])
m = int(lineIn[1])

fibPrev = 0
fib = 1
cached = [fibPrev, fib]

for curr in range(1, n):
    print('curr =>', curr)
    print('------')
    print(fib)
    print(fibPrev)
    fibOld = fib
    fib = (fib + fibPrev) % m
    fibPrev = fibOld

    if fibPrev == 0 and fib == 1:
        print('match')
        cached.pop()
        print(cached)
        break
    else:
        cached.append(fib)
        print(cached)
        print('=====')

offset = n % len(cached)
sys.stdout.write(str(cached[offset]))
