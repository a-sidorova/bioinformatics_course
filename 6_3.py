import numpy as np

result = []

def lcs(v, w):
    v_size = len(v)
    w_size = len(w)
    s = np.zeros([v_size + 1, w_size + 1])
    backtrack = np.zeros([v_size + 1, w_size + 1]) 
    for i in range(1, v_size + 1):
        for j in range(1, w_size + 1):
            s[i, j] = max([s[i - 1, j], s[i, j - 1], s[i - 1, j - 1] + 1 if v[i - 1] == w[j - 1] else s[i - 1, j - 1]])
            if s[i, j] == s[i - 1, j]:
                backtrack[i, j] = 1  # down
            elif s[i, j] == s[i, j - 1]:
                backtrack[i, j] = 2  # right
            elif s[i, j] == s[i - 1, j - 1] + 1 and v[i - 1] == w[j - 1]:
                backtrack[i, j] = 3  # diag
    return backtrack


def output_cs(backtrack, v, i, j):
    if i == 0 or j == 0:
        return
    if backtrack[i, j] == 1:  # down
        output_cs(backtrack, v, i - 1, j)
    elif backtrack[i, j] == 2:  # right
        output_cs(backtrack, v, i, j - 1)
    else:  # diag
        output_cs(backtrack, v, i - 1, j - 1)
        result.append(v[i - 1])


s = str(input())
t = str(input())
backtrack = lcs(s,t)
output_cs(backtrack, s, len(s), len(t))
print("".join(result))
