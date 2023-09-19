from grid import TicTacGrid
from TicTacConstants import TicTacValues
from TicTacToeSolver import solve_ticTacToe


class UltimateGrid:
    def __init__(
        self, grid_draw_scale_x: int = 1, grid_draw_scale_y: int = 1, grid_size: int = 3
    ) -> None:
        grid_cells = grid_size**2
        self.grid_draw_scale_x = grid_draw_scale_x
        self.grid_draw_scale_y = grid_draw_scale_y
        self.grid_size = grid_size
        self.grids = [
            TicTacGrid(grid_draw_scale_x, grid_draw_scale_y, grid_size)
        ] * grid_cells
        self.cells = [TicTacValues.Z] * (grid_cells)

    def __str__(self) -> str:
        return "pass"

    def is_cell_free(self, active_board: int, cell: int) -> bool:
        return self.grids[active_board].cells[cell] == TicTacValues.Z

    def set_cell_value(
        self, active_board: int, cell: int, current_player: TicTacValues
    ):
        self.grids[active_board].cells[cell] = current_player

    def get_game_result(self) -> TicTacValues:
        return solve_ticTacToe(self.cells, self.grid_size)

    def is_finished(self) -> bool:
        i = 0
        for grid in self.grids:
            self.cells[i] = grid.get_game_result()
            i += 1
        return self.get_game_result() != TicTacValues.Z

    def is_sub_grid_finished(self, active_board: int) -> bool:
        return self.grids[active_board].is_finished()
