import numpy as np


hours = np.arange(0, 22, 3)           
line = np.linspace(0, 1, 5)            
zeros = np.zeros(6, dtype=int)      
unknown_table = np.full((2, 3), -1)
identity = np.eye(3)

print("Задание 1")
print("hours:", hours)
print("shape:", hours.shape)
print("ndim:", hours.ndim)
print("size:", hours.size)
print("dtype:", hours.dtype)
print("line:", line)
print("zeros:", zeros)
print("unknown_table:\n", unknown_table)
print("identity:\n", identity)




print("\nЗадание 2")
print("третий элемент:", hours[2])
print("последний элемент:", hours[-1])
print("индексы 2-5:", hours[2:6])  
print("каждый второй:", hours[::2])
print("в обратном порядке:", hours[::-1])


temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18],
])

print("\nЗадание 3")
print("форма:", temperatures.shape)
print("число измерений:", temperatures.ndim)
print("число элементов:", temperatures.size)
print("вторая строка, третий столбец:", temperatures[1, 2])
print("первая строка:", temperatures[0])
print("последний столбец:", temperatures[:, -1])
print("первые две строки без первого столбца:\n", temperatures[:2, 1:])
center = temperatures[:2, 1:3]
print("центральный фрагмент 2x2:\n", center)
print("форма фрагмента:", center.shape)


matrix = np.arange(1, 26).reshape(5, 5)

print("\nЗадание 4")
print("исходная матрица:\n", matrix)

first_rows = matrix[:3]
print("первые три строки:\n", first_rows)
print("shape:", first_rows.shape)

last_rows = matrix[-2:]
print("последние две строки:\n", last_rows)
print("shape:", last_rows.shape)

first_cols = matrix[:, :2]
print("первые два столбца:\n", first_cols)
print("shape:", first_cols.shape)

inner = matrix[1:4, 2:5]
print("строки 1-3, столбцы 2-4:\n", inner)
print("shape:", inner.shape)

corner = matrix[-2:, -2:]
print("правый нижний угол 2x2:\n", corner)
print("shape:", corner.shape)


vector = np.array([10, 20, 30, 40, 50])
vector[1:4] = 0
print("\nЗадание 5")
print("vector после vector[1:4] = 0:", vector)

small_matrix = np.arange(1, 10).reshape(3, 3)
small_matrix[0, :] = -1
small_matrix[1:, 1:] = 9
print("small_matrix:\n", small_matrix)


changed_hours = hours.copy()
changed_hours[2:5] = 99
changed_hours[::2] = -1
print("changed_hours:", changed_hours)
print("исходный hours:", hours)


changed_matrix = matrix.copy()
changed_matrix[1, :] = 0               
changed_matrix[:, -1] = -1             
changed_matrix[1:4, 1:4] = 100         
print("changed_matrix:\n", changed_matrix)
print("исходная matrix:\n", matrix)



numbers = np.arange(12)
table = numbers.reshape(3, 4)
transposed = table.T

print("\nЗадание 6")
print("форма numbers:", numbers.shape)
print("форма table:", table.shape)
print("форма transposed:", transposed.shape)
