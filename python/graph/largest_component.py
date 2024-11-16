from collections import deque


# https://www.structy.net/problems/largest-component
def largest_component(graph):
    visited = set()
    count = 0
    for node, neighbors in graph.items():
        count = max(explore(node, graph, visited), count)
    return count


def explore(node, graph, visited):
    if node in visited:
        return 0
    count = 0

    queue = deque([node])
    while queue:
        current = queue.popleft()
        if current in visited:
            continue
        count += 1
        visited.add(current)

        neighbors = graph[current]
        for neighbor in neighbors:
            queue.append(neighbor)
    return count


def largest_component(graph):
    visited = set()
    largest = 0
    for node in graph.keys():
        largest = max(largest, explore(node, graph, visited))
    return largest


def explore(node, graph, visited):
    if node in visited:
        return 0
    size = 1
    visited.add(node)
    for neighbor in graph[node]:
        size += explore(neighbor, graph, visited)
    return size
