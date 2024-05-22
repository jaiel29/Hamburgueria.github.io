import mysql.connector
import os
from dotenv import load_dotenv
from pathlib import Path

# Carregar variáveis de ambiente do arquivo .env
dotenv_path = Path('.env')
load_dotenv(dotenv_path=dotenv_path)

# Obter variáveis de ambiente
host = os.getenv('HOST_NAME')
usuario = os.getenv('USER_NAME')
senha = os.getenv('PWD_NAME')
database = os.getenv('DB_NAME')

# Conectar ao banco de dados
db_connection = mysql.connector.connect(
    host=host,
    user=usuario,
    password=senha,
    database=database
)
cursor = db_connection.cursor()

# Inserir lanches no banco de dados
lanches = [
    (1, 'Cheeseburger Nove', 40.60),
    (2, 'Choripám', 44.10),
    (3, 'Nove Chicken Grelhado', 48.80),
    (4, 'Nove Supreme', 34.60),
    (5, 'Nove Vegetariano', 44.90),
    (6, 'Nove Vegetariano Fit', 34.60),
    (7, 'Nove Vegano', 44.90)
]

# Query de inserção
insert_query = """
INSERT INTO lanche (codigoLanche, nomeLanche, preco)
VALUES (%s, %s, %s)
"""

# Executar a inserção de cada lanche
for lanche in lanches:
    cursor.execute(insert_query, lanche)

# Confirmar as mudanças no banco de dados
db_connection.commit()

# Fechar a conexão
cursor.close()
db_connection.close()

print("Lanches inseridos com sucesso!")
