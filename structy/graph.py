from collections import deque

graph = {
    "a" : ["b", "c"],
    "b" : ["d"],
    "c" : ["e"],
    "d" : ["f"],
    "e" : [],
    "f" : []
}

#    a
#   / \
#  b   c
#  |   |
#  d   e
#  |
#  f

def dfs(graph, start):
    stack = [ start ]
    while stack:
        current = stack.pop()
        print(current, end = " ")
        for neighbor in graph[current]:
            stack.append(neighbor)
    print()

def dfsRecursive(graph, start):
    print(start, end = " ")
    for neighbor in graph[start]:
        dfsRecursive(graph, neighbor)

def bfs(graph, start):
    queue = deque([start])
    while queue:
        current = queue.popleft()
        print(current, end = " ")
        for neighbor in graph[current]:
            queue.append(neighbor)
    print()

if __name__ == "__main__":
    bfs(graph, "a")
    dfs(graph, "a")
    dfsRecursive(graph, "a")
