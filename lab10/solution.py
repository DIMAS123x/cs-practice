import numpy as np


def make_table(rows, columns):
    return np.arange(rows * columns).reshape(rows, columns).tolist()


def rectangle(matrix, row_start, row_stop, column_start, column_stop):
    array = np.array(matrix)
    return array[row_start:row_stop, column_start:column_stop].tolist()



def replace_rectangle(matrix, row_start, row_stop, column_start, column_stop, value):
    array = np.array(matrix)
    changed = array.astype(np.result_type(array, value), copy=True)
    changed[row_start:row_stop, column_start:column_stop] = value
    return changed.tolist()


def matrix_vector_product(matrix, vector):
    return (np.array(matrix) @ np.array(vector)).tolist()


def matrix_multiply(left, right):
    return (np.array(left) @ np.array(right)).tolist()


def transpose_matrix(matrix):
    return np.array(matrix).T.tolist()


def solve_system(matrix, vector):
    solution = np.linalg.solve(np.array(matrix), np.array(vector))
    return np.round(solution, 6).tolist()


def tensor_channel_mean(tensor):
    return np.array(tensor).mean(axis=-1).tolist()


def point_distance(first, second):
    difference = np.array(first) - np.array(second)
    return round(float(np.linalg.norm(difference)), 6)