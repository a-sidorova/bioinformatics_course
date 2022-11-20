import itertools

def get_hamming_dist(lhs, rhs):
    return len([i for i in range(len(lhs)) if lhs[i] != rhs[i]])

def get_distance(pattern, dna):
    k = len(pattern)
    distance = 0
    for seq in dna:
        hd = float('inf')
        for i in range(len(seq) - k +1):
            hd = min(hd, get_hamming_dist(pattern, seq[i:i+k]))
        distance += hd
    return distance


def get_patterns(k):
    return itertools.product('ACGT', repeat=k)
    
def median_string(dna, k):
    distance = float('inf')
    median = str()
    standarts = get_patterns(k)
    for pattern in standarts:
        d = get_distance(pattern, dna)
        if distance > d:
            distance = d
            median = "".join(pattern)
    return median


k = int(input())
dna = []
while True:
    try:
        seq = input()
    except:
        break
    dna.append(str(seq))
print(median_string(dna, k))