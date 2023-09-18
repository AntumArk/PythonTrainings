from grid import TicTacGrid, TicTacValues
from TicTacToeSolver import solve_ticTacToe

print("Hello world")


# draw_vertical_line(1)
# draw_horizontal_line(1)
# draw_vertical_line(2)
# draw_horizontal_line(2)
# draw_vertical_line(3)
# draw_horizontal_line(3)

gridUI = TicTacGrid(1, 1)
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
# fmt: on
gridUI.draw_grid(game_cells)
# print(x_character)
# print(o_character)
solve_ticTacToe(game_cells)
print()
gridUI.draw_grid(game_cells_X)
solve_ticTacToe(game_cells_X)
print()
gridUI.draw_grid(game_cells_O)
solve_ticTacToe(game_cells_O)
print()
