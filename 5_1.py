dna = input()
k = int(input())
matrix = {}
matrix['A'] = [float(a) for a in input().split()]
matrix['C'] = [float(a) for a in input().split()]
matrix['G'] = [float(a) for a in input().split()]
matrix['T'] = [float(a) for a in input().split()]
max_prob = 0
max_k_mer = ''
for i in range(len(dna) - k + 1):
    k_mer = dna[i:i + k]
    prob = 1
    for j, elem in enumerate(k_mer):
        prob *= matrix[elem][j]
    if prob > max_prob:
        max_prob = prob
        max_k_mer = k_mer
print(max_k_mer)