from flask import Flask, render_template, request, redirect, url_for, session, flash
import mysql.connector
import os
from dotenv import load_dotenv
from pathlib import Path
import config
from werkzeug.security import generate_password_hash, check_password_hash

dotenv_path = Path('.env.local')
load_dotenv(dotenv_path=dotenv_path)

app = Flask(__name__, static_folder='../View/assets',template_folder='../View/pages')
app.secret_key = os.getenv('SECRET_KEY', os.urandom(24))

def get_db_connection():
    host = os.getenv('HOST_NAME')
    usuario = os.getenv('USER_NAME')
    senha = os.getenv('PWD_NAME')
    database = os.getenv('DB_NAME')

    return mysql.connector.connect(
        host=host,
        user=usuario,
        password=senha,
        database=database
    )

@app.route('/')
def index():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
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

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        username = request.form['login']
        password = request.form['senha']
        idusuario = request.form['cpf']
        permissao = request.form['telefone']

        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO usuario (idusuario, nome, senha, permissao) VALUES (%s, %s, %s, %s)", (idusuario, username, password, permissao))
        connection.commit()
        cursor.close()
        connection.close()

        return redirect(url_for('login'))

    return render_template('cadastro.html')

def verify_credentials(username, password):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM usuario WHERE nome = %s", (username,))
    user = cursor.fetchone()
    cursor.close()
    connection.close()

    if user and user['senha'] == password:
        return True
    else:
        return False

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['login']
        password = request.form['senha']
        
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM usuario WHERE nome = %s", (username,))
        user = cursor.fetchone()
        cursor.close()
        connection.close()

        if verify_credentials(username, password):
            session['logged_in'] = True
            session['username'] = username
            return redirect(url_for('index'))
        else:
            mensagem = 'E-mail ou senha incorretos. Tente novamente.'
            return render_template('login.html', mensagem=mensagem)

    
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
