# Uses python3
import sys

def lcm(a, b):
    #write your code here
    _gcd = gcd(a, b)
    return (a*b) // _gcd

def gcd(a, b):
    max_number = max(a,b)
    min_number = min(a,b)
    result = max_number % min_number
    if (result == 1):
        return result
    if (result == 0):
        return min_number
    else:
        return gcd(min_number, result)

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    if (a >= 1) and (a <= 2 * 10**9) and (b >= 1) and (b <= 2 * 10**9):
        print(lcm(a, b))

