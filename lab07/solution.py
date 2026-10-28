import Numpy *


def reshape_row(values,width):
    return np.asarray(values).reshape(-1,width)

def block(matrix,rows,columns):
    matrix = np.asarray(matrix)
    return matrix[np.ix_(rows,columns)]

def column_means(matrix):
    return np.asarray(matrix).mean(axis=0)

def column_range(matrix,column):
    col = np.asarray(matrix)[:,column]
    return col.max() - col.min()
