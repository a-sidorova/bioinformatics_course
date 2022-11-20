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

def isConsistent(peptide, spectrum):
    linear = linearspectrum(peptide)
    for key, value in linear.items():
        if value > spectrum.get(key, 0):
            return False
    return True
    

spectrum = list(map(int, input().split()))
spectrumDict = getSpectrum(spectrum)
parentMass = max(spectrum)

peptides = {''}
result = []
while len(peptides) > 0:
    peptides = expand(peptides)
    removes = []
    for peptide in peptides:
        if getMass(peptide) == parentMass:
            if cyclospectrum(peptide) == spectrumDict:
                result.append(peptide)
            removes.append(peptide)
        elif not isConsistent(peptide, spectrumDict):
            removes.append(peptide)
    for peptide in removes:
        peptides.remove(peptide)
print(*result)
