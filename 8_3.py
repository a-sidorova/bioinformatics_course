def genome(patterns):
    overlap_graph = dict.fromkeys(patterns)
    for v in overlap_graph:
        overlap_graph[v] = None
        for read in patterns:
            if read[:-1] == v[1:]:
                overlap_graph[v] = read
    return overlap_graph


patterns = []
while True:
    try:
        patterns.append(input())
    except:
        break

overlap_graph = genome(patterns)
for v in overlap_graph:
    if overlap_graph[v] is not None:
        print(v + " -> " + overlap_graph[v])
