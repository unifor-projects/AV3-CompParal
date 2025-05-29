from flask import Flask, request, jsonify
from matrix_operations_serial import matrix_multiply_serial
from matrix_operations_parallel import matrix_multiply_parallel
import json
import os
import traceback

app = Flask(__name__)

@app.route('/multiply', methods=['POST'])
def multiply_matrices():
    try:
        data = request.get_json()
        matrix_a = data['matrix_a']
        matrix_b = data['matrix_b']
        operation_type = data.get('type', 'serial')
        matrix_size = data.get('matrix_size', 100)
        
        print(f"Iniciando multiplicação {operation_type} para matrizes {matrix_size}x{matrix_size}")
        
        if operation_type == 'serial':
            result, execution_time = matrix_multiply_serial(matrix_a, matrix_b)
        else:
            result, execution_time = matrix_multiply_parallel(matrix_a, matrix_b)
        
        print(f"Multiplicação {operation_type} concluída em {execution_time:.4f} segundos")
        
        # Salva o resultado no arquivo de saída
        output_dir = 'output'
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        output_file = os.path.join(output_dir, f'matrix_result_{operation_type}_{matrix_size}x{matrix_size}.txt')
        with open(output_file, 'w') as f:
            f.write(f'Tipo de operação: {operation_type}\n')
            f.write(f'Tempo de execução: {execution_time:.4f} segundos\n')
            f.write('Resultado:\n')
            f.write(json.dumps(result, indent=2))
        
        return jsonify({
            'result': result,
            'execution_time': execution_time,
            'type': operation_type
        })
    except Exception as e:
        print(f"Erro no servidor: {str(e)}")
        print(traceback.format_exc())
        return jsonify({
            'error': str(e),
            'traceback': traceback.format_exc()
        }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)