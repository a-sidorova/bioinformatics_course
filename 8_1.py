k, t = int(input()), str(input())
print("\n".join(sorted([t[i:i+k] for i in range(len(t) - k + 1)])))