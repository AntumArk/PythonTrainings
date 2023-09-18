def solve_ticTacToe(cells):
    print("Solving")
    center_index = 4
    first_point = 0
    last_point = 8
    cycles_to_solve = 4
    for cycle in range(cycles_to_solve):
        print("cycle ", cycle)
        sum = cells[first_point] + cells[center_index] + cells[last_point]
        print("Sum ", sum)
        if sum == 3:
            print("X WON!")
            return
        if sum == -3:
            print("O WON!")
            return
        # Rotate beam
        first_point += 1
        last_point -= 1
    print("tie")
