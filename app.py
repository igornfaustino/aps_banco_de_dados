from flask import Flask
from flask import render_template, url_for, request, redirect


app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

# Menus

@app.route('/clientes')
def clientes():
	return render_template('clientes.html')

@app.route('/funcionarios')
def funcionarios():
	return render_template('funcionarios.html')

@app.route('/restaurante')
def restaurante():
	return render_template('restaurante.html')

@app.route('/pedidos')
def pedidos():
	return render_template('pedidos.html')

# fim Menus

@app.route('/cadastro/cliente')
def cadastro_cliente():
	return render_template('cadastro/cadastro_cliente.html')	

@app.route('/cadastro/cliente/submit', methods=['POST'])
def cliente_submit():
	nome = None
	tel = None
	cpf = None
	nome = request.form['nome_cliente']
	tel = request.form['tel_cliente']
	cpf = request.form['cpf_cliente']
	return redirect(url_for('clientes'))

if __name__ == '__main__':
	app.run(debug=True)