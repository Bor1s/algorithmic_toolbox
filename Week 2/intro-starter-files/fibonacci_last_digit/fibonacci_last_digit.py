# Uses python3
import sys

def get_fibonacci_last_digit(n):
    # write your code here
    if (n <= 1):
        return n
    f = []
    f.append(0)
    f.append(1)
    for i in range(2,n+1):
        f.append(divmod(f[i-1] + f[i-2],10)[1])
    return f[n]

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    if (n >= 0) and (n <= 10**7):
        print(get_fibonacci_last_digit(n))
