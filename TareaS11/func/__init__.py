from utils import generate_random_matrix
from utils import get_max_position_from_matrix
from utils import get_min_position_from_matrix
from utils import organize_matrix

def matrix_custom():
    matrix = generate_random_matrix(5, 10)
    print("Matrix: ")
    print(matrix)

    row_max, column_max = get_max_position_from_matrix(matrix)
    print(f"Max number in matrix: { matrix[row_max][column_max] }. Position: [{row_max}][{column_max}]")

    row_min, column_min = get_min_position_from_matrix(matrix)
    print(f"Min number in matrix: { matrix[row_min][column_min] }. Position: [{row_min}][{column_min}]")

    matrix_organized = organize_matrix(matrix)
    print("Organized matrix: ")
    print(matrix_organized)

def recursive_custom(n, p):
    if n == 1: return p

    return n * p + recursive_custom(n-1, p)

def recursive_fibo(max_value, a=0, b=1):
    if max_value <= 0: return a + b

    print(f"{a}, {b}: {a + b}")

    return recursive_fibo(max_value - 1, a=b, b=a + b)
