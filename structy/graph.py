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

# https://www.structy.net/problems/island-count
def island_count(grid):
    visited = set()
    count = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if (row, col) not in visited:
                count += explore((row, col), grid, visited)
    return count

def explore(node, grid, visited):
    row, col = node
    if grid[row][col] == 'W':
        return 0
    stack = [ node ]
    while stack:
        current = stack.pop()
        visited.add(current)
        neighbors = get_neighbors(current, grid)
        for neighbor in neighbors:
            if neighbor not in visited:
                stack.append(neighbor)
    return 1

def get_neighbors(node, grid):
    row, col = node
    up = (row - 1, col)
    right = (row, col + 1)
    down = (row + 1, col)
    left = (row, col - 1)

    res = []
    if row > 0 and grid[row - 1][col] == 'L':
        res.append(up)
    if col < len(grid[row]) - 1 and grid[row][col + 1] == 'L':
        res.append(right)
    if row < len(grid) - 1 and grid[row + 1][col] == 'L':
        res.append(down)
    if col > 0 and grid[row][col - 1] == 'L':
        res.append(left)

    return res


grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]

count = island_count(grid) # -> 3
print(count)