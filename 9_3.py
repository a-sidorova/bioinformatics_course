def parse_graph():
    k = input()
    patterns = []
    try:
        while True:
            pattern = input()
            if pattern == "":
                break
            patterns.append(pattern)
    except:
        pass
    graph = dict.fromkeys(sorted([pattern[:-1] for pattern in patterns]))
    for pattern in patterns:
        try:
            graph[pattern[:-1]].append(pattern[1:])
        except:
            graph[pattern[:-1]] = [pattern[1:]]
    return graph


def edge_count(graph):
    count = 0
    for _, ws in graph.items():
        count += len(ws)
    return count

def eulerian_cycle(graph, start):
    count = edge_count(graph)
    end = graph[start].pop()
    cycle = [start, end]
    while True:
        while cycle[0] != cycle[-1] or len(graph[cycle[0]]) != 0:
            if len(graph[end]) == 0:
                cycle.append(cycle[0])
                continue
            end = graph[end].pop()
            cycle.append(end)
        if len(cycle) == count + 1:
            break
        cycle.pop()
        while len(graph[cycle[-1]]) == 0:
            cycle.insert(0, cycle.pop())
        end = cycle[-1]
    return cycle

def eulerian_path(graph, fake_edge):
    [start, end] = fake_edge
    cycle = eulerian_cycle(graph, start)
    cycle.pop()
    while not cycle[0] == end:
        cycle.insert(0, cycle.pop())
    return cycle

def add_fake_edge(graph):
    degrees = dict.fromkeys(graph.keys(), 0)
    for v, ws in graph.items():
        degrees[v] -= len(ws)
        for w in ws:
            if w not in graph.keys():
                degrees[w] = 0
            degrees[w] += 1
    start = list(degrees.keys())[list(degrees.values()).index(1)]
    end = list(degrees.keys())[list(degrees.values()).index(-1)]
    return [start, end]

def print_string(path):
    print(path[0] + "".join([pattern[-1] for pattern in path[1:]]))

graph = parse_graph()
[start, end] = add_fake_edge(graph)
try:
    graph[start].append(end)
except:
    graph[start] = [end]
print_string(eulerian_path(graph, [start, end]))
