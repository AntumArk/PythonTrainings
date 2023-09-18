""" Module for drawing tic tac toe grid and cell values"""
from enum import IntEnum, Enum


class TicTacValues(IntEnum):
    """Enumerator for game logic"""

    Z = 0
    X = 1
    O = -1


class TicTacChars(Enum):
    """Enumerator for characters used in drawing TicTacToe"""

    Z = " "
    X = "❌"
    O = "⭕"
    H_LINE = "─"
    V_LINE = "│"
    H_CROSS = "┼"


class TicTacGrid:
    """Class for drawing TicTacToe"""

    grid_size: int = 3
    grid_width_scale: int = 5
    grid_scale_x: int = 1
    grid_scale_y: int = 1
    grid_height: int = 3
    x_whitespaces: int = 2  # 2 whitespaces long
    whitespaces_per_cell: int = 3

    def __init__(self, grid_scale_x=1, grid_scale_y=1) -> None:
        self.grid_scale_x = grid_scale_x
        self.grid_scale_y = grid_scale_y

    def draw_vertical_line(self, scale, cells):
        """Draws one grid row cells. Cells can be either blank, X or O"""
        # This is where empty lines should be drawn
        for index in range(self.grid_size):
            self.print_filled_cell(scale, cells[index])
            if index != self.grid_size - 1:
                self.print_no_endl(TicTacChars.V_LINE.value)
        print()

    def print_blank_cell(self, scale):
        """Prints one blank grid cell"""
        for _ in range(self.whitespaces_per_cell * scale):
            self.print_no_endl(TicTacChars.Z.value)

    def print_filled_cell(self, scale, value):
        """Prints filled cell"""
        if value == TicTacValues.Z:
            self.print_blank_cell(scale)
            return
        if value == TicTacValues.X:
            self.print_no_endl(TicTacChars.X.value)
        if value == TicTacValues.O:
            self.print_no_endl(TicTacChars.O.value)
        for _ in range(self.whitespaces_per_cell * scale - self.x_whitespaces):
            self.print_no_endl(TicTacChars.Z.value)

    def print_no_endl(self, text):
        """Prints something without line ending"""
        print(text, end="")

    def draw_horizontal_line(self, scale):
        """Prints one row which separates grid visually"""
        # This is where empty lines should be drawn
        for index in range(self.grid_size):
            for _ in range(self.whitespaces_per_cell * scale):
                self.print_no_endl(TicTacChars.H_LINE.value)
            if index != self.grid_size - 1:
                self.print_no_endl(TicTacChars.H_CROSS.value)
        print()

    def draw_grid(self, cells):
        """Draws all grid based on cell content"""
        print()
        for row in range(self.grid_size):
            self.draw_vertical_line(
                self.grid_scale_y,
                cells[0 + self.grid_size * row : self.grid_size + self.grid_size * row],
            )
            if row != self.grid_size - 1:
                self.draw_horizontal_line(self.grid_scale_x)
        print()
