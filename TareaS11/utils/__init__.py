from typing import List

import random

def generate_random_matrix(rows, columns) -> List[List[int]]:
    matrix = []

    if rows <= 0: raise Exception("Rows Out of range")
    if columns <= 0: raise Exception("Columns Out of range")

    for _i in range(rows):
        row = []

        for _j in range(columns):
            row.append( random.randint(0, 50) )

        matrix.append(row)
    
    return matrix

def get_max_position_from_matrix(matrix:List[List[int]]):
    index_column_max_of_every_row = []
    max_of_every_row = []

    for row in matrix:
        max_value = max(row)
        index_column_max_of_every_row.append( row.index(max_value) )
        max_of_every_row.append( max_value )

    num_max = max(max_of_every_row)
    index_max = max_of_every_row.index(num_max)

    row_max = index_max
    column_max = index_column_max_of_every_row[index_max]

    return row_max, column_max

def get_min_position_from_matrix(matrix:List[List[int]]):
    index_min_column_of_every_row = []
    min_of_every_row = []

    for row in matrix:
        min_value = min(row)
        index_min_column_of_every_row.append( row.index(min_value) )
        min_of_every_row.append( min_value )

    num_max = min(min_of_every_row)
    index_min = min_of_every_row.index(num_max)

    row_min = index_min
    column_min = index_min_column_of_every_row[index_min]

    return row_min, column_min

def organize_matrix(matrix:List[List[int]]):
    new_matix = []

    nums_sorted = []

    for row in matrix:
        nums_sorted.extend(row)

    nums_sorted.sort()

    for row in matrix:
        new_row = []

        for _ in row:
            new_row.append( nums_sorted.pop(0) )

        new_matix.append(new_row)

    return new_matix
