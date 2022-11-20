mass = int(input())
masses = [57, 71, 87,97,99,101,103,113,114,115,128,129,131,137,147,156,163,186]
fb = [0] * (mass + 1)
fb[0] = 1
for i in range(1, mass + 1):
    for j in masses:
        if i >= j:
            fb[i] += fb[i - j]
print(fb[mass])