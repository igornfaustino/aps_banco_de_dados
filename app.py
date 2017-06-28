from flask import Flask
from flask import render_template, url_for, request, redirect
from bdHelper import bdHelper

app = Flask(__name__)
sql = bdHelper()

@app.route('/')
def index():
	results = sql.get_pedido()
	return render_template('index.html', results=results)

# Menus

@app.route('/cliente')
def cliente():
	cadastro = request.args.get('cadastro')
	rm = request.args.get('rm')
	return render_template('clientes.html', cadastro=cadastro, rm=rm)

@app.route('/funcionario')
def funcionario():
	cadastro = request.args.get('cadastro')
	rm = request.args.get('rm')
	return render_template('funcionarios.html', cadastro=cadastro, rm=rm)

@app.route('/restaurante')
def restaurante():
	return render_template('restaurante.html')

@app.route('/restaurante/cardapio')
def cardapio():
	cadastro = request.args.get('cadastro')
	rm = request.args.get('rm')
	return render_template('cardapio.html', cadastro=cadastro, rm=rm)

@app.route('/restaurante/mesa')
def mesa():
	cadastro = request.args.get('cadastro')
	rm = request.args.get('rm')
	return render_template('mesa.html', cadastro=cadastro, rm=rm)

@app.route('/restaurante/reserva')
def reserva():
	cadastro = request.args.get('cadastro')
	rm = request.args.get('rm')
	return render_template('selecionar_reserva.html', cadastro=cadastro, rm=rm)

@app.route('/pedido')
def pedido():
	empty = request.args.get('empty')
	cadastro = request.args.get('cadastro')
	fim = request.args.get('fim')
	can = request.args.get('can')
	rm = request.args.get('rm')
	return render_template('pedidos.html', empty=empty, cadastro=cadastro, fim=fim, can=can, rm=rm)

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
	cadastro = sql.cadastro_cliente(nome, tel, cpf)
	return redirect(url_for('cliente', cadastro=cadastro))

########################
####### Exibir #########

@app.route('/cliente/search')
def search_cliente():
	return render_template('selecionar_cliente.html')

@app.route('/cliente/results')
def results_cliente_nome():
	nome = request.args.get('nome')
	if not nome:
		results = sql.getall_clientes()
	else:
		results = sql.search_cliente(nome=nome)
	return render_template('listar_resultados_cliente.html', results=results)

@app.route('/cliente/results/sem_reservas')
def results_cliente_mes():
	mes = request.args.get('mes')
	if mes:
		results = sql.clientes_sem_reserva(mes=mes)
	else:
		results = ()
	return render_template('listar_resultados_cliente.html', results=results)

@app.route('/cliente/results/algo')
def results_cliente_algo():
	condicao = request.args.get('condicao')
	if not condicao:
		return redirect(url_for('search_cliente'))
	if condicao == 'todas_mesas':
		results = sql.clientes_todas_mesas()
	elif condicao == 'mais_reservas':
		results = sql.clientes_mais_reservas()
	elif condicao == 'media':
		results = sql.media_cliente()
		return render_template('listar_resultados_cliente_media.html', results=results)
	return render_template('listar_resultados_cliente.html', results=results)

@app.route('/cliente/results/minimo')
def results_cliente_minimo_reserva():
	minimo = request.args.get('numero_minimo')
	results = sql.clientes_mais_reservas_que(num=minimo)
	return render_template('listar_resultados_cliente.html', results=results)

@app.route('/cliente/')
def exibir_clientes():
	id = request.args.get('id')
	alt = request.args.get('alt')
	results = sql.search_cliente(idCli=id)
	reserva = request.args.get('reserva')
	return render_template('exibir_cliente.html', results=results, alt=alt, reserva=reserva)

########################
####### Alterar ########

@app.route('/cliente/alterar/nome')
def cliente_nome():
	id = request.args.get('id')
	return render_template('alterar.html', name="Nome", action=url_for('cliente_nome_submit', id=id), type="text", label="Novo Nome")

@app.route('/cliente/alterar/nome/submit', methods=['POST'])
def cliente_nome_submit():
	id = request.args.get('id')
	novo = request.form['alt']
	alt = sql.alter_cliente_nome(idCli=id, nome=novo)
	return redirect(url_for('exibir_clientes', id=id, alt=alt))

