from TicTacConstants import TicTacValues, TicTacGameResults
import numpy as np


def solve_ticTacToe(cells: ndarray) -> TicTacGameResults:
    shape = cells.shape
    grid_size = shape[0]

    columns = [cells[:grid_size, column] for column in range(grid_size)]
    rows = [cells[row, :grid_size] for row in range(grid_size)]
    main_diag = [cells[i, i] for i in range(grid_size)]
    sec_diag = [cells[i, grid_size - 1 - i] for i in range(grid_size)]

    columns_sum = [sum(columns[i]) for i in range(len(columns))]
    rows_sum = [sum(rows[i]) for i in range(len(rows))]
    main_sum = sum(main_diag)
    sec_sum = sum(sec_diag)
    results = [main_sum, sec_sum]
    results.extend(columns_sum)
    results.extend(rows_sum)
    # results = [item for sublist in results for item in sublist]
    print(results)

    print("Solving")
    result = check_win(results)
    if result != TicTacGameResults.IN_PROGRESS:
        return result

    if check_board_full(cells):
        print("TIE")
        return TicTacGameResults.TIE

    print("Game is still going")
    return TicTacGameResults.IN_PROGRESS


def check_win(cell_sum: list[int]) -> TicTacGameResults:
    if 3 * TicTacValues.X.value in cell_sum:
        print("X WON!")
        return TicTacGameResults.X_WON
    if 3 * TicTacValues.O.value in cell_sum:
        print("O WON!")
        return TicTacGameResults.O_WON
    return TicTacGameResults.IN_PROGRESS


def check_board_full(cells: list[TicTacValues]) -> bool:
    for _, cell in enumerate(cells):
        if cell.value == TicTacValues.Z:
            return False
    return True
