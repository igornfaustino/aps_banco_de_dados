from flask import Flask
from flask import render_template, url_for, request, redirect
from bdHelper import bdHelper

app = Flask(__name__)
sql = bdHelper()

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

####### Cadastrar #######

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
	sql.cadastro_cliente(nome, tel, cpf)
	return redirect(url_for('cliente'))

########################
####### Exibir #########

@app.route('/cliente/search')
def search_cliente():
	return render_template('selecionar_cliente.html')

@app.route('/cliente/results')
def results_cliente_nome():
	nome = request.args.get('nome')
	results = sql.search_cliente(nome=nome)
	return render_template('listar_resultados.html', results=results)

@app.route('/cliente/results')
def results_cliente_algo():
	pass

@app.route('/cliente/<nome>')
def exibir_clientes(nome):
	id = request.args.get('id')
	results = sql.search_cliente(idCli=id)
	return render_template('exibir_cliente.html', results=results)

########################
####### Alterar ########

@app.route('/cliente/alterar/<id>/')
def cliente_nome(id):
	return render_template('alterar.html', name="Nome", action=url_for('cliente_nome_submit', id=id), type="text", label="Novo Nome")

@app.route('/cliente/alterar/<id>/submit', methods=['POST'])
def cliente_nome_submit(id):
	novo = request.form['alt']
	sql.alter_cliente_nome(idCli=id, nome=novo)
	return redirect(url_for('cliente'))

@app.route('/cliente/alterar/<id>/')
def cliente_tel(id):
	return render_template('alterar.html', name="Tel", action=url_for('cliente_nome_submit', id=id), type="tel", label="Novo Telefone")

@app.route('/cliente/alterar/<id>/submit', methods=['POST'])
def cliente_tel_submit(id):
	novo = request.form['alt']
	sql.alter_cliente_tel(idCli=id, tel=novo)
	return redirect(url_for('cliente'))

@app.route('/cliente/alterar/<id>/')
def cliente_cpf(id):
	return render_template('alterar.html', name="CPF", action=url_for('cliente_nome_submit', id=id), type="text", label="Novo CPF")

@app.route('/cliente/alterar/<id>/submit', methods=['POST'])
def cliente_cpf_submit(id):
	novo = request.form['alt']
	sql.alter_cliente_nome(idCli=id, cpf=novo)
	return redirect(url_for('cliente'))

########################
######## Remover #######

@app.route('/cliente/<nome>/<idCli>/remove', methods=["POST"])
def rm_cliente(nome, idCli):
	sql.rm_cliente(idCli=idCli)
	return redirect(url_for('cliente'))

#crud pedidos

@app.route('/pedido/cadastro')
def cadastro_pedido():
	return render_template('cadastro/cadastro_pedido.html')

@app.route('/cadastro/pedido/submit', methods=['POST'])
def pedido_submit():
	nroMesa = None
	nroMesa = request.form['nroMesa']
	sql.cadastro_pedido(nroMesa)
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