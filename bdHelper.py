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

	

if __name__ == '__main__':
	teste = bdHelper()
	teste.cadastro_cliente("7", "David Tennant", "183", "12334")
	# print(data)
