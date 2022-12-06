import numpy as np

PAM_250 = [
    [ 2, -2,  0,  0, -3,  1, -1, -1, -1, -2, -1,  0,  1,  0, -2,  1,  1,  0, -6, -3],
    [-2, 12, -5, -5, -4, -3, -3, -2, -5, -6, -5, -4, -3, -5, -4,  0, -2, -2, -8,  0],
    [ 0, -5,  4,  3, -6,  1,  1, -2,  0, -4, -3,  2, -1,  2, -1,  0,  0, -2, -7, -4],
    [ 0, -5,  3,  4, -5,  0,  1, -2,  0, -3, -2,  1, -1,  2, -1,  0,  0, -2, -7, -4],
    [-3, -4, -6, -5,  9, -5, -2,  1, -5,  2,  0, -3, -5, -5, -4, -3, -3, -1,  0,  7],
    [ 1, -3,  1,  0, -5,  5, -2, -3, -2, -4, -3,  0,  0, -1, -3,  1,  0, -1, -7, -5],
    [-1, -3,  1,  1, -2, -2,  6, -2,  0, -2, -2,  2,  0,  3,  2, -1, -1, -2, -3,  0],
    [-1, -2, -2, -2,  1, -3, -2,  5, -2,  2,  2, -2, -2, -2, -2, -1,  0,  4, -5, -1],
    [-1, -5,  0,  0, -5, -2,  0, -2,  5, -3,  0,  1, -1,  1,  3,  0,  0, -2, -3, -4],
    [-2, -6, -4, -3,  2, -4, -2,  2, -3,  6,  4, -3, -3, -2, -3, -3, -2,  2, -2, -1],
    [-1, -5, -3, -2,  0, -3, -2,  2,  0,  4,  6, -2, -2, -1,  0, -2, -1,  2, -4, -2],
    [ 0, -4,  2,  1, -3,  0,  2, -2,  1, -3, -2,  2,  0,  1,  0,  1,  0, -2, -4, -2],
    [ 1, -3, -1, -1, -5,  0,  0, -2, -1, -3, -2,  0,  6,  0,  0,  1,  0, -1, -6, -5],
    [ 0, -5,  2,  2, -5, -1,  3, -2,  1, -2, -1,  1,  0,  4,  1, -1, -1, -2, -5, -4],
    [-2, -4, -1, -1, -4, -3,  2, -2,  3, -3,  0,  0,  0,  1,  6,  0, -1, -2,  2, -4],
    [ 1,  0,  0,  0, -3,  1, -1, -1,  0, -3, -2,  1,  1, -1,  0,  2,  1, -1, -2, -3],
    [ 1, -2,  0,  0, -3,  0, -1,  0,  0, -2, -1,  0,  0, -1, -1,  1,  3,  0, -5, -3],
    [ 0, -2, -2, -2, -1, -1, -2,  4, -2,  2,  2, -2, -1, -2, -2, -1,  0,  4, -6, -2],
    [-6, -8, -7, -7,  0, -7, -3, -5, -3, -2, -4, -4, -6, -5,  2, -2, -5, -6, 17,  0],
    [-3,  0, -4, -4,  7, -5,  0, -1, -4, -1, -2, -2, -5, -4, -4, -3, -3, -2,  0, 10]
]

IDXS = {
    '-':  0, 'A':  1, 'C':  2, 'D':  3, 'E':  4, 'F':  5, 'G':  6, 
    'H':  7, 'I':  8, 'K':  9, 'L': 10, 'M': 11, 'N': 12, 'P': 13, 
    'Q': 14, 'R': 15, 'S': 16, 'T': 17, 'V': 18, 'W': 19, 'Y': 20 
}

SIGMA = 5

def lab(v, w):
    max_score, max_i, max_j = 0, 0, 0
    v_size, w_size = len(v), len(w)
    s = np.zeros([v_size + 1, w_size + 1], dtype=int)
    backtrack = np.zeros([v_size + 1, w_size + 1])
    for i in range(1, v_size + 1):
        for j in range(1, w_size + 1):
            s[i, j] = max([0,
                           s[i - 1, j] - SIGMA,
                           s[i, j - 1] - SIGMA,
                           s[i - 1][j - 1] + PAM_250[IDXS[v[i - 1]] - 1][IDXS[w[j - 1]] - 1]])
            if max_score <= s[i, j]:
                max_score = s[i, j]
                max_i, max_j = i, j
            if s[i, j] == 0:
                backtrack[i, j] = 0
            elif s[i, j] == s[i - 1, j] - SIGMA:
                backtrack[i, j] = 1  # down
            elif s[i, j] == s[i, j - 1] - SIGMA:
                backtrack[i, j] = 2  # right
            else:
                backtrack[i, j] = 3  # diag
    return backtrack, max_score, max_i, max_j


def local_alignment(backtrack, v, w, i, j, v_result, w_result):
    if i == 0 or j == 0 or backtrack[i, j] == 0:
        return v_result, w_result
    if backtrack[i, j] == 1:  # down
        v_result += v[i - 1]
        w_result += '-'
        return local_alignment(backtrack, v, w, i - 1, j, v_result, w_result)
    elif backtrack[i, j] == 2:  # right
        v_result += '-'
        w_result += w[j - 1]
        return local_alignment(backtrack, v, w, i, j - 1, v_result, w_result)
    else:  # diag
        v_result += v[i - 1]
        w_result += w[j - 1]
        return local_alignment(backtrack, v, w, i - 1, j - 1, v_result, w_result)


s = str(input())
t = str(input())
backtrack, max_score, max_i, max_j = lab(s, t)
s_result, t_result = "", ""
s_result, t_result = local_alignment(backtrack, s, t, max_i, max_j, s_result, t_result)
print(max_score)
print(s_result[::-1])
print(t_result[::-1])
