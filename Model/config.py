import mysql.connector
import os
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path('Model/.env.local')
load_dotenv(dotenv_path=dotenv_path)

host = os.getenv('HOST_NAME')
usuario = os.getenv('USER_NAME')
senha = os.getenv('PWD_NAME')
database = os.getenv('DB_NAME')

# Verificar se as variáveis de ambiente foram carregadas corretamente
print(f"Host: {host}")
print(f"Usuário: {usuario}")
print(f"Senha: {'*****' if senha else 'None'}")
print(f"Database: {database}")

try:
    db_connection = mysql.connector.connect(
        host=host,
        user=usuario,
        password=senha,
        database=database
    )
    print(db_connection)
    # Teste de conexão
    if db_connection.is_connected():
        print("Conectado com sucesso")
    else:
        print("Algo deu errado")

except mysql.connector.Error as erro:
    print("Algo deu errado:", erro)
