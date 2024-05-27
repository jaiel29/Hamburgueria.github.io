from flask import Flask, render_template, request, redirect, url_for, session 
import os
import psycopg2
from dotenv import load_dotenv 
from pathlib import Path

dotenv_path = Path('environment/.env')
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
    
    db_connection =  psycopg2.connect(
        host=host,
        user=usuario,
        password=senha,
        database=database
    )    
    print("Conectado com sucesso")
except psycopg2.Error as e:
    print("Algo deu errado:", e)