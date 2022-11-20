translator = {'G':57,'A':71,'S':87,'P':97,'V':99,'T':101,'C':103,'I':113,'L':113,'N':114,'D':115,'K':128,'Q':128,'E':129,'M':131,'H':137,'F':147,'R':156,'Y':163,'W':186}

def get(peptide: list):
    mass = 0
    for c in peptide:
        mass += translator[c]
    return mass

peptide = list(input())
spectrum = list(map(int, input().split()))

count = len(peptide)
result = [0, get(peptide)]
cycle = [*peptide, *peptide]
for i in range(count):
    part = list()
    for j in range(i, i + count - 1):
        part.append(cycle[j])
        result.append(get(part))

score = 0
for x in result:
    if x in spectrum:
        score += 1
        spectrum.remove(x)
print(score)
