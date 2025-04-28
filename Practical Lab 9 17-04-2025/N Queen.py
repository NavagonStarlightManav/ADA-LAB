def solve_n_queens(n):
    solutions = []

    def is_safe(board, row, col):
        for i in range(row):
            if board[i] == col or abs(board[i] - col) == abs(i - row):
                return False
        return True

    def solve(board, row):
        if row == n:
            solutions.append(board[:])
            return
        for col in range(n):
            if is_safe(board, row, col):
                board.append(col)
                solve(board, row + 1)
                board.pop()

    solve([], 0)
    return solutions

n = 4
result = solve_n_queens(n)
print(result)
