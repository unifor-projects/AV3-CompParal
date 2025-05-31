import numpy as np
import requests
import time
import json
from concurrent.futures import ThreadPoolExecutor
import os

def generate_matrix(size):
    return np.random.randint(1, 100, size=(size, size))

def multiply_serial(matrix_a, matrix_b):
    start_time = time.time()
    n = len(matrix_a)
    result = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]
    end_time = time.time()
    return end_time - start_time

def multiply_distributed(matrix_a, matrix_b, num_servers):
    matrix_size = len(matrix_a)
    rows_per_server = matrix_size // num_servers
    extra_rows = matrix_size % num_servers
    
    start_time = time.time()
    
    def process_chunk(server_id):
        start_row = server_id * rows_per_server + min(server_id, extra_rows)
        end_row = start_row + rows_per_server + (1 if server_id < extra_rows else 0)
        
        print(f"Iniciando requisição para o servidor {server_id+1}")
        response = requests.post(
            f'http://server{server_id + 1}:5000/multiply',
            json={
                'matrix_a': matrix_a.tolist(),
                'matrix_b': matrix_b.tolist(),
                'start_row': start_row,
                'end_row': end_row
            }
        )
        print(f"Requisição finalizada para o servidor {server_id+1}")
        return response.json()
    
    with ThreadPoolExecutor(max_workers=num_servers) as executor:
        results = list(executor.map(process_chunk, range(num_servers)))
    
    end_time = time.time()
    return end_time - start_time

def run_experiment(matrix_size):
    matrix_a = generate_matrix(matrix_size)
    matrix_b = generate_matrix(matrix_size)
    
    # Tempo serial
    print("Iniciando multiplicação serial")
    serial_time = multiply_serial(matrix_a, matrix_b)
    
    # Tempo distribuído
    print("Iniciando multiplicação destribuida")
    distributed_time = multiply_distributed(matrix_a, matrix_b, 6)
    
    return {
        'matrix_size': matrix_size,
        'serial_time': serial_time,
        'distributed_time': distributed_time
    }

def main():
    matrix_sizes = [100, 300, 500, 700, 900, 1100]
    results = []
    
    for size in matrix_sizes:
        print("======================")
        print(f"Executando experimento para matriz {size}x{size}")
        print("======================")
        result = run_experiment(size)
        results.append(result)
        
        # Salvar resultados em arquivo
        with open(f'/app/output/results_{size}.txt', 'w') as f:
            f.write(f"Tamanho da matriz: {size}x{size}\n")
            f.write(f"Tempo serial: {result['serial_time']:.4f} segundos\n")
            f.write(f"Tempo distribuído: {result['distributed_time']:.4f} segundos\n")
            f.write(f"Speedup: {result['serial_time']/result['distributed_time']:.4f}x\n")

if __name__ == '__main__':
    time.sleep(30)
    main()