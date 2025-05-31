# Análise da Multiplicação de Matrizes - Serial vs Paralelo

## 1. Atividade Prática

O projeto implementa um sistema distribuído para multiplicação de matrizes, comparando duas abordagens:

### Implementação Serial
- Utiliza loops for tradicionais para realizar a multiplicação de matrizes
- Processa toda a operação em um único processo
- Implementada diretamente no cliente

### Implementação Paralela
- Utiliza uma arquitetura cliente-servidor com 6 servidores
- Divide a matriz em partes iguais entre os servidores
- Cada servidor processa uma parte da multiplicação
- Utiliza ThreadPoolExecutor para gerenciar as requisições paralelas
- Os resultados são combinados no cliente

### Estrutura do Sistema
- Cliente: Gera as matrizes e coordena o processamento
- Servidores: Processam partes específicas da multiplicação
- Docker: Utilizado para containerização dos componentes
- Flask: Framework web para comunicação cliente-servidor

## 2. Conclusão

Baseado nos resultados dos experimentos com diferentes tamanhos de matriz, podemos observar:

### Análise de Performance
- Matriz 100x100:
  - Serial: 0.3760s
  - Paralelo: 0.3097s
  - Speedup: 1.2141x

- Matriz 300x300:
  - Serial: 10.0260s
  - Paralelo: 11.4855s
  - Speedup: 0.8729x

- Matriz 500x500:
  - Serial: 59.7008s
  - Paralelo: 59.6767s
  - Speedup: 1.0004x

- Matriz 700x700:
  - Serial: 161.8892s
  - Paralelo: 162.4670s
  - Speedup: 0.9964x

- Matriz 900x900:
  - Serial: 341.8680s
  - Paralelo: 343.7598s
  - Speedup: 0.9945x

- Matriz 1100x1100:
  - Serial: 627.2624s
  - Paralelo: 625.4124s
  - Speedup: 1.0030x

### Observações
1. Para matrizes pequenas (100x100), a versão paralela apresentou melhor performance devido ao baixo overhead de comunicação
2. Para matrizes médias e grandes, o overhead de comunicação entre os servidores compensou os ganhos de paralelização
3. O speedup foi próximo de 1.0 para a maioria dos casos, indicando que o sistema distribuído não trouxe benefícios significativos de performance
4. A escalabilidade do sistema foi limitada pelo overhead de comunicação entre os componentes

### Recomendações
1. Otimizar a comunicação entre cliente e servidores
2. Considerar o uso de bibliotecas otimizadas como NumPy para operações vetoriais
3. Avaliar a possibilidade de aumentar o número de servidores para matrizes maiores
4. Implementar técnicas de cache para reduzir o overhead de comunicação 