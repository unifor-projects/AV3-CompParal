from flask import Flask, request, jsonify
import numpy as np
import time

app = Flask(__name__)

def multiply_matrix_part(matrix_a, matrix_b, start_row, end_row):
    result = np.zeros((end_row - start_row, matrix_b.shape[1]))
    for i in range(start_row, end_row):
        for j in range(matrix_b.shape[1]):
            for k in range(matrix_b.shape[0]):
                result[i - start_row][j] += matrix_a[i][k] * matrix_b[k][j]
    return result

@app.route('/multiply', methods=['POST'])
def multiply():
    data = request.json
    matrix_a = np.array(data['matrix_a'])
    matrix_b = np.array(data['matrix_b'])
    start_row = data['start_row']
    end_row = data['end_row']
    
    start_time = time.time()
    result = multiply_matrix_part(matrix_a, matrix_b, start_row, end_row)
    end_time = time.time()
    
    return jsonify({
        'result': result.tolist(),
        'execution_time': end_time - start_time
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)