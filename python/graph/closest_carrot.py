from collections import deque

# https://www.structy.net/problems/premium/closest-carrot
def closest_carrot(grid, starting_row, starting_col):
    queue = deque([(starting_row, starting_col, 0)])
    visited = set()
    while queue:
        current_node = queue.popleft()
        current_row, current_col, current_path_len = current_node

        if grid[current_row][current_col] == 'C':
            return current_path_len

        visited.add((current_row, current_col))

        neighbors = get_neighbors(grid, current_node)
        for neighbor in neighbors:
            if (neighbor[0], neighbor[1]) not in visited and grid[neighbor[0]][neighbor[1]] != 'X':
                queue.append(neighbor)

    return -1


def get_neighbors(grid, node):
    row, col, current_path_len = node

    up = (row - 1, col, current_path_len + 1)
    right = (row, col + 1, current_path_len + 1)
    down = (row + 1, col, current_path_len + 1)
    left = (row, col - 1, current_path_len + 1)

    neighbors = []

    if row > 0:
        neighbors.append(up)
    if col < len(grid[row]) - 1:
        neighbors.append(right)
    if row < len(grid) - 1:
        neighbors.append(down)
    if col > 0:
        neighbors.append(left)

    return neighbors
