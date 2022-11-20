def most_probable_k_mer(dna, k, profile):
    max_prob = 0
    max_k_mer = dna[:k]
    for i in range(len(dna) - k + 1):
        k_mer = dna[i:i + k]
        prob = 1
        for j, elem in enumerate(k_mer):
            prob *= profile[elem][j]
        if prob > max_prob:
            max_prob = prob
            max_k_mer = k_mer
    return max_k_mer

def find_profile(motifs):
    nucls = ["A", "C", "G", "T"]
    size = len(motifs[0])
    count = len(motifs)
    profile = {nucle: [1] * size for nucle in nucls}
    for i in range(count):
        for j in range(size):
            profile[motifs[i][j]][j] += 1
    for i in nucls:
        for j in range(size):
            profile[i][j] = profile[i][j] / (count + 4)
    return profile

def score(motifs):
    score = 0
    count = len(motifs)
    size = len(motifs[0])
    for j in range(size):
        value = 0
        values = {i: 0 for i in ["A", "C", "G", "T"]}
        for i in range(count):
            values[motifs[i][j]] += 1
            value += 1
        score += value - max(values.values())
    return score

def greedy_motif_search(dna_seqs, k, t):
    best_motifs = []
    for dna in dna_seqs:
        best_motifs.append(dna[:k])
    for i in range(len(dna_seqs[0]) - k + 1):
        motifs = [dna_seqs[0][i:i+k]]
        for j in range(1, t):
            motifs.append(most_probable_k_mer(dna_seqs[j], k, find_profile(motifs)))
        if score(motifs) < score(best_motifs):
            best_motifs = motifs
    return best_motifs


k, t = [int(a) for a in input().split()]
dna_seqs = []
for i in range(t):
    dna_seqs.append(input())
best_motifs = greedy_motif_search(dna_seqs, k, t)
print("\n".join(best_motifs))