@app.route('/cliente/alterar/telefone')
def cliente_tel():
	id = request.args.get('id')
	return render_template('alterar.html', name="Tel", action=url_for('cliente_tel_submit', id=id), type="tel", label="Novo Telefone")

@app.route('/cliente/alterar/telefonesubmit', methods=['POST'])
def cliente_tel_submit():
	id = request.args.get('id')
	novo = request.form['alt']
	alt = sql.alter_cliente_tel(idCli=id, tel=novo)
	return redirect(url_for('exibir_clientes', id=id, alt=alt))

@app.route('/cliente/alterar/cpf')
def cliente_cpf():
	id = request.args.get('id')
	return render_template('alterar.html', name="CPF", action=url_for('cliente_cpf_submit', id=id), type="text", label="Novo CPF")

@app.route('/cliente/alterar/cpfsubmit', methods=['POST'])
def cliente_cpf_submit():
	id = request.args.get('id')
	novo = request.form['alt']
	alt = sql.alter_cliente_cpf(idCli=id, cpf=novo)
	return redirect(url_for('exibir_clientes', id=id, alt=alt))
########################
######## Remover #######

@app.route('/cliente/remover', methods=["POST"])
def rm_cliente():
	id = request.args.get('id')
	rm = sql.rm_cliente(idCli=id)
	return redirect(url_for('cliente', rm=rm))

#crud pedidos

######## CADASTRAR

@app.route('/pedido/cadastro')
def cadastro_pedido():
	return render_template('cadastro/cadastro_pedido.html')

@app.route('/cadastro/pedido/submit', methods=['POST'])
def pedido_submit():
	nroMesa = None
	nroMesa = request.form['nroMesa']
	cpfGar = request.form['cpf_garcom']
	idCli = sql.cliente_mesa(nroMesa)
	cadastro = sql.cadastro_pedido(idCli=idCli, cpfGar=cpfGar, nroMesa=nroMesa)
	return redirect(url_for('pedido', cadastro=cadastro))

@app.route('/pedido/search')
def search_pedido():
	return render_template('selecionar_pedido.html')

####### itens Pedido ##########

@app.route('/pedido/itens')
def add_item():
	id = request.args.get('id')
	results = sql.getall_pratos()
	return render_template('cadastro/add_item.html', results=results, id=id)

@app.route('/pedido/itens/submit', methods=['POST'])
def item_submit():
	id = request.args.get('id')
	cardapio = request.form['cardapio']
	qtd = request.form['qtd']
	item = sql.add_item(pedido=id, prato=cardapio, qtd=qtd)
	return redirect(url_for('exibir_pedido', item=item, id=id))

@app.route('/pedido/itens/remove', methods=["POST"])
def rm_item():
	pedido = request.args.get('pedido')
	prato = request.args.get('prato')
	rm = sql.rm_item(pedido=pedido, prato=prato)
	return redirect(url_for('exibir_pedido', rm=rm, id=pedido))


@app.route('/pedido/itens/update', methods=["POST"])
def update_qtd():
	pedido = request.args.get('pedido')
	prato = request.args.get('prato')
	qtd = request.form['qtd']
	alt = sql.update_qtd(pedido=pedido, prato=prato, qtd=qtd)
	return redirect(url_for('exibir_pedido', alt=alt, id=pedido))

######## EXIBIR

@app.route('/pedido/results')
def results_pedido_mesa():
	check = None
	nroMesa = request.args.get('nro_mesa')
	if (request.args.get('check')):
		check = True
	id = sql.cliente_mesa(nroMesa)
	if id:
		results = sql.search_pedido(idCli=id, check=check)
		return render_template('listar_resultados_pedido.html', results=results)
	else:
		return redirect(url_for('pedido', empty=True))

@app.route('/pedido/results')
def results_pedido_algo():
	pass

@app.route('/pedido/exibir')
def exibir_pedido():
	id = request.args.get('id')
	alt = request.args.get('alt')
	cadastro = request.args.get('cadastro')
	item = request.args.get('item')
	rm = request.args.get('rm')
	results = sql.search_pedido(idPed=id)
	itens = sql.get_itens(pedido=id)
	return render_template('exibir_pedido.html', item=item, results=results, alt=alt, cadastro=cadastro, itens_results=itens, rm=rm)

############# ALTERAR ###################

