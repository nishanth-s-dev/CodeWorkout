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


print(knight_attack(8, 1, 1, 2, 2))  # -> 2