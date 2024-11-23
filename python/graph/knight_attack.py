from collections import deque

def knight_attack(n, kr, kc, pr, pc):
    board = [[0] * n for i in range(n)]
    # board[kr][kc] = "K"
    board[pr][pc] = "P"

    visited = set()

    queue = deque([(kr, kc, 0)])
    while queue:
        current_kr, current_kc, distance = queue.popleft()
        if (current_kr, current_kc) in visited:
            continue
        visited.add((current_kr, current_kc))

        if board[current_kr][current_kc] == "P":
            return distance

        deltas = [(2, -1), (2, 1), (-2, -1), (-2, 1), (1, -2), (1, 2), (-1, 2), (-1, -2)]
        for delta in deltas:
            delta_row, delta_col = delta
            current_row, current_col = current_kr + delta_row, current_kc + delta_col
            if is_inbounds(board, current_row, current_col):
                queue.append((current_row, current_col, distance + 1))

    return None


def is_inbounds(grid, row, col):
    row_inbounds = 0 <= row < len(grid)
    col_inbounds = 0 <= col < len(grid[0])
    return row_inbounds and col_inbounds


# Without board
def knight_attack(n, kr, kc, pr, pc):
    visited = set()
    queue = deque([(kr, kc, 0)])

    while queue:
        row, col, distance = queue.popleft()

        if (row, col) in visited:
            continue

        if (row, col) == (pr, pc):
            return distance

        visited.add((row, col))
        neighbors = get_knight_moves(n, row, col)

        for neighbor in neighbors:
            neighbor_row, neighbor_col = neighbor
            queue.append((neighbor_row, neighbor_col, distance + 1))


def get_knight_moves(n, r, c):
    positions = [
        (r + 2, c + 1),
        (r - 2, c + 1),
        (r + 2, c - 1),
        (r - 2, c - 1),
        (r + 1, c + 2),
        (r - 1, c + 2),
        (r + 1, c - 2),
        (r - 1, c - 2),
    ]
    inbound_positions = []
    for position in positions:
        current_row, current_col = position
        if is_inbounds(n, current_row, current_col):
            inbound_positions.append(position)
    return inbound_positions


def is_inbounds(n, row, col):
    row_inbounds = 0 <= row < n
    col_inbounds = 0 <= col < n
    return row_inbounds and col_inbounds


print(knight_attack(8, 1, 1, 2, 2))  # -> 2