@app.route('/pedido/finalizado')
def finalizar_pedido():
	id = request.args.get('id')
	fim = sql.fim_pedido(id)
	return redirect(url_for('pedido', fim=fim))

@app.route('/pedido/cancelado')
def cancelar_pedido():
	id = request.args.get('id')
	can = sql.canc_pedido(id)
	return redirect(url_for('pedido', can=can))

############# REMOVER ###################

@app.route('/pedido/remove', methods=["POST"])
def rm_pedido():
	id = request.args.get('id')
	rm = sql.rm_pedido(id=id)
	return redirect(url_for('pedido', rm=rm))

#crud funcionarios

@app.route('/funcionario/cadastro')
def cadastro_funcionario():
	return render_template('cadastrar_funcionarios.html')

@app.route('/funcionario/cadastro/cozinheiro')
def cadastro_cozinheiro():
	results = sql.search_cozinheiro_all()
	return render_template('cadastro/cadastro_cozinheiro.html', results=results)

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
	if (sal_funcionario == ''):
		sal_funcionario = 0
	if funcao == 'cozinheiro':
		cpf_chefe = None
		cpf_chefe = request.form['cpfChefe']
		cadastro = sql.cadastro_cozinheiro(nome=nome_funcionario, salario=sal_funcionario, cpf=cpf_funcionario, chefe=cpf_chefe)
	else:
		cadastro = sql.cadastro_garcom(nome=nome_funcionario, salario=sal_funcionario, cpf=cpf_funcionario)
	return redirect(url_for('funcionario', cadastro=cadastro))

########################
####### Exibir #########	


@app.route('/funcionario/search')
def search_funcionario():
	empty = request.args.get('empty')
	return render_template('selecionar_funcionario.html', empty=empty)

@app.route('/funcionario/search/algo')
def results_funcionario_algo():
	condicao = request.args.get('condicao')
	if not condicao:
		return redirect(url_for('search_funcionario'))
	if condicao == 'todos_clientes':
		results = sql.garcons_todos_cliente()
	elif condicao == 'todas_mesas':
		results = sql.garcons_todas_mesas()
	return render_template('listar_resultados_funcionario.html', results=results, funcao='garcom')

@app.route('/funcionario/results')
def results_funcionario_nome():
	nome = request.args.get('nome_funcionario')
	op = request.args.get('options')
	if (op == 'garcom'):
		if nome:
			results = sql.search_garcom(nome=nome)
		else:
			return redirect(url_for('search_funcionario', empty=True))
	else:
		if nome:
			results = sql.search_cozinheiro(nome=nome)
		else:
			return redirect(url_for('search_funcionario', empty=True))
		if (results == ()):
			if nome:
				results = sql.search_cozinheiro_semChefe(nome=nome)
			else:
				return redirect(url_for('search_funcionario', empty=True))

	return render_template('listar_resultados_funcionario.html', results=results, funcao=op)

@app.route('/funcionario/results/exibir')
def exibir_funcionario():
	id = request.args.get('cpf')
	alt = request.args.get('alt')
	funcao = request.args.get('funcao')
	if (funcao == 'garcom'):
		results = sql.search_garcom(cpf=id)
	else:
		results = sql.search_cozinheiro(cpf=id)
		if results == ():
			results = sql.search_cozinheiro_semChefe(cpf=id)
	return render_template('exibir_funcionario.html', results=results, alt=alt, funcao=funcao)

########################
####### Alterar ########

@app.route('/funcionario/alterar/nome/<funcao>')
def nome_funcionario(funcao):
	id = request.args.get('id')
	return render_template('alterar.html', name="Nome", action=url_for('nome_funcionario_submit', id=id, funcao=funcao), type="text", label="Novo Nome")

@app.route('/funcionario/alterar/nome/submit', methods=['POST'])
def nome_funcionario_submit():
	cpf = request.args.get('id')
	funcao = request.args.get('funcao')
	novo = request.form['alt']
	alt = sql.alter_nome_funcionario(cpf=cpf, nome=novo)
	return redirect(url_for('exibir_funcionario', cpf=cpf, alt=alt, funcao=funcao))

@app.route('/funcionario/alterar/salario/<funcao>')
def sal_funcionario(funcao):
	id = request.args.get('id')
	return render_template('alterar.html', name="salario", action=url_for('sal_funcionario_submit', id=id, funcao=funcao), type="number", label="Novo Salario")

