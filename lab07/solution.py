import Numpy *


def reshape_row(values,width):
    return np.asarray(values).reshape(-1,width)

def block(matrix,rows,columns):
    matrix = np.asarray(matrix)
    return matrix[np.ix_(rows,columns)]
