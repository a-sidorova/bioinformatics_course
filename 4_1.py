def get_hamming_dist(lhs, rhs):
    return len([i for i in range(len(lhs)) if lhs[i] != rhs[i]])

def pattern_appears(pattern, text, d):
    k = len(pattern)
    l = len(text)
    for i in range(0, l-k+1):
        if get_hamming_dist(pattern, text[i:i+k]) <= d:
            return True
    return False 

def get_imm_patterns(pattern):
    neighbor = set()
    nset = {'A', 'C', 'G', 'T'}
    for i in range(len(pattern)):
        for n in nset:
            neighbor.add(pattern[:i]+n+pattern[i+1:])
    return neighbor

def get_neighbors(pattern, d):
    tmp = get_imm_patterns(pattern)
    neighbor = tmp
    for j in range(d-1):
        for p in tmp:
            neighbor = neighbor.union(get_imm_patterns(p))
        tmp = neighbor
    return neighbor

def motif_enumeration(dna, k, d):
    patterns = set()
    neighbor = set()
    text = dna[0]
    for i in range(len(text)-k+1):
        new = get_neighbors(text[i:i+k], d)
        neighbor = neighbor.union(new)
    for n in neighbor:
        valid = True
        for seq in dna[1:]:
            if not pattern_appears(n, seq, d):
                valid = False
                break
        if valid:
            patterns.add(n)
    return patterns        


[k, d] = list(map(int, input().split()))
dna = []
while True:
    try:
        seq = input()
    except:
        break
    dna.append(str(seq))
p = motif_enumeration(dna, k, d)
print(' '.join(sorted(p)))
