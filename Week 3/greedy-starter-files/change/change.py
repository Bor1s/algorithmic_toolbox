# Uses python3
import sys

def get_change(n):
    #write your code here
    coins = [10,5,1]
    result_coins = []
    while n > 0:
        for coin in coins:
            subset = n - coin
            if subset >= 0:
                n = subset
                result_coins.append(coin)
                break
    return len(result_coins)

if __name__ == '__main__':
    n = int(sys.stdin.read())
    if (n >= 1) and (n <= 10**3):
        print(get_change(n))
