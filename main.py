from grid import TicTacGrid, TicTacValues
from Controller import GameController

print("Hello world")


gridUI = [TicTacGrid(1, 1),TicTacGrid(1, 1),TicTacGrid(1, 1)]



controller = GameController()
# fmt: off
game_cells = [
    TicTacValues.Z,    TicTacValues.Z,    TicTacValues.O,
    TicTacValues.Z,    TicTacValues.Z,    TicTacValues.X,
    TicTacValues.Z,    TicTacValues.Z,    TicTacValues.O,
]
# Win X cells
game_cells_X = [
    TicTacValues.X,    TicTacValues.Z,    TicTacValues.X,
    TicTacValues.O,    TicTacValues.X,    TicTacValues.X,
    TicTacValues.X,    TicTacValues.Z,    TicTacValues.Z,
]
# Win O cells
game_cells_O = [
    TicTacValues.X,    TicTacValues.Z,    TicTacValues.O,
    TicTacValues.O,    TicTacValues.O,    TicTacValues.O,
    TicTacValues.Z,    TicTacValues.Z,    TicTacValues.Z,
]
# Tie  cells
game_cells_tie = [
    TicTacValues.X,    TicTacValues.O,    TicTacValues.O,
    TicTacValues.O,    TicTacValues.O,    TicTacValues.X,
    TicTacValues.X,    TicTacValues.X,    TicTacValues.O,
]
# fmt: on
# gridUI.draw_grid(game_cells)
# # print(x_character)
# # print(o_character)
# print(solve_ticTacToe(game_cells))
# print()

# gridUI.draw_grid(game_cells_X)
# print(solve_ticTacToe(game_cells_X))
# print()

# gridUI.draw_grid(game_cells_O)
# print(solve_ticTacToe(game_cells_O))
# print()


# gridUI.draw_grid(game_cells_tie)
# print(solve_ticTacToe(game_cells_tie))
# print()

for ui in gridUI:
    # ui.draw_grid(game_cells_tie)
    ui.print_no_endl(ui.get_vertical_line(1, game_cells_tie))
    ui.print_no_endl("┃")

# controller.run()
