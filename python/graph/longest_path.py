# https://www.structy.net/problems/premium/longest-path

def longest_path(graph):
  max_path = 0
  if not graph:
    return max_path

  for node in graph.keys():
    stack = [(node, 0)]
    while stack:
      current, path_len = stack.pop()
      max_path = max(max_path, path_len)
      neighbors = graph[current]
      for neighbor in neighbors:
        stack.append((neighbor, path_len + 1))
  return max_path


def longest_path(graph):
    distance = {}
    for node in graph:
        if not graph[node]:
            distance[node] = 0

    for node in graph:
        traverse_distance(node, graph, distance)

    return max(distance.values())


def traverse_distance(node, graph, distance):
    if node in distance:
        return distance[node]

    max_length = 0
    for neighbor in graph[node]:
        max_length = max(max_length, traverse_distance(neighbor, graph, distance))

    distance[node] = max_length + 1
    return distance[node]


graph = {
    'a': ['c', 'b'],
    'b': ['c'],
    'c': [],
    'q': ['r'],
    'r': ['s', 'u', 't'],
    's': ['t'],
    't': ['u'],
    'u': []
}

longest_path(graph)  # -> 4