"""
text = input("enter your name: ")
print(f'Hello {text}')
"""
import collections


class game_board:
    def __init__(self):
        self.board = [['_'] * 3 for i in range(3)]

    def is_valid_move(self, row, column):
        if 0 <= row <= 2:
            if 0 <= column <= 2:
                return self.board[row][column] == '_'
        return False

    def place_marker(self, row, column, token):
        self.board[row][column] = token

    def is_game_over(self):
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '_':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != '_':
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
        return True

    def display_board(self):
        print()
        for row in self.board:
            result = f'{row[0]} {row[1]} {row[2]}'
            print(result)
        print()


def execute_move(player, game):
    print(f'It is {player.name}\'s turn')
    row = int(input('Please enter the row: '))
    column = int(input('Please enter the column: '))

    if game.is_valid_move(row, column):
        game.place_marker(row, column, player.symbol)
    else:
        print("That is not a valid move")
        execute_move(player, game)


player = collections.namedtuple("player", ("name", "symbol"))
players = {- 1: (player("Player 1", "X")), 1: (player("Player 2", "O"))}

game = game_board()
player_num = -1
while not game.is_game_over():
    current_player = players[player_num]
    game.display_board()
    execute_move(current_player, game)
    player_num = player_num * -1

print("End of the game!")
game.display_board()
