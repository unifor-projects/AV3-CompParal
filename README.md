# Multiplicação de Matrizes - Serial vs Paralelo

Este projeto implementa a multiplicação de matrizes de duas formas:
1. Serial: usando loops for tradicionais
2. Paralela: usando multiprocessing para dividir o trabalho entre múltiplos processos

## Estrutura do Projeto

- `server/`: Contém o servidor Flask que implementa as operações de multiplicação
- `client/`: Contém o cliente que faz as requisições para o servidor
- `output/`: Diretório onde os resultados são salvos

## Como Executar

1. Certifique-se de ter o Docker e Docker Compose instalados
2. Execute o comando:
```bash
docker-compose up --build
```

## Resultados

Os resultados serão salvos no diretório `output/`:
- `matrix_result_serial.txt`: Resultado da multiplicação serial
- `matrix_result_parallel.txt`: Resultado da multiplicação paralela
- `comparison.txt`: Comparação dos tempos de execução entre as duas implementações