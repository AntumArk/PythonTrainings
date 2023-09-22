# from TicTacToeSolver import get_rows
import numpy as np
from functools import reduce


# from grid import TicTacGrid
def flatten_reduce_lambda(matrix):
    flat_list = []
    for row in matrix:
        flat_list += row
    return flat_list


# arrange gives single dimentional list
# reshape, makes it two dimensional.
x = np.arange(25).reshape(5, 5)
row, col = np.indices((2, 3))
print(x[row, col])
print(x)
allgrid = []
# print([x[:5,i] for i in range(5)])
# print([x[i,:5] for i in range(5)])
# print([x[i,i] for i in range(5)])
# print([x[i,4-i] for i in range(5)])

grid_size = 5
columns = [x[:grid_size, i] for i in range(grid_size)]
rows = [x[i, :grid_size] for i in range(grid_size)]
main_diag = [x[i, i] for i in range(grid_size)]
sec_diag = [x[i, grid_size - 1 - i] for i in range(grid_size)]

columns_sum = [sum(columns[i]) for i in range(len(columns))]
rows_sum = [sum(rows[i]) for i in range(len(rows))]
main_sum = sum(main_diag)
sec_sum = sum(sec_diag)
allgrid = [main_sum, sec_sum]
allgrid.extend(columns_sum)
allgrid.extend(rows_sum)
# allgrid = [item for sublist in allgrid for item in sublist]
print(allgrid)
breakpoint()
# grid= TicTacGrid(1,1,4)
# get_rows(3)
# a=[i for i in range(1,4)]
# print(a)
# a= [a, [i for i in range(1,4)]]
# print(a)
