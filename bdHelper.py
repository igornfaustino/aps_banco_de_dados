import pymysql

class bdHelper():
	# """docstring for bdHelper"""
	# def __init__(self):
	# 	pass

	def connect(self, database="restaurante_bd"):
		return pymysql.connect(host="localhost", user="root", passwd="root", db=database)

	# crud cliente

	def cadastro_cliente(self, nome=None, telefone=None, cpf=None):
		connection = self.connect()
		try:
			query = "insert into clientes(nome, telefone, cpf) values(%s, %s, %s);"
			
			with connection.cursor() as cursor:
				cursor.execute(query, (nome, telefone, cpf))
				connection.commit()
		except Exception as e:
			print(e)
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

	def rm_cliente(self, idCli=None):
		connection = self.connect()
		try:
			query = "delete from clientes where idCli = %s;"
			with connection.cursor() as cursor:
				cursor.execute(query, idCli)
				connection.commit()
		except Exception as e:
			print(e)
		finally:
			connection.close()

	def alter_cliente_nome(self, idCli=None, nome = None):
		connection = self.connect()
		try:
			query = "update clientes set nome = %s where idCli = %s;"
			with connection.cursor() as cursor:
				cursor.execute(query, (nome, idCli))
				connection.commit()
		except Exception as e:
			print(e)
		finally:
			connection.close()

	def alter_cliente_tel(self, idCli=None, tel = None):
		connection = self.connect()
		try:
			query = "update clientes set nome = %s where idCli = %s;"
			with connection.cursor() as cursor:
				cursor.execute(query, (tel, idCli))
				connection.commit()
		except Exception as e:
			print(e)
		finally:
			connection.close()

	def alter_cliente_cpf(self, idCli=None, cpf = None):
		connection = self.connect()
		try:
			query = "update clientes set nome = %s where idCli = %s;"
			with connection.cursor() as cursor:
				cursor.execute(query, (cpf, idCli))
				connection.commit()
		except Exception as e:
			print(e)
		finally:
			connection.close()

	# def cadastro_pedido(self, nroMesa):
	# 	connection = self.connect()
	# 	try:
	# 		query = "insert into pedidos(inPed, situacao, idCli, cpfGar, dataPed) values(%s, %s, %s, %s, NULL);"
	# 		with connection.cursor() as cursor:
	# 			cursor.execute(query, ("Pedido Pendente", idCli, "NULL", "curdate()"))
	# 	except Exception as e:
	# 		print(e)
	# 	finally:
	# 		connection.close()


	
	def cadastro_garcom(self, nome, sal, cpf):
		connection = self.connect()
		try:
			query = "insert into funcionario(cpf, salario, situacao, nome) values (%s, %s, %s, %s)"
			query1 = "insert into garcom(cpf) values (%s)"
			with connection.cursor as cursor:
				cursor.execute(query, (cpf, sal, "Ativo", nome))
				cursor.execute(query1, (cpf))
				connection.commit()
		except Exception as e:
			print(e)
		finally:
			connection.close()

	def cadastro_cozinheiro(self, nome, sal, cpf, chefe):
		connection = self.connect()
		try:
			query = "insert into funcionario(cpf, salario, situacao, nome) values (%s, %s, %s, %s)"
			query1 = "insert into cozinheiros(cpf, cpfChefe) values (%s, %s)"
			with connection.cursor as cursor:
				cursor.execute(query, (cpf, sal, "Ativo", nome))
				cursor.execute(query1, (cpf, chefe))
				connection.commit()
		except Exception as e:
			print(e)
		finally:
			connection.close()


if __name__ == '__main__':
	teste = bdHelper()
	# teste.cadastro_cliente("7", "David Tennant", "183", "12334")
	# print(data)
