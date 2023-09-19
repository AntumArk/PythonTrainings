from grid import TicTacValues


def solve_ticTacToe(cells: list[TicTacValues], grid_size: int) -> TicTacValues:
    print("Solving")
    result = check_crosses(cells, grid_size)
    if result != TicTacValues.Z:
        return result

    result = check_rows(cells, grid_size)
    if result != TicTacValues.Z:
        return result

    result = check_columns(cells, grid_size)
    if result != TicTacValues.Z:
        return result

    if check_board_full(cells):
        print("TIE")
        return TicTacValues.Z
    print("Game is still going")
    return TicTacValues.Z


def check_rows(cells: list[TicTacValues], grid_size: int) -> TicTacValues:
    print("Checking Rows")
    for row in range(grid_size):
        cell_sum = sum(cells[row * grid_size : row * grid_size + grid_size])
        print("cell_sum ", cell_sum)
        result = check_win(cell_sum)
        if result != TicTacValues.Z:
            return result
    return TicTacValues.Z


def check_columns(cells: list[TicTacValues], grid_size: int) -> TicTacValues:
    print("Checking Columns")
    for column in range(grid_size):
        cell_sum = sum(cells[column::grid_size])
        print("cell_sum ", cell_sum)
        result = check_win(cell_sum)
        if result != TicTacValues.Z:
            return result
    return TicTacValues.Z


def check_crosses(cells: list[TicTacValues], grid_size: int) -> TicTacValues:
    print("Checking crosses")
    center_index = 4
    first_point = 0
    last_point = 8
    columns_to_solve = 4
    for _ in range(columns_to_solve):
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


def check_board_full(cells: list[TicTacValues]) -> bool:
    for _, cell in enumerate(cells):
        if cell.value == TicTacValues.Z:
            return False
    return True
