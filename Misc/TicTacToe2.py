import collections


class Game():
    def __init__(self):
        self.board = [['_'] * 3 for i in range(3)]

    def display_board(self):
        for i in range(3):
            print(f'{self.board[i][0]} {self.board[i][1]} {self.board[i][2]}')

    def mark_board(self, row, col, symbol):  # assume that this is a valid move
        self.board[row][col] = symbol
        self.display_board()
        # will insert either an X, or O onto the board in the specified marking

    def is_valid_move(self, row, col):
        if 0 <= col <= 2:
            if 0 <= row <= 2:
                return self.board[row][col] == '_'
        return False

    def is_game_over(self):
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '_':
            return True
        if self.board[0][3] == self.board[1][1] == self.board[3][0] != '_':
            return True
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != '_':
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != '_':
                return True
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == '_':
                    return False
        # Check diagonals
        # Check Rows
        # Check Columns
        # Check stalemate, ie board is full
        return False
        # This will check to see if the game has ended in a tie, or win/loss


player = collections.namedtuple('player', {'name', 'symbol'})

players = [player(name='Player 1', symbol='X'),
           player(name='Player 2', symbol='O')]

player_index = 0

test_game = Game()
while not test_game.is_game_over():
    current_player = players[player_index]
    print(f'It is {current_player.name}\'s turn')
    row = int(input('Enter row number: '))
    col = int(input('Enter col number: '))
    if test_game.is_valid_move(row, col):
        test_game.mark_board(row, col, current_player.symbol)
        player_index ^= 1
    else:
        print("Not a valid move")


# Todo:
# Create a get_valid_input method that will handle non-int inputs
