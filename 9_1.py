def parse_graph():
    def parse_edge():
        edge = input().split(" -> ")
        return int(edge[0]), [int(x) for x in edge[1].split(",")]
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

def eulerian_cycle(graph):
    count = edge_count(graph)
    start = next(iter(graph.keys()))
    end = graph[start].pop(0)
    cycle = [start, end]
    while True:
        while not (cycle[0] == cycle[-1] and len(graph[cycle[0]]) == 0):
            if len(graph[end]) != 0:
                end = graph[end].pop(0)
                cycle.append(end)
            else:
                cycle.append(cycle[0])
        if len(cycle) == count + 1:
            break
        while len(graph[cycle[-1]]) == 0:
            cycle.pop(0)
            cycle.append(cycle[0])
        end = cycle[-1]
    return cycle

def print_cycle(cycle):
    print("->".join([str(v) for v in cycle]))

graph = parse_graph()
print_cycle(eulerian_cycle(graph))
