def parse_graph():
    def parse_edge():
        edge = input().split(" -> ")
        return int(edge[0]), sorted([int(x) for x in edge[1].split(",")], reverse=True)
    graph = dict()
    v, ws = parse_edge()
    graph[v] = ws
    try:
        while True:
            v, ws = parse_edge()
            graph[v] = ws
    except:
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


def print_cycle(cycle):
    print("->".join([str(v) for v in cycle]))

def vertex_count(graph):
    count = max(graph.keys())
    for _, ws in graph.items():
        count = max(count, *ws)
    return count + 1

def add_fake_edge(graph):
    degrees = [0] * vertex_count(graph)
    for v, ws in graph.items():
        degrees[v] -= len(ws)
        for w in ws:
            degrees[w] += 1
    return [degrees.index(1), degrees.index(-1)]

graph = parse_graph()
[start, end] = add_fake_edge(graph)
try:
    graph[start].append(end)
except:
    graph[start] = [end]
print_cycle(eulerian_path(graph, [start, end]))
