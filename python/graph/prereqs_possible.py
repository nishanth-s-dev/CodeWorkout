def prereqs_possible(num_courses, prereqs):
    visiting, visited = set(), set()
    graph = build_graph(num_courses, prereqs)
    for node in graph:
        if detect_cycle(graph, node, visiting, visited):
            return False
    return True


def detect_cycle(graph, node, visiting, visited):
    if node in visited:
        return False
    if node in visiting:
        return True

    visiting.add(node)
    for neighbor in graph[node]:
        if detect_cycle(graph, neighbor, visiting, visited):
            return True

    visiting.remove(node)
    visited.add(node)

    return False


def build_graph(length, edges):
    graph = {}

    for i in range(length):
        graph[i] = []

    for edge in edges:
        key, value = edge
        graph[key].append(value)

    return graph


numCourses = 6
prereqs = [
    (0, 1),
    (2, 3),
    (0, 2),
    (1, 3),
    (4, 5),
]
print(prereqs_possible(numCourses, prereqs))  # -> True