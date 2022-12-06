import numpy as np


def score(s, t):
    s_size, t_size = len(s), len(t)
    score = np.zeros([s_size + 1, t_size + 1], dtype=int)
    for i in range(1, s_size + 1):
        score[i][0] = score[i - 1][0] + 1
    for j in range(1, t_size + 1):
        score[0][j] = score[0][j - 1] + 1
    for i in range(1, s_size + 1):
        for j in range(1, t_size + 1):
            score[i][j] = min(
                score[i - 1][j] + 1,
                score[i][j - 1] + 1,
                score[i - 1][j - 1] if s[i - 2] == t[j - 2] else score[i - 1][j - 1] + 1
            )
    return score[s_size, t_size]


s = input()
t = input()
print(score(s, t))
