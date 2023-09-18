from grid import TicTacGrid, TicTacValues

print("Hello world")


# draw_vertical_line(1)
# draw_horizontal_line(1)
# draw_vertical_line(2)
# draw_horizontal_line(2)
# draw_vertical_line(3)
# draw_horizontal_line(3)

gridUI = TicTacGrid(1, 1)

game_cells = [
    TicTacValues.X,
    TicTacValues.Z,
    TicTacValues.O,
    TicTacValues.X,
    TicTacValues.O,
    TicTacValues.X,
    TicTacValues.Z,
    TicTacValues.Z,
    TicTacValues.Z,
]

gridUI.draw_grid(game_cells)
# print(x_character)
# print(o_character)
