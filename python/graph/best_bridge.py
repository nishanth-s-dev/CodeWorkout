from collections import deque


def best_bridge(grid):
    main_island = None
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            potential_island = traverse_island(grid, row, col, set())
            if len(potential_island) > 0:
                main_island = potential_island

    visited = set(main_island)
    queue = deque([])
    for pos in main_island:
        row, col = pos
        queue.append((row, col, 0))

    while queue:
        row, col, distance = queue.popleft()

        if grid[row][col] == "L" and (row, col) not in main_island:
            return distance - 1

        deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for delta in deltas:
            delta_row, delta_col = delta
            neighbor_row, neighbor_col = row + delta_row, col + delta_col
            neighbor_pos = (neighbor_row, neighbor_col)
            if is_inbounds(grid, neighbor_pos) and neighbor_pos not in visited:
                visited.add(neighbor_pos)
                queue.append((neighbor_row, neighbor_col, distance + 1))


def is_inbounds(grid, pos):
    row, col = pos
    row_inbounds = 0 <= row < len(grid)
    col_inbounds = 0 <= col < len(grid[0])
    return row_inbounds and col_inbounds


def traverse_island(grid, row, col, potential_island):
    pos = (row, col)
    if not is_inbounds(grid, pos) or grid[row][col] == 'W' or pos in potential_island:
        return potential_island

    potential_island.add(pos)

    traverse_island(grid, row - 1, col, potential_island)
    traverse_island(grid, row + 1, col, potential_island)
    traverse_island(grid, row, col + 1, potential_island)
    traverse_island(grid, row, col - 1, potential_island)

    return potential_island


grid = [
    ["W", "W", "W", "L", "L"],
    ["L", "L", "W", "W", "L"],
    ["L", "L", "L", "W", "L"],
    ["W", "L", "W", "W", "W"],
    ["W", "W", "W", "W", "W"],
    ["W", "W", "W", "W", "W"],
]
best_bridge(grid)  # -> 1