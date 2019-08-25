class Cell:

    def __init__(self):
        self.value = ''

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
        return self.content


class Board:

    def __init__(self):
        self.cells = []
        self.setup_board()

    def setup_board(self):
        for x in range(1,10):
            self.cells.append(str(x))

    def __str__(self):
        return str(self.cells)

