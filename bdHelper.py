import pymysql

class bdHelper():
	"""docstring for bdHelper"""
	def __init__(self):
		pass

	def connect(self, database="restaurante_bd"):
		return pymysql.connect(host="localhost", user="root", passwd="root", db=database)

	def cadastro_cliente(self, idCli=None, nome=None, telefone=None, cpf=None):
		connection = self.connect()
		try:
			query = "insert into clientes(idCli, nome, telefone, cpf) values(%s, %s, %s, %s);"
			
			with connection.cursor() as cursor:
				cursor.execute(query, (idCli, nome, telefone, cpf))
				connection.commit()
		except Exception as e:
			print(e)
		finally:
			connection.close()

	def cadastro_pedido(self, nroMesa):
		connection = self.connect()
		try:
			query = "insert into pedidos"


	
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
	teste.cadastro_cliente("7", "David Tennant", "183", "12334")
	# print(data)
