from grid import TicTacValues
from typing import List


def solve_ticTacToe(cells) -> TicTacValues:
    print("Solving")
    result = check_crosses(cells)
    if result != TicTacValues.Z:
        return result

    result = check_rows(cells)
    if result != TicTacValues.Z:
        return result

    result = check_columns(cells)
    if result != TicTacValues.Z:
        return result

    if check_board_full(cells):
        print("TIE")
        return TicTacValues.Z
    print("Game is still going")
    return TicTacValues.Z


def check_rows(cells) -> TicTacValues:
    print("Checking Rows")
    grid_size = 3
    first_index = 0
    for _ in range(grid_size):
        cell_sum = cells[first_index] + cells[first_index + 1] + cells[first_index + 2]
        print("cell_sum ", cell_sum)
        result = check_win(cell_sum)
        if result != TicTacValues.Z:
            return result
        first_index += grid_size
    return TicTacValues.Z


def check_columns(cells) -> TicTacValues:
    print("Checking Columns")
    grid_size = 3
    for cycle in range(grid_size):
        cell_sum = (
            cells[cycle] + cells[cycle + grid_size] + cells[cycle + 2 * grid_size]
        )
        print("cell_sum ", cell_sum)
        result = check_win(cell_sum)
        if result != TicTacValues.Z:
            return result
    return TicTacValues.Z


# end def


def check_crosses(cells) -> TicTacValues:
    print("Checking crosses")
    center_index = 4
    first_point = 0
    last_point = 8
    cycles_to_solve = 4
    for _ in range(cycles_to_solve):
        cell_sum = cells[first_point] + cells[center_index] + cells[last_point]
        print("cell_sum ", cell_sum)
        result = check_win(cell_sum)
        if result != TicTacValues.Z:
            return result
        # Rotate beam
        first_point += 1
        last_point -= 1
    return TicTacValues.Z


def check_win(cell_sum: int) -> TicTacValues:
    if cell_sum == 3 * TicTacValues.X.value:
        print("X WON!")
        return TicTacValues.X
    if cell_sum == 3 * TicTacValues.O.value:
        print("O WON!")
        return TicTacValues.O
    return TicTacValues.Z


def check_board_full(cells: List[TicTacValues]) -> bool:
    for _, cell in enumerate(cells):
        if cell.value == TicTacValues.Z:
            return False
    return True
