from collections import deque, defaultdict


def dfs(graph, start):
    stack = [start]
    while stack:
        current = stack.pop()
        print(current, end=" ")
        for neighbor in graph[current]:
            stack.append(neighbor)
    print()


def dfsRecursive(graph, start):
    print(start, end=" ")
    for neighbor in graph[start]:
        dfsRecursive(graph, neighbor)


def bfs(graph, start):
    queue = deque([start])
    while queue:
        current = queue.popleft()
        print(current, end=" ")
        for neighbor in graph[current]:
            queue.append(neighbor)
    print()


# https://www.structy.net/problems/has-path
def has_path(graph, src, dst):
    stack = [src]
    while stack:
        current = stack.pop()
        if current == dst:
            return True
        for neighbor in graph[current]:
            stack.append(neighbor)
    return False


def has_path(graph, src, dst):
    queue = deque([src])
    while queue:
        current = queue.popleft()
        if current == dst:
            return True
        for neighbor in graph[current]:
            queue.append(neighbor)
    return False


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


if __name__ == "__main__":
    edges = [
        ('i', 'j'),
        ('k', 'i'),
        ('m', 'k'),
        ('k', 'l'),
        ('o', 'n')
    ]
    print(undirected_path(edges, 'i', 'n'))
