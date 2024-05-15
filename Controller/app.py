from flask import Flask, render_template
#from config import db_connection

app = Flask(__name__, static_folder='../View/assets',template_folder='../View/pages')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cardapio')
def cardapio():
    return render_template('index.pg5.html')
    #return render_template('cardapio.html')

@app.route('/cardapio2')
def cardapio2():
    return render_template('index.pg4.html')
    
    #return render_template('cardapio2.html')
    #numero_pedido = request.form['numero_pedido']
    #nome_do_pedido = request.form['nome_do_pedido']
    #quantidade = request.form['quantidade']

@app.route('/cardapio3', methods=['POST'])
def cardapio3():
    return render_template('index.pg3.html')
    #return render_template('cardapio3.html')

@app.route('/pedidos')
def pedidos():
    return render_template('index.pg2.html')
    #return render_template('pedidos.html')

@app.route('/pagamento', methods=['POST'])
def pagamento():
    return render_template('index.pg7.html')
    #return render_template('pagamento.html')

if __name__ == '__main__':
    app.run(debug=True)
