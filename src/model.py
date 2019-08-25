class Cell:

    def __init__(self, start_value):
        self.value = start_value

    def set(self, new_value):
        self.value = new_value

    @property
    def content(self):
        return self.value

    @property
    def is_X(self):
        return self.value == 'X'

    @property
    def is_O(self):
        return self.value == 'O'

    @property
    def is_available(self):
        return self.value not in ('X', 'O')

    def __repr__(self):
        return str(self.content)


class Board:

    def __init__(self):
        self.cells = []
        self.setup_board()

    def setup_board(self):
        for x in range(1,10):
            a_cell = Cell(str(x))
            self.cells.append(a_cell)

    def __repr__(self):
        return f"Board({len(self.cells)}"

    def __str__(self):
        return str(self.cells)

    def not_full(self):
        result = False
        for i in range(9):
            result = result or self.cells[i].is_available
        return result

    def winner_is(self):
        winner = None
        for temp_player in ('X', 'O'):
            if self.check_rows(temp_player):
                winner = temp_player
            elif self.check_columns(temp_player):
                winner = temp_player
            elif self.check_diagonals(temp_player):
                winner = temp_player
        return winner

    def check_rows(self, test_player):
        for x in (0, 3, 6):
            if test_player == self.cells[x].content \
                    and test_player == self.cells[x+1].content\
                    and test_player == self.cells[x+2].content:
                return True
        return False

    def check_columns(self, test_player):
        for x in (0, 1, 2):
            if test_player == self.cells[x].content \
                    and test_player == self.cells[x+3].content \
                    and test_player == self.cells[x+6].content:
                return True
        return False

    def check_diagonals(self, test_player):
            if test_player == self.cells[0].content \
                    and test_player == self.cells[4].content \
                    and test_player == self.cells[8].content:
                return True
            elif test_player == self.cells[2].content \
                    and test_player == self.cells[4].content \
                    and test_player == self.cells[6].content:
                return True
            else:
                return False

    def display_board(self):
        build = 'Current Board:\n'
        line = f"-----------\n"
        for x in (0, 3, 6):
            temp = f" {self.cells[x].content} |" \
            f" {self.cells[x+1].content} |" \
            f" {self.cells[x+2].content} \n"
            build = build + temp
            if x in (0, 3): build = build + line
        return build


class Player:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Player: {self.name}"


class HumanPlayer(Player):

    def __init__(self):
        Player.__init__(self, 'temp')
        self.ask_for_name()

    def ask_for_name(self):
        self.name = input('Please enter your name: ')

    def make_move(self, the_board: Board):
        valid = False
        while not valid:
            move_location = int(input('Please enter the location number for your move: '))
            move_location -= 1
            if the_board.cells[move_location].is_available:
                return move_location
            else:
                print('Sorry that position is already taken, please choose from available #.')


class ComputerPlayer(Player):

    def __init__(self):
        Player.__init__(self, 'Hal')

    def make_move(self, the_board):
        for i in range(9):
            if the_board.cells[i].is_available: return i

