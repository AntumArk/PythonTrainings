from grid import TicTacGrid, TicTacValues
from TicTacToeSolver import solve_ticTacToe, check_board_full
class GameController:
    game_cells = [
    TicTacValues.Z,    TicTacValues.Z,    TicTacValues.Z,
    TicTacValues.Z,    TicTacValues.Z,    TicTacValues.Z,
    TicTacValues.Z,    TicTacValues.Z,    TicTacValues.Z,
    ]
    UI : TicTacGrid=TicTacGrid( 1, 1 )
    
    current_player = TicTacValues.Z

    def __init__(self) -> None:
        pass

    def run(self):
        self.current_player=self.get_player_from_input()
        if self.current_player == TicTacValues.Z:
            print("Invalid player cant play.")
            return
        self.play()
        
        
    def play(self):
        self.UI.draw_grid(self.game_cells)
        while(not check_board_full(self.game_cells) and solve_ticTacToe(self.game_cells)==TicTacValues.Z):
            self.UI.draw_grid(self.game_cells)
            print("Select which cell to enter[1-9]. Current player:", self.current_player)
            line = input()
            self.switch_player()
        print("GAME OVER")

    def switch_player(self):
        if self.current_player==TicTacValues.X:
            self.current_player=TicTacValues.O
        else:
            self.current_player=TicTacValues.X

    def get_player_from_input(self):
        print("Select which player starts. Enter \"X\" or \"Y\"")
        line=input()
        if len(line) > 1:
            print("invalid input")
            return TicTacValues.Z
        if line == "X":
            return TicTacValues.X
        if line == "O":
            return TicTacValues.O
        return TicTacValues.Z

