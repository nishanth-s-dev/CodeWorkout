from collections import defaultdict


# https://www.structy.net/problems/undirected-path
def undirected_path(edges, src, dst):
    graph = get_adjacency_list(edges)
    stack = [src]
    visited = set()
    while stack:
        current = stack.pop()
        visited.add(current)

        if current == dst:
            return True
        for neighbor in graph[current]:
            if neighbor not in visited:
                stack.append(neighbor)
    return False


def get_adjacency_list(edges):
    graph = defaultdict(list)
    for first_node, second_node in edges:
        if second_node not in graph[first_node]:
            graph[first_node].append(second_node)
        if first_node not in graph[second_node]:
            graph[second_node].append(first_node)
    return dict(graph)