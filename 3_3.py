masses = '57 71 87 97 99 101 103 113 114 115 128 129 131 137 147 156 163 186'.split()

def expand(peptides):
    expanded = set()
    for peptide in peptides:
        for mass in masses:
            expanded.add("-".join([peptide, mass])[1 if peptide == '' else 0:])
    return expanded

def translate(peptide):
    return [int(x) for x in peptide.split('-')]

def getMass(peptide):
    return sum(translate(peptide))

def getSpectrum(spectrum):
    result = dict()
    for s in spectrum:
        result[s] = result.get(s, 0) + 1
    return result
     
def cyclospectrum(peptide):
    t = translate(peptide)
    rank = len(t)
    prefix = [0]
    for i in range(rank):
        prefix.append(prefix[i] + t[i])
    peptide_mass = max(prefix)
    cspectrum = [0]
    for i in range(rank):
        for j in range(i + 1, rank + 1):
            diff = prefix[j] - prefix[i]
            cspectrum.append(diff)
            if i > 0 and j < rank:
                cspectrum.append(peptide_mass - diff)
    return getSpectrum(cspectrum)

def cycloscore(peptide, spectrum):
    if len(peptide) == 0:
        return 0
    cyclo_spectrum = cyclospectrum(peptide)
    score = 0
    for v, c in cyclo_spectrum.items():
        value = spectrum.get(v, 0)
        if value >= c:
            score += c
        else:
            score += value
    return score

def linearspectrum(peptide):
    t = translate(peptide)
    rank = len(t)
    prefix = [0]
    for i in range(rank):
        prefix.append(prefix[i] + t[i])
    lspectrum = [0]
    for i in range(rank):
        for j in range(i + 1, rank + 1):
            diff = prefix[j] - prefix[i]
            lspectrum.append(diff)
    return getSpectrum(lspectrum)

def linearscore(peptide, spectrum):
    if len(peptide) == 0:
        return 0
    linear_spectrum = linearspectrum(peptide)
    score = 0
    for v, c in linear_spectrum.items():
        value = spectrum.get(v, 0)
        if value >= c:
            score += c
        else:
            score += value
    return score

def update(leaderboard, spectrum, n):
    count = len(leaderboard)
    linears_scores = dict()
    for peptide in leaderboard:
        linears_scores[peptide] = linearscore(peptide, spectrum)
    score = sorted(linears_scores.items(), key = lambda peptide:peptide[1], reverse = True)
    leaderboard = [peptide[0] for peptide in score]
    linear_scores = [peptide[1] for peptide in score]
    for j in range(n, count):
        if linear_scores[j] < linear_scores[n - 1]:
            return leaderboard[:j]
    return leaderboard


n = int(input())
spectrum = list(map(int, input().split()))
spectrumDict = getSpectrum(spectrum)
parentMass = max(spectrum)

peptides = {''}
max_peptide = ''
max_score = 0
while len(peptides) > 0:
    peptides = expand(peptides)
    removes = []
    for peptide in peptides:
        if getMass(peptide) == parentMass:
            score = cycloscore(peptide, spectrumDict)
            if score > max_score:
                max_peptide = peptide
                max_score = score
        elif getMass(peptide) > parentMass:
            removes.append(peptide)
    for peptide in removes:
        peptides.remove(peptide)
    peptides = update(peptides, spectrumDict, n)
print(max_peptide)