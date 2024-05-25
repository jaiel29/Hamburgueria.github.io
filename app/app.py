from flask import Flask, render_template, request, redirect, url_for, session, flash 
import os
import mysql.connector
from dotenv import load_dotenv 
from pathlib import Path
from werkzeug.security import generate_password_hash, check_password_hash 

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

app = Flask(__name__, static_folder='../assets',template_folder='../pages')
app.secret_key = os.getenv('SECRET_KEY', os.urandom(24))


@app.route('/')
def index():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('index.html')

@app.route('/lanche', methods=['GET', 'POST'])
def lanche():
    print("Entrou na rota /lanche")
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT e.nomeItem, c.preco FROM Estoque e INNER JOIN Cardapio c ON e.idItem = c.idItem WHERE e.tipoItem = 'lanche'")
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
    for nomeLanche, quantidade in zip(nomeLanches, quantidades):
        cursor.execute("INSERT INTO Pedido (idCliente, itemPed, valTotal, dataHoraPed) VALUES (%s, %s, %s, NOW())", (session['idCliente'], nomeLanche, quantidade, ))
        connection.commit()
   # for nomeLanche in nomeLanches:
    #    cursor.execute("INSERT INTO Pedido (nome_do_pedido) VALUES (%s)", (nomeLanche,))
     #   connection.commit()
    #for quantidade in quantidades:
      #  cursor.execute("INSERT INTO Pedido (quantidade) VALUES (%s)", (quantidade,))
       # connection.commit()
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
        #username = request.form['login']
        cpf = request.form['cpf']
        email = request.form['email']
        telefone = request.form['telefone']
        endereco = request.form['endereco']
        password = request.form['senha']


        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO Cadastro (cpf, email, telefone, endereco, senha) VALUES (%s, %s, %s, %s, %s)", (cpf, email, telefone, endereco, password))
        connection.commit()
        
        #obtém o idCadastro inserido
        idCadastro = cursor.lastrowid
        
        #inserindo o cliente associado ao idCadastro
        cursor.execute("INSERT INTO Cliente (idCadastro) VALUES (%s)", (idCadastro,))
        connection.commit()

        cursor.close()
        connection.close()

        return redirect(url_for('login'))

    return render_template('cadastro.html')

def verify_credentials(username, password):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Cadastro WHERE email = %s AND senha = %s", (username, password))
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
        username = request.form.get('login')
        password = request.form.get('senha')
        

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
