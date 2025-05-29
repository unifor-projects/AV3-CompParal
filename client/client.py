import time
import requests
import numpy as np
import os

def generate_random_matrix(rows, cols):
    """Gera uma matriz aleatória com valores entre 0 e 10"""
    return np.random.randint(0, 10, size=(rows, cols)).tolist()

def main(matrix_size):
    # Configuração do servidor
    server_url = "http://server:5000/multiply"
    
    # Gera matrizes aleatórias
    matrix_a = generate_random_matrix(matrix_size, matrix_size)
    matrix_b = generate_random_matrix(matrix_size, matrix_size)
    
    # Testa multiplicação serial
    print("Executando multiplicação serial...")
    serial_response = requests.post(
        server_url,
        json={
            'matrix_a': matrix_a,
            'matrix_b': matrix_b,
            'type': 'serial',
            'matrix_size': matrix_size
        }
    )
    serial_result = serial_response.json()
    
    # Testa multiplicação paralela
    print("Executando multiplicação paralela...")
    parallel_response = requests.post(
        server_url,
        json={
            'matrix_a': matrix_a,
            'matrix_b': matrix_b,
            'type': 'parallel',
            'matrix_size': matrix_size
        }
    )
    parallel_result = parallel_response.json()
    
    # Cria diretório de saída se não existir
    output_dir = 'output'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Salva comparação dos resultados
    comparison_file = os.path.join(output_dir, f'comparison_{matrix_size}x{matrix_size}.txt')
    with open(comparison_file, 'w') as f:
        f.write("Comparação entre multiplicação serial e paralela\n")
        f.write("=" * 50 + "\n\n")
        f.write(f"Tamanho das matrizes: {matrix_size}x{matrix_size}\n\n")
        f.write(f"Tempo serial: {serial_result['execution_time']:.4f} segundos\n")
        f.write(f"Tempo paralelo: {parallel_result['execution_time']:.4f} segundos\n")
        f.write(f"Speedup: {serial_result['execution_time'] / parallel_result['execution_time']:.2f}x\n")

if __name__ == "__main__":
    time.sleep(5)
    matrix_sizes = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000]
    for matrix_size in matrix_sizes:
        main(matrix_size)