@app.route('/funcionario/alterar/salario/submit', methods=['POST'])
def sal_funcionario_submit():
	cpf = request.args.get('id')
	funcao = request.args.get('funcao')
	novo = request.form['alt']
	alt = sql.alter_sal_funcionario(cpf=cpf, salario=novo)
	return redirect(url_for('exibir_funcionario', cpf=cpf, alt=alt, funcao=funcao))

@app.route('/funcionario/alterar/chefe/')
def chefe_funcionario():
	id = request.args.get('id')
	results = sql.search_cozinheiro_all()
	return render_template('alterarChefe.html', id=id, results=results)

@app.route('/funcionario/alterar/chefe/submit', methods=['POST'])
def chefe_funcionario_submit():
	cpf = request.args.get('id')
	novo = request.form['alt']
	alt = sql.alter_chefe_funcionario(cpf=cpf, chefe=novo)
	return redirect(url_for('exibir_funcionario', cpf=cpf, alt=alt, funcao='cozinheiro'))

########################
######## Remover #######

@app.route('/funcionario/remove', methods=["POST"])
def rm_funcionario():
	id = request.args.get('id')
	funcao = request.args.get('funcao')
	if (funcao == 'garcom'):
		rm = sql.rm_garcom(cpf=id)
	else:
		rm = sql.rm_cozinheiro(cpf=id)
	return redirect(url_for('funcionario', rm=rm))

# crud pratos	

####### Cadastrar #######

@app.route('/restaurante/cardapio/prato/cadastro')
def cadastro_prato():
	return render_template('cadastro/cadastro_prato.html')	

@app.route('/restaurante/cardapio/prato/cadastro/submit', methods=['POST'])
def prato_submit():
	nome = None
	nome = request.form['nome_prato']
	preco = request.form['c1']
	cadastro = sql.cadastro_prato(nome=nome, preco=preco)
	return redirect(url_for('cardapio', cadastro=cadastro))

########################
####### Exibir #########

@app.route('/restaurante/prato/search')
def search_prato():
	clientes = sql.getall_clientes()
	return render_template('selecionar_prato.html', clientes=clientes)

@app.route('/prato/results')
def results_prato_nome():
	nome = request.args.get('nome_prato')
	if not nome:
		results = sql.getall_pratos()
	else:
		results = sql.search_prato(nome=nome)
	return render_template('listar_resultados_prato.html', results=results)

@app.route('/prato/results/maisvendido')
def results_prato_mes():
	mes = request.args.get('mes')
	if mes:
		results = sql.prato_do_mes(mes=mes)
	else:
		results = ()
	return render_template('listar_resultados_prato.html', results=results)


@app.route('/prato/results/cliente')
def results_prato_cliente():
	cliente = request.args.get('cliente')
	results = sql.prato_mais_pedido_cliente(id = cliente)
	return render_template('listar_resultados_prato.html', results=results)

@app.route('/prato')
def exibir_prato():
	id = request.args.get('id')
	alt = request.args.get('alt')
	results = sql.search_prato(id=id)
	return render_template('exibir_prato.html', results=results, alt=alt)

########################
####### Alterar ########

@app.route('/prato/alterar/nome')
def prato_nome():
	id = request.args.get('id')
	return render_template('alterar.html', name="Nome", action=url_for('prato_nome_submit', id=id), type="text", label="Novo Nome")

@app.route('/prato/alterar/submit', methods=['POST'])
def prato_nome_submit():
	id = request.args.get('id')
	novo = request.form['alt']
	alt = sql.alter_prato_nome(id=id, nome=novo)
	return redirect(url_for('exibir_prato', alt=alt, id=id))

@app.route('/prato/alterar/preco')
def prato_preco():
	id = request.args.get('id')
	return render_template('alterar.html', name="Nome", action=url_for('prato_preco_submit', id=id), type="number", label="Novo Preco")

@app.route('/prato/alterar/preco/submit', methods=['POST'])
def prato_preco_submit():
	id = request.args.get('id')
	novo = request.form['alt']
	alt = sql.alter_prato_preco(id=id, preco=novo)
	return redirect(url_for('exibir_prato', alt=alt, id=id))

########################
######## Remover #######

@app.route('/prato/remove', methods=["POST"])
def rm_prato():
	id = request.args.get('id')
	rm = sql.rm_prato(id=id)
	return redirect(url_for('cardapio', rm=rm))

