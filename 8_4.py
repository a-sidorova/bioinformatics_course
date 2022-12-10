k, t = int(input()), str(input())
patterns = sorted([t[i:i+k-1] for i in range(len(t) - k + 1)])
graph = dict.fromkeys(patterns)
for i in range(len(t) - k + 1):
    pattern = t[i:i+k-1]
    if graph[pattern] is None:
        graph[pattern] = [t[i+1:i+k]]
    else:
        graph[t[i:i+k-1]].append(t[i+1:i+k])

for v, ws in graph.items():
    if len(ws) == 0:
        continue
    else:
        print(v + " -> " +  ", ".join(ws))
