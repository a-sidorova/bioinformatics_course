translator = {'G':57,'A':71,'S':87,'P':97,'V':99,'T':101,'C':103,'I':113,'L':113,'N':114,'D':115,'K':128,'Q':128,'E':129,'M':131,'H':137,'F':147,'R':156,'Y':163,'W':186}

peptide = list(input())
count = len(peptide)
cycle = [*peptide, *peptide]
result = [peptide]
for i in range(count):
    part = list()
    for j in range(i, i + count - 1):
        part.append(cycle[j])
        result.append(part.copy())
masses = []
for i in result:
    mass = 0
    for j in i:
        mass += translator[j]
    masses.append(mass)
masses.sort()
print(0, *masses)
