def get_matrix(n, m, value): # определяем функцию с тремя параметрами
    matrix = []  # создаем пустой список (матрицу)
    for i in range(n):
        matrix.append([]) # наполняем матрицу строками
        for j in range(m):
            matrix[i].append(value) # наполняем строки значениями
    return matrix
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)