# def get_matrix(n, m, value):
#     matrix = []
#     for n1 in n():
#         n1.append(n(matrix))

def get_matrix(n, m, value):
    # Проверка на некорректные размеры
    if n <= 0 and m <= 0:
        return []  # Возвращаем пустой список, если размеры некорректны

    # Создаём пустую матрицу
    matrix = []

    # Внешний цикл для строк
    for _ in range(n):
        # Создаём строку и заполняем её значением `value`
        row = []
        for _ in range(m):
            row.append(value)

        # Добавляем строку в матрицу
        matrix.append(row)

    # Возвращаем полученную матрицу
    return matrix

# Примеры использования функции
result1 = get_matrix(int(input('enter n: ')), int(input('enter m: ')), int(input('enter value: ')))
result2 = get_matrix(int(input('enter n: ')), int(input('enter m: ')), int(input('enter value: ')))
result3 = get_matrix(int(input('enter n: ')), int(input('enter m: ')), int(input('enter value: ')))

# Вывод результатов
print(result1)
print(result2)
print(result3)


