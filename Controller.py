from TicTacConstants import TicTacValues
from grid import TicTacGrid
from TicTacToeSolver import solve_ticTacToe, check_board_full
from UltiGrid import UltimateGrid


class GameController:
    current_player = TicTacValues.Z
    INVALID_INPUT: int = -1

    def __init__(self, grid_size: int = 3) -> None:
        self.grid_size = grid_size
        self.ultimate_grid = UltimateGrid(1, 1, grid_size)
        self.active_board = -1

    def run(self):
        self.current_player = self.get_player_from_input()
        if self.current_player == TicTacValues.Z:
            print("Invalid player cant play.")
            return
        self.pick_board()

        self.play()

    def pick_board(self) -> bool:
        print("Select which board to play [1-9]. Current player:", self.current_player)
        self.active_board = self.parse_input(input())
        if self.active_board == self.INVALID_INPUT:
            print("Board input invalid, please restart")
            return False
        return True

    def play(self):
        print(str(self.ultimate_grid))
        while not self.ultimate_grid.is_finished():
            print(str(self.ultimate_grid))
            print(
                "Select which cell to enter[1-9].\n Current player:",
                self.current_player,
                "\n current board:",
                self.active_board + 1,
            )
            cell = self.parse_input(input())
            if cell != self.INVALID_INPUT:
                if self.is_cell_free(cell):
                    self.ultimate_grid[self.active_board][cell] = self.current_player
                    self.switch_player()
                    self.set_active_board(cell)
                else:
                    print("Cell is not empty")
            else:
                print("Failed to parse input")

        print("GAME OVER")

    def set_active_board(self, cell):
        self.active_board = cell
        if self.ultimate_grid[self.active_board].is_finished():
            print("Board is already finished, please pick another one")
            while self.pick_board():
                print("Picking board")

    def parse_input(self, text) -> int:
        try:
            cell = int(text)
            if cell > self.grid_size**2 or cell < 1:
                raise ValueError("Input out of [1-9] range")
            cell -= 1  # move to zero based system
            return cell

        except ValueError:
            print("Invalid input")
            return self.INVALID_INPUT

    def switch_player(self):
        if self.current_player == TicTacValues.X:
            self.current_player = TicTacValues.O
        else:
            self.current_player = TicTacValues.X

    def is_cell_free(self, cell: int) -> bool:
        return self.ultimate_grid[self.active_board][cell] == TicTacValues.Z

    def get_player_from_input(self):
        print('Select which player starts. Enter "X" or "O"')
        line = input()
        if len(line) > 1:
            print("invalid input")
            return TicTacValues.Z
        if line == "X":
            return TicTacValues.X
        if line == "O":
            return TicTacValues.O
        return TicTacValues.Z