# crud mesa

####### Cadastrar #######

@app.route('/mesa/cadastro')
def cadastro_mesa():
	return render_template('cadastro/cadastro_mesa.html')	

@app.route('/cadastro/mesa/submit', methods=['POST'])
def mesa_submit():
	numero_da_mesa = None
	numero_de_pessoas = None
	numero_da_mesa = request.form['numero_da_mesa']
	numero_de_pessoas = request.form['numero_de_pessoas']
	cadastro = sql.cadastro_mesa(numero_de_pessoas=numero_de_pessoas, numero_da_mesa=numero_da_mesa)
	return redirect(url_for('mesa', cadastro=cadastro))

########################
####### Exibir #########

@app.route('/restaurante/mesa/search')
def search_mesa():
	return render_template('selecionar_mesa.html')

@app.route('/restaurante/mesa/results')
def results_numero_da_mesa():
	numero = request.args.get('numero_da_mesa')
	if not numero:
		results = sql.getall_mesas()
		return render_template('listar_resultados_mesa.html', results=results)
	# else:
	# 	results = sql.search_mesa(numero_da_mesa=numero)
	return redirect(url_for('exibir_mesa', numero_da_mesa=numero))


@app.route('/mesa/')
def exibir_mesa():
	numero_da_mesa = request.args.get('numero_da_mesa')
	results = sql.search_mesa(numero_da_mesa=numero_da_mesa)
	alt = request.args.get('alt')
	return render_template('exibir_mesa.html', results=results, alt=alt)

########################
####### Alterar ########

@app.route('/mesa/alterar/')
def numero_da_mesa():
	id = request.args.get('id')
	return render_template('alterar.html', name="Numero da mesa", action=url_for('numero_da_mesa_submit', id=id), type="num", label="Novo Numero da Mesa")

@app.route('/mesa/alterar/submit', methods=['POST'])
def numero_da_mesa_submit():
	id = request.args.get('id')	
	novo = request.form['alt']
	alt = sql.alter_numero_da_mesa(numero_da_mesa=id, novo_numero=novo)
	return redirect(url_for('exibir_mesa', numero_da_mesa=novo, alt=alt))

@app.route('/mesa/alterar/')
def numero_de_pessoas():
	id = request.args.get('id')
	return render_template('alterar.html', name="Numero de Pessoas", action=url_for('numero_de_pessoas_submit', id=id), type="num", label="Novo Numero de Pessoas")

@app.route('/mesa/alterar/submit', methods=['POST'])
def numero_de_pessoas_submit():
	id = request.args.get('id')
	novo = request.form['alt']
	alt = sql.alter_numero_de_pessoas(numero_da_mesa=id, numero_de_pessoas=novo)
	return redirect(url_for('exibir_mesa', numero_da_mesa=id, alt=alt))

########################
######## Remover #######

@app.route('/mesa/<nroMesa>/remove', methods=["POST"])
def rm_mesa(nroMesa):
	rm = sql.rm_mesa(numero_da_mesa=nroMesa)
	return redirect(url_for('mesa', rm=rm))


# crud Reservas

####### Cadastrar #######

@app.route('/reserva/cadastro')
def cadastro_reserva():
	id = request.args.get('id')
	return render_template('cadastro/cadastro_reservas.html', id=id)	

@app.route('/reserva/cadastro/submit/<id>')
def reserva_submit(id):
	nroPessoas = None
	nroMesa = None
	data = None
	hora = None
	# id = None
	# id = request.args.get('id')
	nroMesa = request.args.get('numero_da_mesa')
	nroPessoas = request.args.get('numero_de_pessoas')
	hora = request.args.get('hora_reserva')
	data = request.args.get('data_reserva')
	reserva = sql.cadastro_reserva(idCli=id, nroMesa=nroMesa, datas=data, hora=hora, nroPessoas=nroPessoas)
	return redirect(url_for('exibir_clientes', id=id, reserva=reserva))

@app.route('/selecionar/mesa_livre/<id>')
def mesa_reserva(id):
	nroPessoas = None
	data = None
	hora = None
	nroPessoas = request.args.get('numero_de_pessoas')
	hora = request.args.get('hora_reserva')
	data = request.args.get('data_reserva')
	if(data and nroPessoas):
		results = sql.mesa_livre(data, nroPessoas)
	else:
		return redirect(url_for('exibir_clientes', id=id, empty=True))
	return render_template('listar_resultados_mesaLivres.html', results=results, nroPessoas=nroPessoas, hora=hora, data=data, id=id)

 ########################
 ####### Exibir #########

