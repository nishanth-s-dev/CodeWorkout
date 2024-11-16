from collections import deque, defaultdict

# https://www.structy.net/problems/shortest-path
def shortest_path(edges, src, dst):
    visited = set()
    graph = build_graph(edges)
    return explore(graph, visited, src, dst)


def explore(graph, visited, src, dst):
    queue = deque([(src, 0)])
    while queue:
        current_node, current_length = queue.popleft()
        visited.add(current_node)
        if current_node == dst:
            return current_length
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                queue.append((neighbor, current_length + 1))
    return -1

def build_graph(edges):
    graph = defaultdict(list)

    for first_node, second_node in edges:
        if second_node not in graph[first_node]:
            graph[first_node].append(second_node)
        if first_node not in graph[second_node]:
            graph[second_node].append(first_node)

    return dict(graph)