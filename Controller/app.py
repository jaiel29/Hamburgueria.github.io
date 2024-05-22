from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
import os
from dotenv import load_dotenv
from pathlib import Path
import config

dotenv_path = Path('.env')
load_dotenv(dotenv_path=dotenv_path)

app = Flask(__name__, static_folder='../View/assets',template_folder='../View/pages')

def get_db_connection():
    host = os.getenv('HOST_NAME')
    usuario = os.getenv('USER_NAME')
    senha = os.getenv('PWD_NAME')
    database = os.getenv('DB_NAME')

    return mysql.connector.connect(
        host=host,
        user=usuario,
        password=senha
        database=database
    )

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cardapio')
def cardapio():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM lanche")
    cardapio_itens = cursor.fetchall()
    cursor.close()
    connection.close()

    return render_template('cardapio.html', cardapio_itens=cardapio_itens)
    #return render_template('cardapio.html')

@app.route('/lanche', methods=['GET', 'POST'])
def lanche():
    print("Entrou na rota /lanche")
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM LANCHE")
    lanches = cursor.fetchall()
    cursor.close()
    connection.close()
    
    return render_template('lanches.html', lanches=lanches)


@app.route('/bebidas')
def bebidas():
    return render_template('bebidas.html')
    #return render_template('cardapio3.html')

@app.route('/porcoes')
def porcoes():
    return render_template('porcoes.html')
    #return render_template('pedidos.html')

@app.route('/pagamento', methods=['POST', 'GET'])
def pagamento():
     # Recebe os dados do formulário
    nomeLanches = request.form.getlist('pedidos')
    quantidades = request.form.getlist('quantidade')


    # Adiciona o lanche selecionado na tabela de pedidos (exemplo)
    connection = get_db_connection()
    cursor = connection.cursor()
    for nomeLanche in nomeLanches:
        cursor.execute("INSERT INTO pedidos (nome_do_pedido) VALUES (%s)", (nomeLanche,))
        connection.commit()
    for quantidade in quantidades:
        cursor.execute("INSERT INTO pedidos (quantidade) VALUES (%s)", (quantidade,))
        connection.commit()
    cursor.close()
    connection.close()

    return render_template('index.pg7.html')

@app.route('/pagamento-bem-sucedido')
def pagamentosucesso():
    return render_template('pagamento_feito_com_sucesso.html')

@app.route('/status-pedido')
def pedidostatus():
    return render_template('status_do_pedido.html')

if __name__ == '__main__':
    app.run(debug=True)
