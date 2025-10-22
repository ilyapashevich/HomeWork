import numpy as np

def multiply_columns_with_k(matrix, k):
    if not (0 <= k < matrix.shape[1]):
        raise ValueError("Индекс K выходит за пределы количества столбцов матрицы.")
    k_column = matrix[:, k]
    result = matrix * k_column[:, np.newaxis]
    
    return result

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

k = 1
result = multiply_columns_with_k(matrix, k)
print(result)