from random import randint
from cell import Cell


class Model:
    """Class who implements the logic of game"""

    def __init__(self):
        self.flag_win = None
        self.flagged_cells = -1
        self.seconds_from_start = 1
        self.controller = None
        self.FIELD_WIDTH = None
        self.MINES_MAX = None
        self.FIELD_HEIGHT = None
        self.checked = None
        self.field = None
        self.stop_game = None
        self.is_game_over = None
        self.must_open_cells = None
        self.open_cells = None
        self.first_click = None
        self.playersEasy = []
        self.playersMid = []
        self.playersHard = []
        self.playersRandom = []

    """Getter and setter"""

    def set_controller(self, controller):
        self.controller = controller

    def get_FIELD_WIDTH(self):
        return self.FIELD_WIDTH

    def get_FIELD_HEIGHT(self):
        return self.FIELD_HEIGHT

    def get_MINES_MAX(self):
        return self.MINES_MAX

    def get_field(self):
        return self.field

    def get_cell(self, x, y):
        return self.field[y][x]

    def get_seconds_from_start(self):
        return self.seconds_from_start

    """Starts the game at a certain difficulty level."""

    def new_game(self, game_level=0):
        """Store the callback functions in list"""
        self.flag_win = 0
        levels = [
            self.empty_func,
            self.new_game_easy,
            self.new_game_mid,
            self.new_game_hard,
            self.new_game_random
        ]
        levels[game_level]()
        self.controller.set_start_button()
        self.controller.stop_timer()
        self.controller.clear_timer()
        self.controller.set_start_button()
        if self.flagged_cells != -1:
            self.controller.set_mines_board(self.MINES_MAX)
        self.create_field()

    def empty_func(self):
        """When player did not change game level and play last one."""
        pass

    def new_game_easy(self):
        self.FIELD_WIDTH = 9
        self.FIELD_HEIGHT = 9
        self.MINES_MAX = 10

    def new_game_mid(self):
        self.FIELD_WIDTH = 16
        self.FIELD_HEIGHT = 16
        self.MINES_MAX = 40

    def new_game_hard(self):
        self.FIELD_WIDTH = 30
        self.FIELD_HEIGHT = 16
        self.MINES_MAX = 99

    def new_game_random(self):
        self.FIELD_WIDTH = self.controller.get_int_input("Random Field", "Insert width:")
        self.FIELD_HEIGHT = self.controller.get_int_input("Random Field", "Insert height:")
        self.MINES_MAX = self.controller.get_int_input("Random Field", "Insert mines:")

    def create_field(self):
        # Creating field.
        self.first_click = True
        self.seconds_from_start = 1
        self.flagged_cells = 0
        self.open_cells = 0
        self.must_open_cells = (self.FIELD_WIDTH * self.FIELD_HEIGHT
                                - self.MINES_MAX)
        self.is_game_over = False
        self.stop_game = False
        self.field = []
        for y in range(self.FIELD_HEIGHT):
            _xrow = []
            for x in range(self.FIELD_WIDTH):
                cell = Cell(x, y)
                _xrow.append(cell)
            self.field.append(_xrow)

        # Setting mines at field.
        mines_ammout = 0
        while mines_ammout < self.MINES_MAX:
            _x = randint(0, self.FIELD_WIDTH - 1)
            _y = randint(0, self.FIELD_HEIGHT - 1)
            if not self.field[_y][_x].mined:
                mines_ammout += 1
                self.field[_y][_x].mined = True

    def open_cell(self, x, y):
        if not self.stop_game:
            if self.first_click:
                self.controller.create_timer()
                self.first_click = False
            cell = self.get_cell(x, y)
            # Check if the cell is not mined.
            last_state = cell.state
            cell.open()
            if cell.state == "opened" and last_state != cell.state:
                self.open_cells += 1
                self.checked = []
                if not cell.mined:
                    mines_number = self.check_neighbors(cell)
                    cell.int_state = mines_number
            if cell.state == "opened":
                if cell.mined:
                    # If this cell was mined game over.
                    cell.state = "opened"
                    self.is_game_over = True
                    self.stop_game = True
                else:
                    pass

            if self.is_game_over:
                self.game_over()

    def check_neighbors(self, cell):
        neighbors_mines = 0
        self.checked.append(cell)
        if self.is_mined(cell, cell.x - 1, cell.y - 1): neighbors_mines += 1
        if self.is_mined(cell, cell.x, cell.y - 1): neighbors_mines += 1
        if self.is_mined(cell, cell.x + 1, cell.y - 1): neighbors_mines += 1
        if self.is_mined(cell, cell.x - 1, cell.y): neighbors_mines += 1
        if self.is_mined(cell, cell.x + 1, cell.y): neighbors_mines += 1
        if self.is_mined(cell, cell.x - 1, cell.y + 1): neighbors_mines += 1
        if self.is_mined(cell, cell.x, cell.y + 1): neighbors_mines += 1
        if self.is_mined(cell, cell.x + 1, cell.y + 1): neighbors_mines += 1
        if neighbors_mines == 0:
            self.open_neighbors(cell)
            pass
        return neighbors_mines

    def open_neighbors(self, cell):
        self.open_one_neighbor(cell, cell.x - 1, cell.y - 1)
        self.open_one_neighbor(cell, cell.x, cell.y - 1)
        self.open_one_neighbor(cell, cell.x + 1, cell.y - 1)
        self.open_one_neighbor(cell, cell.x - 1, cell.y)
        self.open_one_neighbor(cell, cell.x + 1, cell.y)
        self.open_one_neighbor(cell, cell.x - 1, cell.y + 1)
        self.open_one_neighbor(cell, cell.x, cell.y + 1)
        self.open_one_neighbor(cell, cell.x + 1, cell.y + 1)

    def open_one_neighbor(self, old_cell, x, y):
        try:
            if old_cell.x == 0 and x == -1:
                return False
            if old_cell.x == self.FIELD_WIDTH - 1 and x == 1:
                return False
            if old_cell.y == 0 and y == -1:
                return False
            if old_cell.y == self.FIELD_HEIGHT - 1 and y == 1:
                return False
            cell = self.get_cell(x, y)
            if cell.state != "opened":
                cell.open()
                self.open_cells += 1
                if cell not in self.checked:
                    cell.int_state = self.check_neighbors(cell)
        except:
            pass

    def is_mined(self, old_cell, x, y):
        try:
            if old_cell.x == 0 and x == -1:
                return False
            if old_cell.x == self.FIELD_WIDTH - 1 and x == 1:
                return False
            if old_cell.y == 0 and y == -1:
                return False
            if old_cell.y == self.FIELD_HEIGHT - 1 and y == 1:
                return False
            return self.get_cell(x, y).mined
        except:
            return False

    def game_status(self):
        if self.is_game_over:
            self.controller.stop_timer()
            return "Lose"
        if self.must_open_cells <= self.open_cells:
            self.stop_game = True
            self.controller.set_win_button()
            if self.flag_win == 0:
                self.flag_win = 1
                self.controller.stop_timer()
                self.store_played_games()
            return "Win"
        return "Game"

    def game_over(self):
        for row in self.field:
            for cell in row:
                if cell.mined and cell.state != "flagged":
                    if cell.state == "opened":
                        cell.int_state = 13
                    else:
                        cell.int_state = 12
                elif not cell.mined and cell.state == "flagged":
                    cell.int_state = 14

    def next_mark(self, x, y):
        if not self.stop_game:
            cell = self.get_cell(x, y)
            old_state = cell.state
            cell.next_mark()
            if cell.state == "flagged":
                self.flagged_cells += 1
            else:
                if old_state == "flagged":
                    self.flagged_cells -= 1

    def store_played_games(self):
        if self.MINES_MAX == 3:
            self.playersEasy.append(self.controller.get_text_input("Noobie mode", "Insert your name"))
        elif self.MINES_MAX == 40:
            self.playersMid.append(self.controller.get_text_input("Average mode", "Insert your name"))
        elif self.MINES_MAX == 99:
            self.playersHard.append(self.controller.get_text_input("Respect mode", "Insert your name"))
        else:
            self.playersRandom.append(self.controller.get_text_input("Crazy mode", "Insert your name"))