@app.route('/restaurante/reserva/search')
def search_reserva():
	return render_template('selecionar_reserva.html')

@app.route('/restaurante/reserva/results')
def results_data_reserva():
	data = request.args.get('data_reserva')
	results = sql.search_reserva(data=data)
	return render_template('listar_resultados_reserva.html', results=results)


@app.route('/reserva/exibir')
def exibir_reserva():
	id = request.args.get('id')
	results = sql.search_reserva(id=id)
	cliente = sql.search_cliente(idCli = (results[0])[1])
	alt = request.args.get('alt')
	return render_template('exibir_reserva.html', results=results, alt=alt, cliente=(cliente[0])[1])

########################
####### Alterar ########

@app.route('/selecionar/mesa_livre/<id>/alterar')
def alt_mesa_reserva(id):
	date = request.args.get('date')
	nroPessoas = request.args.get('nroPessoas')
	results = sql.mesa_livre(date=date, nroPessoas=nroPessoas)
	return render_template('listar_resultados_mesaAlt.html', results=results, id=id)

@app.route('/selecionar/mesa_livre/alterar/submit')
def alt_mesa_reserva_submit():
	id = request.args.get('id')
	nro = request.args.get('nroMesa')
	alt = sql.alter_reserva_nroMesa(id=id, nro = nro)
	return redirect(url_for('exibir_reserva', id=id, alt=alt))

@app.route('/reserva/nropessoas/alterar')
def alt_nroPessoas_reservas():
	id = request.args.get('id')
	return render_template('alterar.html', name="Numero de Pessoas", action=url_for('alt_nroPessoas_reservas_submit', id=id), type="number", label="Novo Numero de Pessoas")

@app.route('/reserva/nropessoas/alterar/submit', methods=['POST'])
def alt_nroPessoas_reservas_submit():
	id = request.args.get('id')
	novo = request.form['alt']
	alt = sql.alter_reserva_nroPessoas(id=id, nroPessoas=novo)
	return redirect(url_for('exibir_reserva', id=id, alt=alt))

@app.route('/reserva/datas/alterar')
def alt_datas_reservas():
	id = request.args.get('id')
	return render_template('alterar.html', name="Data", action=url_for('alt_datas_reservas_submit', id=id), type="date", label="Nova Data")

@app.route('/reserva/datas/alterar/submit', methods=['POST'])
def alt_datas_reservas_submit():
	id = request.args.get('id')
	novo = request.form['alt']
	alt = sql.alter_reserva_datas(id=id, datas=novo)
	return redirect(url_for('exibir_reserva', id=id, alt=alt))

@app.route('/reserva/horas/alterar')
def alt_hora_reservas():
	id = request.args.get('id')
	return render_template('alterar.html', name="Hora", action=url_for('alt_hora_reservas_submit', id=id), type="time", label="Nova Hora")

@app.route('/reserva/horas/alterar/submit', methods=['POST'])
def alt_hora_reservas_submit():
	id = request.args.get('id')
	novo = request.form['alt']
	alt = sql.alter_hora_reserva(id=id, hora=novo)
	return redirect(url_for('exibir_reserva', id=id, alt=alt))


 ########################
 ######## Remover #######

@app.route('/reserva/remove', methods=["POST"])
def rm_reserva():
	id = request.args.get('id')
	rm = sql.rm_reserva(id=id)
	return redirect(url_for('mesa', rm=rm))

 #######################
 ####### Ingredientes ##

@app.route('/restaurante/ingredientes/search')
def search_ingrediente():
	return render_template('selecionar_ingrediente.html')

@app.route('/restaurante/ingredientes/results/algo')
def results_ingrediente_algo():
	condicao = request.args.get('condicao')
	if not condicao:
		return redirect(url_for('search_ingrediente'))
	if condicao == 'sem_fornecedor':
		results = sql.ingredientes_que_nao_fornecedor()
	else:
		results = ()
	return render_template('listar_resultados_ingredientes.html', results=results)

if __name__ == '__main__':
	app.run(debug=True)