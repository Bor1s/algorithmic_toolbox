# Uses python3
import sys

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

# def gcd_slow(a,b):
#     current_gcd = 1
#     for d in range(2, min(a, b) + 1):
#         if a % d == 0 and b % d == 0:
#             if d > current_gcd:
#                 current_gcd = d
#     return current_gcd

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    if (a >= 1) and (a <= 2 * 10**9) and (b >= 1) and (b <= 2 * 10**9):
        print(gcd(a, b))
