from src.model import Board

my_board = Board()
print(my_board)


my_board.cells[2].set('X')
my_board.cells[4].set('X')
my_board.cells[6].set('X')


print(my_board)

print(my_board.winner_is())

print(my_board.display_board())
