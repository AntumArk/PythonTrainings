from TicTacConstants import TicTacValues, TicTacGameResults


def solve_ticTacToe(cells) -> TicTacGameResults:
    shape = cells.shape
    grid_size = shape[0]
    columns = []
    rows = []
    main_diag = []
    sec_diag = []
    results = []
    for i in range(grid_size):
        columns = cells[:grid_size][i]  # columns
        rows = cells[i][:grid_size]  # rows
        results.append(sum(columns))
        results.append(sum(rows))
        main_diag.append(cells[i][i])
        sec_diag.append(cells[i][grid_size - 1 - i])
    
    results.append(sum(main_diag))
    results.append(sum(sec_diag))
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


def check_board_full(cells) -> bool:
    return TicTacValues.Z not in cells
