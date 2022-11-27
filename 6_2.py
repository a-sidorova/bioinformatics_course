import copy

def manhattan_tourist(n, m, down, right):
    row = [0 for _ in range(m + 1)]
    s = [copy.copy(row) for _ in range(n+1)]

    for i in range(1, n):
        s[i][0] = s[i-1][0] + down[i - 1][0]
    for j in range(1, m):
        s[0][j] = s[0][j-1] + right[0][j - 1]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            s[i][j] = max(s[i-1][j] + down[i-1][j], s[i][j-1]+right[i][j-1])
    return s[n][m]
n, m = [int(p) for p in input().split()]
down = []
right = []
for _ in range(n):
    down.append([int(v) for v in input().split()])
input()
for _ in range(n + 1):
    right.append([int(v) for v in input().split()])
print(manhattan_tourist(n, m, down, right))
