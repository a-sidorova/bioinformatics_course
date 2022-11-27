import sys

money = int(input())
coins = [int(coin) for coin in input().split(',')]
count = len(coins)

table = [sys.maxsize for i in range(money + 1)]
table[0] = 0

for i in range(1, money + 1):
    for coin in coins:
        if coin <= i:
            sub_res = table[i - coin]
            if (sub_res != sys.maxsize and sub_res + 1 < table[i]):
                table[i] = sub_res + 1
print(table[money])
