from grid import TicTacGrid, TicTacValues

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
        self.UI.draw_grid(self.game_cells)
        
        

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

