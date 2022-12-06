import numpy as np

BLOSUM_62 = [
    [ 4,  0, -2, -1, -2,  0, -2, -1, -1, -1, -1, -2, -1, -1, -1,  1,  0,  0, -3, -2],
    [ 0,  9, -3, -4, -2, -3, -3, -1, -3, -1, -1, -3, -3, -3, -3, -1, -1, -1, -2, -2],
    [-2, -3,  6,  2, -3, -1, -1, -3, -1, -4, -3,  1, -1,  0, -2,  0, -1, -3, -4, -3],
    [-1, -4,  2,  5, -3, -2,  0, -3,  1, -3, -2,  0, -1,  2,  0,  0, -1, -2, -3, -2],
    [-2, -2, -3, -3,  6, -3, -1,  0, -3,  0,  0, -3, -4, -3, -3, -2, -2, -1,  1,  3],
    [ 0, -3, -1, -2, -3,  6, -2, -4, -2, -4, -3,  0, -2, -2, -2,  0, -2, -3, -2, -3],
    [-2, -3, -1,  0, -1, -2,  8, -3, -1, -3, -2,  1, -2,  0,  0, -1, -2, -3, -2,  2],
    [-1, -1, -3, -3,  0, -4, -3,  4, -3,  2,  1, -3, -3, -3, -3, -2, -1,  3, -3, -1],
    [-1, -3, -1,  1, -3, -2, -1, -3,  5, -2, -1,  0, -1,  1,  2,  0, -1, -2, -3, -2],
    [-1, -1, -4, -3,  0, -4, -3,  2, -2,  4,  2, -3, -3, -2, -2, -2, -1,  1, -2, -1],
    [-1, -1, -3, -2,  0, -3, -2,  1, -1,  2,  5, -2, -2,  0, -1, -1, -1,  1, -1, -1],
    [-2, -3,  1,  0, -3,  0,  1, -3,  0, -3, -2,  6, -2,  0,  0,  1,  0, -3, -4, -2],
    [-1, -3, -1, -1, -4, -2, -2, -3, -1, -3, -2, -2,  7, -1, -2, -1, -1, -2, -4, -3],
    [-1, -3,  0,  2, -3, -2,  0, -3,  1, -2,  0,  0, -1,  5,  1,  0, -1, -2, -2, -1],
    [-1, -3, -2,  0, -3, -2,  0, -3,  2, -2, -1,  0, -2,  1,  5, -1, -1, -3, -3, -2],
    [ 1, -1,  0,  0, -2,  0, -1, -2,  0, -2, -1,  1, -1,  0, -1,  4,  1, -2, -3, -2],
    [ 0, -1, -1, -1, -2, -2, -2, -1, -1, -1, -1,  0, -1, -1, -1,  1,  5,  0, -2, -2],
    [ 0, -1, -3, -2, -1, -3, -3,  3, -2,  1,  1, -3, -2, -2, -3, -2,  0,  4, -3, -1],
    [-3, -2, -4, -3,  1, -2, -2, -3, -3, -2, -1, -4, -4, -2, -3, -3, -2, -3, 11,  2],
    [-2, -2, -3, -2,  3, -3,  2, -1, -2, -1, -1, -2, -3, -1, -2, -2, -2, -1,  2,  7]
]

IDXS = {
    '-':  0, 'A':  1, 'C':  2, 'D':  3, 'E':  4, 'F':  5, 'G':  6, 
    'H':  7, 'I':  8, 'K':  9, 'L': 10, 'M': 11, 'N': 12, 'P': 13, 
    'Q': 14, 'R': 15, 'S': 16, 'T': 17, 'V': 18, 'W': 19, 'Y': 20 
}

SIGMA = 5

def lcs(v, w):
    v_size = len(v)
    w_size = len(w)
    s = np.zeros([v_size + 1, w_size + 1], dtype=int)
    backtrack = np.zeros([v_size + 1, w_size + 1])
    for i in range(1, v_size + 1):
        s[i][0] = s[i - 1][0] - SIGMA
        backtrack[i][0] = 1  # down
    for j in range(1, w_size + 1):
        s[0][j] = s[0][j - 1] - SIGMA
        backtrack[0][j] = 2  # right
    for i in range(1, v_size + 1):
        for j in range(1, w_size + 1):
            s[i, j] = max([s[i - 1, j] - SIGMA,
                           s[i, j - 1] - SIGMA,
                           s[i - 1][j - 1] + BLOSUM_62[IDXS[v[i - 1]] - 1][IDXS[w[j - 1]] - 1]])
            if s[i, j] == s[i - 1, j] - SIGMA:
                backtrack[i, j] = 1  # down
            elif s[i, j] == s[i, j - 1] - SIGMA:
                backtrack[i, j] = 2  # right
            else:
                backtrack[i, j] = 3  # diag
    return backtrack, s[v_size][w_size]


def output_cs(backtrack, v, w, i, j, v_result, w_result):
    if i == 0 and j == 0:
        return v_result, w_result
    if backtrack[i, j] == 1:  # down
        v_result += v[i - 1]
        w_result += '-'
        return output_cs(backtrack, v, w, i - 1, j, v_result, w_result)
    elif backtrack[i, j] == 2:  # right
        v_result += '-'
        w_result += w[j - 1]
        return output_cs(backtrack, v, w, i, j - 1, v_result, w_result)
    else:  # diag
        v_result += v[i - 1]
        w_result += w[j - 1]
        return output_cs(backtrack, v, w, i - 1, j - 1, v_result, w_result)


s = str(input())
t = str(input())
backtrack, score = lcs(s, t)
s_result, t_result = "", ""
s_result, t_result = output_cs(backtrack, s, t, len(s), len(t), s_result, t_result)
print(score)
print(s_result[::-1])
print(t_result[::-1])
