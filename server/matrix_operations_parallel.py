import numpy as np
import multiprocessing as mp
import time

# Configura o método de inicialização do multiprocessing
mp.set_start_method('spawn', force=True)

def multiply_chunk(args):
    """
    Multiplica um chunk de linhas da matriz A com a matriz B
    """
    try:
        chunk, matrix_b = args
        # result = np.zeros((len(chunk), matrix_b.shape[1]))
        
        # for i, row in enumerate(chunk):
        #     for j in range(matrix_b.shape[1]):
        #         for k in range(matrix_b.shape[0]):
        #             result[i, j] += row[k] * matrix_b[k, j]
        
        # return result
        chunk = np.array(chunk)
        matrix_b = np.array(matrix_b)
        result = chunk @ matrix_b  # Usando operador @ do numpy
        return result.tolist()
    except Exception as e:
        print(f"Erro no chunk: {str(e)}")
        raise

def matrix_multiply_parallel(matrix_a, matrix_b, num_processes=None):
    """
    Multiplica duas matrizes usando processamento paralelo
    """
    try:
        start_time = time.time()
        
        if num_processes is None:
            num_processes = mp.cpu_count()
        
        # Converte para numpy arrays
        matrix_a = np.array(matrix_a)
        matrix_b = np.array(matrix_b)
        
        # Divide a matriz A em chunks
        chunk_size = matrix_a.shape[0] // num_processes
        chunks = [matrix_a[i:i + chunk_size] for i in range(0, matrix_a.shape[0], chunk_size)]
        
        # Cria um pool de processos
        with mp.Pool(processes=num_processes) as pool:
            # Mapeia cada chunk para um processo
            results = pool.map(multiply_chunk, [(chunk, matrix_b) for chunk in chunks])
        
        # Combina os resultados
        final_result = np.vstack(results)
        
        end_time = time.time()
        execution_time = end_time - start_time
        
        return final_result.tolist(), execution_time
    except Exception as e:
        print(f"Erro na multiplicação paralela: {str(e)}")
        raise 