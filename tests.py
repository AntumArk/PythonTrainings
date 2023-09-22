# from TicTacToeSolver import get_rows
# import numpy as np
from functools import reduce


from grid import TicTacGrid


def flatten_reduce_lambda(matrix):
    flat_list = []
    for row in matrix:
        flat_list += row
    return flat_list


# arrange gives single dimentional list
# reshape, makes it two dimensional.

grid_size = 5
x = [[5] * grid_size] * grid_size
print(x)
allgrid = []
# print([x[:5,i] for i in range(5)])
# print([x[i,:5] for i in range(5)])
# print([x[i,i] for i in range(5)])
# print([x[i,4-i] for i in range(5)])
columns = []
rows = []
main_diag = []
sec_diag = []
results = []
for i in range(grid_size):
    columns = x[:grid_size][i]  # columns
    rows = x[i][:grid_size]  # rows
    results.append(sum(columns))
    results.append(sum(rows))
    main_diag.append(x[i][i])
    sec_diag.append(x[i][grid_size - 1 - i])
    # breakpoint()

results.append(sum(main_diag))
results.append(sum(sec_diag))
# allgrid = [item for sublist in allgrid for item in sublist]
print(results)
breakpoint()
grid = TicTacGrid(1, 1, 4)
# get_rows(3)
# a=[i for i in range(1,4)]
# print(a)
# a= [a, [i for i in range(1,4)]]
# print(a)
