import pymysql

class bdHelper():
	"""docstring for bdHelper"""
	def __init__(self):
		pass

	def connect(self, database="restaurante_bd"):
		return pymysql.connect(host="localhost", user="root", passwd="root", db=database)

	def get_all_inputs(self):
		connection = self.connect()
		try:
			query = "select * from clientes;"
			with connection.cursor() as cursor:
				cursor.execute(query)
				return cursor.fetchall()
		finally:
			connection.close()

if __name__ == '__main__':
	teste = bdHelper()
	data = teste.get_all_inputs()
	print(data)
