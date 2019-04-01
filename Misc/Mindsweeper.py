import collections
import random


class Game:
    def __init__(self, size):
        self.board = [['_'] * size for i in range(size)]
        self.answer_board = [[0] * size for i in range(size)]
        self.generate_board()
        self.size = size
        self.game_over = False
        self.reveal_queue = collections.deque()
        self.bombs_marked = 0

    def generate_board(self):
        self.num_bombs = int((size * size) / 10)
        bombs_added = 0
        while bombs_added < self.num_bombs:
            row = random.randrange(size-1)
            col = random.randrange(size-1)
            if self.answer_board[row][col] != -1:
                self.add_bomb(row, col)
                bombs_added += 1

    def add_bomb(self, row, col):
        self.answer_board[row][col] = -1
        for temp_row, temp_col in self.adjacent_squares(row, col):
            if self.answer_board[temp_row][temp_col] != -1:
                self.answer_board[temp_row][temp_col] += 1

    # Safely returns the adjacent squares, checking for edge cases
    def adjacent_squares(self, row, col):
        results = []
        for i in range(-1, 2):
            temp_row = row + i
            if 0 <= temp_row < size:
                for j in range(-1, 2):
                    temp_col = col + j
                    if 0 <= temp_col < size:
                        results.append((temp_row, temp_col))
        return results

    def display_board(self):
        for i in range(self.size):
            row = ""
            for j in range(self.size):
                row = row + " " + self.board[i][j]
            print(row[1:])

    def mark_bomb(self, row, column):
        self.board[row][column] = "B"
        self.bombs_marked += 1
        if self.bombs_marked == self.num_bombs:
            self.game_over = True

    def reveal_square(self):
        row, column = self.reveal_queue.popleft()
        if self.answer_board[row][column] == -1:
            print("That is a bomb! You have lost")
            self.game_over = True
        elif self.answer_board[row][column] != 0:
            self.board[row][column] = str(self.answer_board[row][column])
        else:
            self.board[row][column] = " "
            for adj_row, adj_col in self.adjacent_squares(row, column):
                if self.board[adj_row][adj_col] == "_":
                    if self.answer_board[adj_row][adj_col] != -1:
                        self.reveal_queue.append((adj_row, adj_col))

    def make_move(self, row, column):
        self.reveal_queue.append((row, column))
        while len(self.reveal_queue) >= 1:
            self.reveal_square()

    def check_win(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == "B" and self.answer_board[i][j] != -1:
                    return False
        return True

    # requires some logic to reveal necessary squares
    # I think I should use a queue to walk through and
    # Reveal adjacent squares that are either blank or #s


size = int(input("How large would you like the square to be? "))
game = Game(size)

while (not game.game_over):
    command = input("Would you like to 1) mark a bomb or 2) reveal a square? ")
    row = int(input("Row: "))
    col = int(input("Col: "))
    if command == "1":
        game.mark_bomb(row, col)
    if command == "2":
        game.make_move(row, col)
    game.display_board()
"""
_ = undiscovered
0 = clear
B = bomb
1 = touches 1 bomb
2 - touches 2 bombs, etc


B 1 0 2 B
1 2 2 3 B
0 1 B B 2
0 1 2 2 1
"""


"""

Notes to self:
I need to be careful of going off the edge with my range(-1, 2) markings...
It would also be useful to check a valid move... i.e. that row and column are in the range
It would be simple to add an un-mark feature to remove 

"""
