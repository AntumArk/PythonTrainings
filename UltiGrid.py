from grid import TicTacGrid
from TicTacConstants import TicTacValues, TicTacGameResults
from TicTacToeSolver import solve_ticTacToe


class UltimateGrid:
    def __init__(
        self, grid_draw_scale_x: int = 1, grid_draw_scale_y: int = 1, grid_size: int = 3
    ) -> None:
        self.grid_draw_scale_x = grid_draw_scale_x
        self.grid_draw_scale_y = grid_draw_scale_y
        self.grid_size = grid_size
        self.grids = [
            TicTacGrid(grid_draw_scale_x, grid_draw_scale_y, grid_size)
        ] * grid_size**2

    def __str__(self) -> str:
        rows = [""]
        index = 0
        separator = ""
        grids_strings = [str(grid).splitlines() for grid in self.grids]
        for uiline in self.grid_size + 2:
            first_row = [bleh[uiline] for bleh in grids_strings[0 : len(grids_strings)]]
            rows.append(separator.join(first_row[0]))
        print(grids_strings)

        return ""

    def __getitem__(self, cell):
        return self.grids[cell]

    def set_cell_value(
        self, active_board: int, cell: int, current_player: TicTacValues
    ):
        self.grids[active_board][cell] = current_player

    def get_game_result(self) -> TicTacGameResults:
        return solve_ticTacToe(self.cells, self.grid_size)

    def is_finished(self) -> bool:
        i = 0
        for grid in self.grids:
            self.cells[i] = grid.get_game_result()
            i += 1
        # results=map(lambda result:result.get_game_result(),self.grids)
        return self.get_game_result() != TicTacGameResults.IN_PROGRESS
