import pymysql
import bdconfig

class bdHelper():
	# """docstring for bdHelper"""
	# def __init__(self):
	# 	pass

	def connect(self, database="restaurante_bd"):
		return pymysql.connect(host="localhost", user=bdconfig.user, passwd=bdconfig.passwd, db=database)

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

if __name__ == '__main__':
	teste = bdHelper()
	# teste.cadastro_cliente("7", "David Tennant", "183", "12334")
	# print(data)
