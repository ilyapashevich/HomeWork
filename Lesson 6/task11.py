def sum_with_row(matrix, l):
    if l < 0 or l >= len(matrix):
        raise ValueError("Индекс строки L выходит за пределы матрицы.")
    
    l_row = matrix[l]
    result = []
    
    for row in matrix:
        summed_row = [row[i] + l_row[i] for i in range(len(row))]
        result.append(summed_row)
    
    return result

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

l = 1
result = sum_with_row(matrix, l)
print(result)