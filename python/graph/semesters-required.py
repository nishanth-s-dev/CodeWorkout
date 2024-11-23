# https://www.structy.net/problems/premium/semesters-required

def semesters_required(num_courses, prereqs):
    graph = build_graph(prereqs, num_courses)

    distance = {}
    for node in graph:
        if not graph[node]:
            distance[node] = 1

    for node in graph:
        traverse_node(node, graph, distance)
    return max(distance.values())


def build_graph(prereqs, num_courses):
    graph = {}
    for i in range(num_courses):
        graph[i] = []

    for pair in prereqs:
        start, end = pair
        graph[start].append(end)
    return graph


def traverse_node(node, graph, distance):
    if node in distance:
        return distance[node]

    max_sem = 0
    for neighbor in graph[node]:
        max_sem = max(traverse_node(neighbor, graph, distance), max_sem)
    distance[node] = max_sem + 1

    return distance[node]