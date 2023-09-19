""" Module for drawing tic tac toe grid and cell values"""

from TicTacToeSolver import solve_ticTacToe
from TicTacConstants import TicTacValues, TicTacChars


def print_no_endl(text):
    """Prints something without line ending"""
    print(text, end="")


class TicTacGrid:
    """Class for drawing TicTacToe"""

    whitespaces_per_filled_cell: int = 2  # 2 whitespaces long
    whitespaces_per_cell: int = 3

    def __init__(
        self, grid_draw_scale_x: int = 1, grid_draw_scale_y: int = 1, grid_size: int = 3
    ) -> None:
        self.grid_draw_scale_x = grid_draw_scale_x
        self.grid_draw_scale_y = grid_draw_scale_y
        self.grid_size = grid_size
        self.cells = [TicTacValues.Z] * (grid_size**2)

    def __str__(self) -> str:
        return self.get_grid(self.cells)

    def _get_vertical_line(self, scale, cells) -> str:
        """Draws one grid row cells. Cells can be either blank, X or O"""
        output_str = ""
        for index in range(self.grid_size):
            output_str += self._get_filled_cell(scale, cells[index])
            if index != self.grid_size - 1:
                output_str += TicTacChars.V_LINE.value
        return output_str

    def _get_blank_cell(self, scale) -> str:
        """Prints one blank grid cell"""
        output_str = ""
        for _ in range(self.whitespaces_per_cell * scale):
            output_str += TicTacChars.Z.value
        return output_str

    def _get_filled_cell(self, scale, value) -> str:
        """Prints filled cell"""
        output_str = ""
        if value == TicTacValues.Z:
            output_str += self._get_blank_cell(scale)
            return output_str
        if value == TicTacValues.X:
            output_str += TicTacChars.X.value
        if value == TicTacValues.O:
            output_str += TicTacChars.O.value
        for _ in range(
            self.whitespaces_per_cell * scale - self.whitespaces_per_filled_cell
        ):
            output_str += TicTacChars.Z.value
        return output_str

    def _get_horizontal_line(self, scale) -> str:
        """Prints one row which separates grid visually"""
        # This is where empty lines should be drawn
        output_str = "\n"
        for index in range(self.grid_size):
            for _ in range(self.whitespaces_per_cell * scale):
                output_str += TicTacChars.H_LINE.value
            if index != self.grid_size - 1:
                output_str += TicTacChars.H_CROSS.value
        output_str += "\n"
        return output_str

    def get_grid(self, cells) -> str:
        """Draws all grid based on cell content"""
        output_str = ""
        for row in range(self.grid_size):
            output_str += self._get_vertical_line(
                self.grid_draw_scale_y,
                cells[0 + self.grid_size * row : self.grid_size + self.grid_size * row],
            )
            if row != self.grid_size - 1:
                output_str += self._get_horizontal_line(self.grid_draw_scale_x)
        return output_str

    def get_game_result(self) -> TicTacValues:
        solve_ticTacToe(self.cells, self.grid_size)

    def is_finished(self) -> bool:
        return self.get_game_result() != TicTacValues.Z

    def set_cell_value(self, current_player: TicTacValues, cell_index: int):
        if cell_index > self.grid_size**2:
            raise ValueError("Trying to set value out of bounds")
        self.cells[cell_index] = current_player
