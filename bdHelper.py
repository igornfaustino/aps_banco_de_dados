import pymysql
import bdconfig

class bdHelper():
	# """docstring for bdHelper"""
	# def __init__(self):
	# 	pass

	def connect(self, database="restaurante_bd"):
		return pymysql.connect(host="localhost", user=bdconfig.user, passwd=bdconfig.passwrd, db=database)

	# crud cliente

	def cadastro_cliente(self, nome=None, telefone=None, cpf=None):
		connection = self.connect()
		try:
			query = "insert into clientes(nome, telefone, cpf) values(%s, %s, %s);"
			
			with connection.cursor() as cursor:
				cursor.execute(query, (nome, telefone, cpf))
				connection.commit()
				return True
		except Exception as e:
			print(e)
			return False
		finally:
			connection.close()

	def search_cliente(self, idCli=None, nome=None):
		connection = self.connect()
		try:
			with connection.cursor() as cursor:
				if(idCli):
					query = "select * from clientes where idCli = %s;"
					cursor.execute(query, idCli)
				elif(nome):
					query = "select * from clientes where nome like %s;"
					cursor.execute(query, ("%" + nome + "%"))
				return cursor.fetchall()
		except Exception as e:
			print(e)
		finally:
			connection.close()

	def getall_clientes(self):
		connection = self.connect()
		try:
			with connection.cursor() as cursor:
				query = "select * from clientes"
				cursor.execute(query)
				return cursor.fetchall()
		except Exception as e:
			print(e)
		finally:
			connection.close()

	def rm_cliente(self, idCli=None):
		connection = self.connect()
		try:
			query = "delete from clientes where idCli = %s;"
			with connection.cursor() as cursor:
				cursor.execute(query, idCli)
				connection.commit()
				return True
		except Exception as e:
			return False
		finally:
			connection.close()

	def alter_cliente_nome(self, idCli=None, nome = None):
		connection = self.connect()
		try:
			query = "update clientes set nome = %s where idCli = %s;"
			with connection.cursor() as cursor:
				cursor.execute(query, (nome, idCli))
				connection.commit()
				return True
		except Exception as e:
			print(e)
			return False
		finally:
			connection.close()

	def alter_cliente_tel(self, idCli=None, tel = None):
		connection = self.connect()
		try:
			query = "update clientes set telefone = %s where idCli = %s;"
			with connection.cursor() as cursor:
				cursor.execute(query, (tel, idCli))
				connection.commit()
				return True
		except Exception as e:
			print(e)
			return False
		finally:
			connection.close()

	def alter_cliente_cpf(self, idCli=None, cpf = None):
		connection = self.connect()
		try:
			query = "update clientes set cpf = %s where idCli = %s;"
			with connection.cursor() as cursor:
				cursor.execute(query, (cpf, idCli))
				connection.commit()
				return True
		except Exception as e:
			print(e)
			return False
		finally:
			connection.close()

	# crud pedido

	def cadastro_pedido(self, idCli, cpfGar):
		connection = self.connect()
		try:
			query = "insert into pedidos(situacao, idCli, cpfGar, dataPed) values(%s, %s, %s, CURDATE());"
			with connection.cursor() as cursor:
				cursor.execute(query, ("Pedido Pendente", idCli, cpfGar))
				connection.commit()
				return True
		except Exception as e:
			print(e)
			return False
		finally:
			connection.close()

	def search_pedido(self, idCli=None, check=False, idPed=None):
		connection = self.connect()
		try:
			with connection.cursor() as cursor:
				query1 = "select * from pedidos where idCli = %s and dataPed=CURDATE();"
				query2 = "select * from pedidos where idCli = %s and situacao <> 'Finalizado' and situacao <> 'Cancelado' and dataPed=CURDATE();"
				query3 = "select * from pedidos where idPed = %s;"
				if check:
					cursor.execute(query1, idCli)
				else:
					if(idPed):
						cursor.execute(query3, idPed)
					else:
						cursor.execute(query2, idCli)
				return cursor.fetchall()
		except Exception as e:
			print(e)
		finally:
			connection.close()

	def fim_pedido(self, idPed=None):
		connection = self.connect()
		try:
			query = "update pedidos set situacao = 'Finalizado' where idPed = %s;"
			with connection.cursor() as cursor:
				cursor.execute(query, (idPed))
				connection.commit()
				return True
		except Exception as e:
			print(e)
			return False
		finally:
			connection.close()

	def canc_pedido(self, idPed=None):
		connection = self.connect()
		try:
			query = "update pedidos set situacao = 'Cancelado' where idPed = %s;"
			with connection.cursor() as cursor:
				cursor.execute(query, (idPed))
				connection.commit()
				return True
		except Exception as e:
			print(e)
			return False
		finally:
			connection.close()

	def rm_pedido(self, id=None):
		connection = self.connect()
		try:
			query = "delete from pedidos where idPed = %s;"
			with connection.cursor() as cursor:
				cursor.execute(query, id)
				connection.commit()
				return True
		except Exception as e:
			print(e)
			return False
		finally:
			connection.close()



	# crud mesa

	def cadastro_mesa(self, numero_de_pessoas=None, numero_da_mesa=None):
		connection = self.connect()
		try:
			query = "insert into mesas(nroPessoas, nroMesa) values(%s, %s);"
			
			with connection.cursor() as cursor:
				cursor.execute(query, (int(numero_de_pessoas), int(numero_da_mesa)))
				connection.commit()
				return True
		except Exception as e:
			print(e)
			return False
		finally:
			connection.close()

	def search_mesa(self, numero_da_mesa=None):
		connection = self.connect()
		try:
			with connection.cursor() as cursor:
				query = "select * from mesas where nroMesa = %s;"
				cursor.execute(query, int(numero_da_mesa))
				return cursor.fetchall()
		except Exception as e:
			print(e)
		finally:
			connection.close()

	def getall_mesas(self, numero_da_mesa=None):
		connection = self.connect()
		try:
			with connection.cursor() as cursor:
				query = "select * from mesas;"
				cursor.execute(query)
				return cursor.fetchall()
		except Exception as e:
			print(e)
		finally:
			connection.close()

	def rm_mesa(self, numero_da_mesa=None):
		connection = self.connect()
		try:
			query = "delete from mesas where nroMesa = %s;"
			with connection.cursor() as cursor:
				cursor.execute(query, numero_da_mesa)
				connection.commit()
				return True
		except Exception as e:
			print(e)
			return False
		finally:
			connection.close()

	def alter_numero_de_pessoas(self, numero_da_mesa=None, numero_de_pessoas = None):
		connection = self.connect()
		try:
			query = "update mesas set nroPessoas = %s where nroMesa = %s;"
			with connection.cursor() as cursor:
				cursor.execute(query, (int(numero_de_pessoas), int(numero_da_mesa)))
				connection.commit()
				return True
		except Exception as e:
			print(e)
			return False
		finally:
			connection.close()

	def alter_numero_da_mesa(self, numero_da_mesa=None, novo_numero = None):
		connection = self.connect()
		try:
			query = "update mesas set nroMesa = %s where nroMesa = %s;"
			with connection.cursor() as cursor:
				cursor.execute(query, (int(novo_numero), int(numero_da_mesa)))
				connection.commit()
				return True
		except Exception as e:
			print(e)
			return False
		finally:
			connection.close()

	

 #crud funcionario
	
	def cadastro_garcom(self, cpf=None, salario=0, nome=None):
		connection = self.connect()
		try:
			query1 = "insert into funcionarios(cpf, salario, situacao, nome) values(%s, %s, 'Ativo', %s);"
			query2 = "insert into garcons(cpf) values (%s)"
			with connection.cursor() as cursor:
				cursor.execute(query1, (cpf, float(salario), nome))
				cursor.execute(query2, (cpf))
				connection.commit()
				return True
		except Exception as e:
			print(e)
			return False
		finally:
			connection.close()

	def cadastro_cozinheiro(self, cpf=None, salario=0, nome=None, chefe=None):
		connection = self.connect()
		try:
			query1 = "insert into funcionarios(cpf, salario, situacao, nome) values(%s, %s, 'Ativo', %s);"
			if chefe:
				query2 = "insert into cozinheiros(cpf, cpfChefe) values (%s, %s)"
			else:
				query2 = "insert into cozinheiros(cpf) values (%s)"
			with connection.cursor() as cursor:
				cursor.execute(query1, (cpf, float(salario), nome))
				if chefe:
					cursor.execute(query2, (cpf, chefe))
				else:	
					cursor.execute(query2, (cpf))
				connection.commit()
				return True
		except Exception as e:
			print(e)
			return False
		finally:
			connection.close()

	def search_garcom(self, nome=None, cpf=None):
		connection = self.connect()
		try:
			with connection.cursor() as cursor:
				query1 = "select F.cpf, F.salario, F.situacao, F.nome from funcionarios F, garcons G where nome like %s and G.cpf = F.cpf;"
				query2 = "select * from funcionarios where cpf = %s;"
				if cpf:
					cursor.execute(query2, (cpf))
				else:
					cursor.execute(query1, ("%" + nome + "%"))
				return cursor.fetchall()
		except Exception as e:
			print(e)
		finally:
			connection.close()

	def search_cozinheiro(self, nome=None, cpf=None):
		connection = self.connect()
		try:
			with connection.cursor() as cursor:
				query1 = """select 	F1.cpf, F1.salario, F1.situacao, F1.nome, F2.nome 
							from 	funcionarios F1, cozinheiros C1, funcionarios F2
							where 	F1.nome like %s and
									C1.cpf = F1.cpf and 
									C1.cpfChefe = F2.cpf;"""
				query2 = """select 	F1.cpf, F1.salario, F1.situacao, F1.nome, F2.nome 
							from 	funcionarios F1, cozinheiros C1, funcionarios F2
							where 	F1.cpf = %s and
									C1.cpf = F1.cpf and 
									C1.cpfChefe = F2.cpf;"""
				if cpf:
					cursor.execute(query2, (cpf))
				else:
					cursor.execute(query1, ("%" + nome + "%"))
				return cursor.fetchall()
		except Exception as e:
			print(e)
		finally:
			connection.close()

	def search_cozinheiro_semChefe(self, nome=None, cpf=None):
		connection = self.connect()
		try:
			with connection.cursor() as cursor:
				query1 = """select 	F1.cpf, F1.salario, F1.situacao, F1.nome
							from 	funcionarios F1, cozinheiros C1
							where 	F1.nome like %s and
									C1.cpf = F1.cpf;"""
				query2 = """select 	F1.cpf, F1.salario, F1.situacao, F1.nome 
							from 	funcionarios F1, cozinheiros C1
							where 	F1.cpf = %s and
									C1.cpf = F1.cpf;"""
				if cpf:
					cursor.execute(query2, (cpf))
				else:
					cursor.execute(query1, ("%" + nome + "%"))
				return cursor.fetchall()
		except Exception as e:
			print(e)
		finally:
			connection.close()

	def search_cozinheiro_all(self):
		connection = self.connect()
		try:
			with connection.cursor() as cursor:
				query1 = """select 	F1.cpf, F1.salario, F1.situacao, F1.nome
							from 	funcionarios F1, cozinheiros C1
							where 	C1.cpf = F1.cpf;"""
				cursor.execute(query1)
				return cursor.fetchall()
		except Exception as e:
			print(e)
		finally:
			connection.close()

	def getall_funcionario(self):
		connection = self.connect()
		try:
			with connection.cursor() as cursor:
				query = "select * from funcionarios"
				cursor.execute(query)
				return cursor.fetchall()
		except Exception as e:
			print(e)
		finally:
			connection.close()

	def rm_garcom(self, cpf=None):
		connection = self.connect()
		try:
			query1 = "delete from garcons where cpf = %s;"
			query2 = "delete from funcionarios where cpf = %s;"
			with connection.cursor() as cursor:
				cursor.execute(query1, cpf)
				cursor.execute(query2, cpf)
				connection.commit()
				return True
		except Exception as e:
			print(e)
			return False
		finally:
			connection.close()

	def rm_cozinheiro(self, cpf=None):
		connection = self.connect()
		try:
			query1 = "delete from cozinheiros where cpf = %s;"
			query2 = "delete from funcionarios where cpf = %s;"
			with connection.cursor() as cursor:
				cursor.execute(query1, cpf)
				cursor.execute(query2, cpf)
				connection.commit()
				return True
		except Exception as e:
			print(e)
			return False
		finally:
			connection.close()

	def alter_nome_funcionario(self, cpf=None, nome = None):
		connection = self.connect()
		try:
			query = "update funcionarios set nome = %s where cpf = %s;"
			with connection.cursor() as cursor:
				cursor.execute(query, (nome, cpf))
				connection.commit()
				return True
		except Exception as e:
			print(e)
			return False
		finally:
			connection.close()

	def alter_sal_funcionario(self, cpf=None, salario = None):
		connection = self.connect()
		try:
			query = "update funcionarios set salario = %s where cpf = %s;"
			with connection.cursor() as cursor:
				cursor.execute(query, (salario, cpf))
				connection.commit()
				return True
		except Exception as e:
			print(e)
			return False
		finally:
			connection.close()

	def alter_chefe_funcionario(self, cpf=None, chefe = None):
		connection = self.connect()
		try:
			query = "update cozinheiros set cpfChefe = %s where cpf = %s;"
			with connection.cursor() as cursor:
				cursor.execute(query, (chefe, cpf))
				connection.commit()
				return True
		except Exception as e:
			print(e)
			return False
		finally:
			connection.close()


	# crud pratos

	def cadastro_prato(self, nome=None):
		connection = self.connect()
		try:
			query = "insert into pratos(nome) values(%s);"
			
			with connection.cursor() as cursor:
				cursor.execute(query, nome)
				connection.commit()
				return True
		except Exception as e:
			print(e)
			return False
		finally:
			connection.close()

	def search_prato(self, id=None, nome=None):
		connection = self.connect()
		try:
			with connection.cursor() as cursor:
				if(id):
					query = "select * from pratos where id = %s;"
					cursor.execute(query, id)
				elif(nome):
					query = "select * from pratos where nome like %s;"
					cursor.execute(query, ("%" + nome + "%"))
				return cursor.fetchall()
		except Exception as e:
			print(e)
		finally:
			connection.close()

	def getall_pratos(self):
		connection = self.connect()
		try:
			with connection.cursor() as cursor:
				query = "select * from pratos;"
				cursor.execute(query)
				return cursor.fetchall()
		except Exception as e:
			print(e)
		finally:
			connection.close()


	def rm_prato(self, id=None):
		connection = self.connect()
		try:
			query = "delete from pratos where id = %s;"
			with connection.cursor() as cursor:
				cursor.execute(query, id)
				connection.commit()
				return True
		except Exception as e:
			print(e)
			return False
		finally:
			connection.close()

	def alter_prato_nome(self, id=None, nome = None):
		connection = self.connect()
		try:
			query = "update pratos set nome = %s where id = %s;"
			with connection.cursor() as cursor:
				cursor.execute(query, (nome, id))
				connection.commit()
				return True
		except Exception as e:
			print(e)
			return False
		finally:
			connection.close()

	# crud reserva


	def cadastro_reserva(self, idCli=None, nroMesa=None, datas=None
		, hora=None, nroPessoas=None):
		connection = self.connect()
		try:
			query = "insert into reservas(idCli, nroMesa, datas, hora, nroPessoas) values(%s, %s, %s, %s, %s);"
			
			with connection.cursor() as cursor:
				cursor.execute(query, (idCli, nroMesa, datas, hora, nroPessoas))
				connection.commit()
				return True
		except Exception as e:
			print(e)
			return False
		finally:
			connection.close()

	def search_reserva(self, id=None, data=None):
		connection = self.connect()
		try:
			with connection.cursor() as cursor:
	 			if(id):
	 				query = "select * from reservas where idReser = %s;"
	 				cursor.execute(query, id)
	 			else:
	 				query = "select * from reservas where datas = %s;"
	 				cursor.execute(query, (data))
	 			return cursor.fetchall()
		except Exception as e:
	 		print(e)
		finally:
	 		connection.close()

	def getall_reserva(self):
		connection = self.connect()
		try:
			with connection.cursor() as cursor:
				query = "select * from reservas;"
				cursor.execute(query)
				return cursor.fetchall()
		except Exception as e:
			print(e)
		finally:
			connection.close()


	def rm_reserva(self, id=None):
		connection = self.connect()
		try:
			query = "delete from reservas where idReser = %s;"
			with connection.cursor() as cursor:
				cursor.execute(query, id)
				connection.commit()
				return True
		except Exception as e:
			print(e)
			return False
		finally:
			connection.close()

	def alter_reserva_nroMesa(self, id=None, nro = None):
		connection = self.connect()
		try:
			query = "update reservas set nroMesa = %s where idReser = %s;"
			with connection.cursor() as cursor:
				cursor.execute(query, (nro, id))
				connection.commit()
				return True
		except Exception as e:
			print(e)
			return False
		finally:
			connection.close()

	def alter_reserva_datas(self, id=None, datas = None):
		connection = self.connect()
		try:
			query = "update reservas set datas = %s where idReser = %s;"
			with connection.cursor() as cursor:
				cursor.execute(query, (datas, id))
				connection.commit()
				return True
		except Exception as e:
			print(e)
			return False
		finally:
			connection.close()

	def alter_hora_reserva(self, id=None, hora = None):
		connection = self.connect()
		try:
			query = "update reservas set hora = %s where idReser = %s;"
			with connection.cursor() as cursor:
				cursor.execute(query, (hora, id))
				connection.commit()
				return True
		except Exception as e:
			print(e)
			return False
		finally:
			connection.close()

	def alter_reserva_nroPessoas(self, id=None, nroPessoas = None):
		connection = self.connect()
		try:
			query = "update reservas set nroPessoas = %s where idReser = %s;"
			with connection.cursor() as cursor:
				cursor.execute(query, (nroPessoas, id))
				connection.commit()
				return True
		except Exception as e:
			print(e)
			return False
		finally:
			connection.close()

	# pesquisar cliente sentado em uma mesa
	def cliente_mesa(self, nroMesa=None):
		connection = self.connect()
		try:
			with connection.cursor() as cursor:
				query = """	select R.idCli
							from reservas R
							where R.nroMesa = %s and R.datas = curdate();
						"""
				cursor.execute(query, nroMesa)
				return cursor.fetchall()
		except Exception as e:
			print(e)
		finally:
			connection.close()

	# Pesquisar mesas livres para determinada data
	def mesa_livre(self, date='curdate()', nroPessoas='0'):
		connection = self.connect()
		try:
			with connection.cursor() as cursor:
				query = """	select M.*
							from mesas M
							where M.nroPessoas >= %s and M.nroMesa not in (	select R.nroMesa
														from reservas R
														where datas = %s
													);
						"""
				cursor.execute(query, (int(nroPessoas), date))
				return cursor.fetchall()
		except Exception as e:
			print(e)
		finally:
			connection.close()


if __name__ == '__main__':
	teste = bdHelper()
	# teste.cadastro_cliente("7", "David Tennant", "183", "12334")
	# print(data)
