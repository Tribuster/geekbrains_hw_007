#   1. Реализовать класс Matrix (матрица).
#   1.1 Обеспечить перегрузку конструктора класса (метод __init__()),
#   который должен принимать данные (список списков) для формирования матрицы.
#   Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
#   Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
#
#   31    32         3    5    32        3    5    8    3
#   37    43         2    4    6         8    3    7    1
#   51    86        -1   64   -8
#   1.2 Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
#   1.3 Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
#   Результатом сложения должна быть новая матрица.
#   Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
#   с первым элементом первой строки второй матрицы и т.д.

class Matrix:
    def __init__(self, list_of_lists):
        self.list_of_lists = list_of_lists

    def __str__(self):
        string = ''
        for i in self.list_of_lists:
            for j in i:
                string = string + '%s\t' % (j)
            string = string[:-1]
            string = string + '\n'
        string = string[:-1]
        return string

    def __add__(self, other):
        result = []
        numbers = []
        for i in range(len(self.list_of_lists)):
            for j in range(len(self.list_of_lists[0])):
                sum = other.list_of_lists[i][j] + self.list_of_lists[i][j]
                numbers.append(sum)
                if len(numbers) == len(self.list_of_lists[0]):
                    result.append(numbers)
                    numbers = []
        return Matrix(result)


lists_one = [[3, 5, 32], [2, 4, 6], [-1, 64, -8]]
lists_two = [[31, 32, 37], [2, -1, -8], [8, 3, 7]]


matix_first = Matrix(lists_one)
matix_second = Matrix(lists_two)


print(f'Первая матрица:\n{matix_first.__str__()}\n')
print(f'Вторая матрица:\n{matix_second.__str__()}\n')
print(f'Сумма матриц:\n{matix_first + matix_second}\n')