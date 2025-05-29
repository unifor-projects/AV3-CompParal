import time
import numpy as np

def matrix_multiply_serial(matrix_a, matrix_b):
    """
    Multiplica duas matrizes usando loops for (implementação serial)
    """
    start_time = time.time()
    
    # rows_a = len(matrix_a)
    # cols_a = len(matrix_a[0])
    # cols_b = len(matrix_b[0])
    
    # result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]
    
    # for i in range(rows_a):
    #     for j in range(cols_b):
    #         for k in range(cols_a):
    #             result[i][j] += matrix_a[i][k] * matrix_b[k][j]
    
    matrix_a = np.array(matrix_a)
    matrix_b = np.array(matrix_b)
    
    # Usando operador @ do numpy
    result = matrix_a @ matrix_b
    result = result.tolist()
    
    end_time = time.time()
    execution_time = end_time - start_time
    
    return result, execution_time