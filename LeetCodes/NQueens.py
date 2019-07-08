def find_n_queens(n):
    solutions = []
    empty_row = "." * n
    empty_board = [empty_row] * n

    def find_queens_helper(row, n, board, solutions):
        for col in range(n):
            board[row] = "." * n
            if check_if_valid(row, col, board):
                cur_row = board[row]
                cur_row = cur_row[:col] + "Q" + cur_row[col + 1:]
                board[row] = cur_row
                if row + 1 == n:
                    solutions += [board.copy()]
                else:
                    find_queens_helper(row + 1, n, board, solutions)

    def check_if_valid(row, col, board):
        if row == 0:
            return True
        else:
            # check above
            for r in range(row):
                if board[r][col] == "Q":
                    return False

            for i in range(0, row):
                i = i+1
                if col >= i:
                    if board[row - i][col - i] == "Q":
                        return False
                if col + i < len(board):
                    if board[row - i][col + i] == "Q":
                        return False
            return True

        # will need to check most recent row

    find_queens_helper(0, n, empty_board, solutions)
    return solutions


print(find_n_queens(5))
