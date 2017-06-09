from flask import Flask
from flask import render_template, url_for, request, redirect
import bdHelper

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

# Menus

@app.route('/cliente')
def cliente():
	return render_template('clientes.html')

@app.route('/funcionario')
def funcionario():
	return render_template('funcionarios.html')

@app.route('/restaurante')
def restaurante():
	return render_template('restaurante.html')

@app.route('/pedido')
def pedido():
	return render_template('pedidos.html')

# fim Menus

# crud clientes

@app.route('/cliente/cadastro')
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
	bdHelper.cadastro_cliente(nome, tel, cpf)
	return redirect(url_for('cliente'))

@app.route('/cliente/search')
def search_cliente():
	return render_template('selecionar_cliente.html')

@app.route('/cliente/results')
def results_cliente_nome():
	return render_template('listar_resultados.html')

@app.route('/cliente/results')
def results_cliente_algo():
	pass

#crud pedidos

@app.route('/pedido/cadastro')
def cadastro_pedido():
	return render_template('cadastro/cadastro_pedido.html')

@app.route('/cadastro/pedido/submit', methods=['POST'])
def pedido_submit():
	nroMesa = None
	nroMesa = request.form['nroMesa']
	bdHelper.cadastro_pedido(nroMesa)
	return redirect(url_for('pedido'))

@app.route('/pedido/search')
def search_pedido():
	return render_template('selecionar_pedido.html')

@app.route('/pedido/results')
def results_pedido_nome():
	return render_template('listar_resultados.html')

@app.route('/pedido/results')
def results_pedido_algo():
	pass

#crud funcionarios

@app.route('/funcionario/cadastro')
def cadastro_funcionario():
	return render_template('cadastrar_funcionarios.html')

@app.route('/funcionario/cadastro/cozinheiro')
def cadastro_cozinheiro():
	return render_template('cadastro/cadastro_cozinheiro.html')

@app.route('/funcionario/cadastro/garcom')
def cadastro_garcom():
	return render_template('cadastro/cadastro_garcom.html')

@app.route('/funcionario/cadastro/<funcao>/submit', methods=['POST'])
def funcionario_submit(funcao):
	nome_funcionario = None
	sal_funcionario = None
	cpf_funcionario = None
	nome_funcionario = request.form['nome_funcionario']
	sal_funcionario = request.form['sal_funcionario']
	cpf_funcionario = request.form['cpf_funcionario']

	if funcao == 'cozinheiro':
		cpf_chefe = None
		cpf_chefe = request.form['cpf_chefe']
		cadastro_cozinheiro(nome_funcionario, sal_funcionario, cpf_funcionario, cpf_chefe)
	else:
		bdHelper.cadastro_garcom(nome_funcionario, sal_funcionario, cpf_funcionario)
	return redirect(url_for('funcionario'))

@app.route('/funcionario/search')
def search_funcionario():
	return render_template('selecionar_funcionario.html')

@app.route('/funcionario/results')
def results_funcionario_nome():
	return render_template('listar_resultados.html')

@app.route('/funcionario/results')
def results_funcionario_algo():
	pass


if __name__ == '__main__':
	app.run(debug=True)