from grid import TicTacValues
from typing import List


def solve_ticTacToe(cells) -> TicTacValues:
    print("Solving")
    check_crosses(cells)
    check_rows(cells)
    check_columns(cells)
    if check_board_full(cells):
        print("tie")
        return TicTacValues.Z
    print("Game is still going")


def check_rows(cells):
    print("Checking Rows")
    grid_size = 3
    first_index = 0
    for cycle in range(grid_size):
        sum = cells[first_index] + cells[first_index + 1] + cells[first_index + 2]
        print("Sum ", sum)
        if check_win(sum):
            return
        first_index += grid_size


def check_columns(cells):
    print("Checking Columns")
    grid_size = 3
    for cycle in range(grid_size):
        sum = cells[cycle] + cells[cycle + grid_size] + cells[cycle + 2 * grid_size]
        print("Sum ", sum)
        if check_win(sum):
            return


# end def


def check_crosses(cells):
    print("Checking crosses")
    center_index = 4
    first_point = 0
    last_point = 8
    cycles_to_solve = 4
    for cycle in range(cycles_to_solve):
        # print("cycle ", cycle)
        sum = cells[first_point] + cells[center_index] + cells[last_point]
        print("Sum ", sum)
        if check_win(sum):
            return
        # Rotate beam
        first_point += 1
        last_point -= 1


def check_win(sum: int) -> bool:
    if sum == 3:
        print("X WON!")
        return True
    if sum == -3:
        print("O WON!")
        return True
    return False


def check_board_full(cells: List[TicTacValues]) -> bool:
    for _, cell in enumerate(cells):
        if cell.value == TicTacValues.Z:
            return False
    return True
