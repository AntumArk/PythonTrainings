from TicTacConstants import TicTacValues
from grid import TicTacGrid
from TicTacToeSolver import solve_ticTacToe, check_board_full


class GameController:
    game_cells = [
        TicTacValues.Z,
        TicTacValues.Z,
        TicTacValues.Z,
        TicTacValues.Z,
        TicTacValues.Z,
        TicTacValues.Z,
        TicTacValues.Z,
        TicTacValues.Z,
        TicTacValues.Z,
    ]
    UI: TicTacGrid = TicTacGrid(1, 1)

    current_player = TicTacValues.Z

    def __init__(self) -> None:
        pass

    def run(self):
        self.current_player = self.get_player_from_input()
        if self.current_player == TicTacValues.Z:
            print("Invalid player cant play.")
            return
        self.play()

    def play(self):
        self.UI.draw_grid(self.game_cells)
        while (
            not check_board_full(self.game_cells)
            and solve_ticTacToe(self.game_cells) == TicTacValues.Z
        ):
            self.UI.draw_grid(self.game_cells)
            print(
                "Select which cell to enter[1-9]. Current player:", self.current_player
            )
            if self.parse_input(input()):
                self.switch_player()
            else:
                print("Failed to parse input")
        print("GAME OVER")

    def parse_input(self, text) -> bool:
        try:
            cell = int(text)
            if cell > 9 or cell < 1:
                raise ValueError("Input out of [1-9] range")
            cell -= 1  # move to zero based system
            self.check_if_occupied(cell)
            self.game_cells[cell] = self.current_player
            return True
        except ValueError:
            return False

    def check_if_occupied(self, cell):
        if self.game_cells[cell] != TicTacValues.Z:
            raise ValueError("Cell is already occupied")

    def switch_player(self):
        if self.current_player == TicTacValues.X:
            self.current_player = TicTacValues.O
        else:
            self.current_player = TicTacValues.X

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
