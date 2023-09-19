from TicTacConstants import TicTacValues
from grid import TicTacGrid
from Controller import GameController

print("Hello world")


# gridUI = [TicTacGrid(1, 1),TicTacGrid(1, 1),TicTacGrid(1, 1)]
gridUI = TicTacGrid(1, 1, 3)
print(gridUI)
game_grid_size = 3

gridUI.set_cell_value(TicTacValues.X, 5)

print(gridUI)
controller = GameController()
# fmt: off

a = [
    1,    0,    0,
    0,    2,    0,
    0,    0,    3,
]
print(a[0::(3*2-2)])

a = [
    1,    0,    0, 0,
    0,    2,    0, 0,
    0,    0,    3, 0,
    0,    0,    0, 4
]
print([a[(i-1)*i] for i in range(4)])

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
    TicTacValues.O,    TicTacValues.Z,    TicTacValues.O,
    TicTacValues.Z,    TicTacValues.Z,    TicTacValues.O,
]
# Tie  cells
game_cells_tie = [
    TicTacValues.X,    TicTacValues.O,    TicTacValues.O,
    TicTacValues.O,    TicTacValues.O,    TicTacValues.X,
    TicTacValues.X,    TicTacValues.X,    TicTacValues.O,
]
# print(game_cells[0:3])
# print(game_cells[0:3])
# print(game_cells_O[0::4])
# print(game_cells_O[1::3])
# print(game_cells_O[2::3])
# print()
# print(game_cells_O[1::game_grid_size])
# print()
# print(game_cells_O[2::game_grid_size])
# print()
# fmt: on
# gridUI.draw_grid(game_cells)
# # print(x_character)
# # print(o_character)
# print(solve_ticTacToe(game_cells))
# print()

# gridUI.draw_grid(game_cells_X)
# print(solve_ticTacToe(game_cells_X))
# print()

# gridUI.draw_grid(game_cells_X)
# print(solve_ticTacToe(game_cells_X, game_grid_size))
# print()


# gridUI.draw_grid(game_cells_tie)
# print(solve_ticTacToe(game_cells_tie))
# print()
# print(gridUI.get_draw_grid(game_cells_tie))
# for ui in gridUI:
#     # ui.draw_grid(game_cells_tie)
#     print()
#     print(ui.get_draw_grid(game_cells_tie))
#     print()
controller.run()
