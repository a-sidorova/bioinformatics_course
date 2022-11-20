translator = { "AAA":"K","AAC":"N","AAG":"K","AAU":"N","ACA":"T","ACC":"T","ACG":"T","ACU":"T","AGA":"R","AGC":"S","AGG":"R","AGU":"S","AUA":"I","AUC":"I","AUG":"M","AUU":"I","CAA":"Q","CAC":"H","CAG":"Q","CAU":"H","CCA":"P","CCC":"P","CCG":"P","CCU":"P","CGA":"R","CGC":"R","CGG":"R","CGU":"R","CUA":"L","CUC":"L","CUG":"L","CUU":"L","GAA":"E","GAC":"D","GAG":"E","GAU":"D","GCA":"A","GCC":"A","GCG":"A","GCU":"A","GGA":"G","GGC":"G","GGG":"G","GGU":"G","GUA":"V","GUC":"V","GUG":"V","GUU":"V","UAA":"","UAC":"Y","UAG":"","UAU":"Y","UCA":"S","UCC":"S","UCG":"S","UCU":"S","UGA":"","UGC":"C","UGG":"W","UGU":"C","UUA":"L","UUC":"F","UUG":"L","UUU":"F"
}
def translate(rna):
    result = []
    for i in range(0, len(rna), 3):
        pattern = rna[i:i+3]
        result.append(translator[pattern])
    return "".join(result)

dna = input()
peptide = input()
step = len(peptide) * 3
result = []
for i in range(len(dna) - step + 1):
    pattern = dna[i:i+step]
    before = list(pattern[::-1])
    pattern = pattern.replace('T', 'U')
    for j in range(len(before)):
        if before[j] == 'A':
            before[j] = 'T'
        elif before[j] == 'T':
            before[j] = 'A'
        elif before[j] == 'G':
            before[j] = 'C'
        else:
            before[j] = 'G'
    before = "".join(before).replace('T', 'U')
    if (translate(before) == peptide or translate(pattern) == peptide):
        print(dna[i:i+step])