from src.model import Board, HumanPlayer, ComputerPlayer


class Game:

    def __init__(self):
        self.winner = None
        self.board = Board()
        self.human = HumanPlayer()
        self.computer = ComputerPlayer()
        self.play_game()

    def play_game(self):
        playing = True
        while playing:
            print(self.board.display_board())
            self.board.cells[self.human.make_move(self.board)].set('X')
            self.winner = self.board.winner_is()
            if self.board.not_full():
                print(self.board.display_board())
                self.board.cells[self.computer.make_move(self.board)].set('O')
                self.winner = self.board.winner_is()
            if self.winner is not None:
                playing = False
            if self.board.not_full() is False:
                playing = False

        if self.winner is None:
            print(f"Game finished with a Tie.")
            print(self.board.display_board())
        else:
            print(f"Game finished,")
            print(self.board.display_board())
            print(f"and winner is: {self.winner}.")

