import numpy as np


def make_table(rows, columns):
    return np.arange(rows * columns).reshape(rows, columns).tolist()


def rectangle(matrix, row_start, row_stop, column_start, column_stop):
    array = np.array(matrix)
    return array[row_start:row_stop, column_start:column_stop].tolist()