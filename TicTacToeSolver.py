from TicTacConstants import TicTacValues


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
        return TicTacValues.TIE
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
    if grid_size % 2 == 0:
        print("Not solving crosses for even grid")
        return TicTacValues.Z

    # Primary principal
    print("Checking crosses")
    cell_sum = sum(cells[0 :: (grid_size - 1) + 2])
    print("cell_sum ", cell_sum)
    result = check_win(cell_sum)
    if result != TicTacValues.Z:
        return result

    # Secondary principal
    cell_sum = sum(cells[grid_size - 1 :: grid_size])
    print("cell_sum ", cell_sum)
    result = check_win(cell_sum)
    if result != TicTacValues.Z:
        return result

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
