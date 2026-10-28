import numpy as np


def reshape_rows(values: list[float], width: int) -> list[list[float]]:
    if width <= 0 or len(values) % width != 0:
        return []
    if len(values) == 0:
        return []
    arr = np.asarray(values).reshape(-1,width)
    return np.round(arr,6).tolist()

def block(matrix: list[list[float]], rows: list[int], columns: list[int]) -> list[list[float]]:
    arr = np.asarray(matrix)
    if arr.size == 0 or len(rows) == 0 or len(columns):
        return []

def column_means(matrix: list[list[float]]) -> list[float]:
    arr = np.asarray(matrix)
    if arr.size == 0 or arr.ndim < 2 or arr.shape[0] == 0:
        return []
    means = arr.mean(axis=0)
    return np.round(means,6).tolist()

def column_range(matrix,column):
    arr = np.asarray(matrix)
    if arr.size == 0 or arr.ndim < 2 or arr.shape[0] == 0:
        return 0.0

    col = arr[:,column]
    diff = col.max() - col.min()
    return float(round(diff,6))
