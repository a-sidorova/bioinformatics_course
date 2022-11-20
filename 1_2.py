text = input()
size = int(input())
k_mers = {}
for i in range(len(text) - size + 1):
    k_mer = text[i:i+size]
    if k_mer in k_mers:
        k_mers[k_mer] += 1
    else:
        k_mers[k_mer] = 0
max_count = 0
for key in k_mers:
    max_count = max(max_count, k_mers[key])
freqs = []
for k_mer in k_mers.keys():
    if k_mers[k_mer] == max_count:
        freqs.append(k_mer)
result = []
for i in range(len(text) - size + 1):
    k_mer = text[i:i+size]
    if k_mer in freqs and k_mer not in result:
        result.append(k_mer)
print(*result)