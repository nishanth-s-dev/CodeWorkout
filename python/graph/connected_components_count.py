# https://www.structy.net/problems/connected-components-count
def connected_components_count(graph):
    visited = set()
    count = 0
    for node in graph.keys():
        count += traverse(node, graph, visited)
    return count


def traverse(node, graph, visited):
    if node in visited:
        return 0
    neighbors = graph[node]
    visited.add(node)
    for neighbor in neighbors:
        traverse(neighbor, graph, visited)
    return 1

def traverse(node, graph, visited):
    if node in visited:
        return 0

    stack = [node]
    while stack:
        current = stack.pop(0)
        visited.add(current)

        neighbors = graph[current]
        for neighbor in neighbors:
            if neighbor not in visited:
                stack.append(neighbor)

    return 1