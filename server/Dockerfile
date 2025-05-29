FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# Expondo a porta de debug do Python
EXPOSE 5000 5678

# Iniciando o servidor com debugger
# CMD ["python", "-m", "debugpy", "--listen", "0.0.0.0:5678", "--wait-for-client", "server.py"]
CMD ["python", "-m", "debugpy", "--listen", "0.0.0.0:5678", "server.py"]