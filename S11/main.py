from typing import List

import random

import copy

def generate_matrix(filas, columnas):
    matrix:List[List[int]] = []

    for i in range(filas):
        matrix.append([])
        for j in range(columnas):
            num = int(input(f"Enter the number of the position [{i}][{j}]: "))
            matrix[i].append(num)
    
    return matrix


def escalar(matrix:List[List[int]], escalar):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = matrix[i][j] * escalar
    return matrix


def escalar_2(matrix:List[List[int]], escalar):
    for i in range(len(matrix)):
        matrix[i] = list(map( lambda value: value * escalar, matrix[i] ))
    return matrix


def escalar_2(matrix:List[List[int]], escalar):
    for i in range(len(matrix)):
        matrix[i] = list(map( lambda value: value * escalar, matrix[i] ))
    return matrix

def odd(x):
    if x <= 0: return 0

    return 2*x-1 + odd(x-1)

if __name__ == "__main__":
    # matrix = generate_matrix(4, 3)
    # matrix_new = escalar(copy.deepcopy(matrix), 2) 
    # matrix_new_2 = escalar_2(copy.deepcopy(matrix), 2)
    # print(matrix)
    # print(matrix_new)
    # print(matrix_new_2)

    odd(10)

