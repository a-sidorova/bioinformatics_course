pattern = input()
genome = input()
count = 0
for i in range(len(genome)):
    if genome[i:i+len(pattern)] == pattern:
        count += 1
print(count)