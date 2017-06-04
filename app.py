from flask import Flask
from flask import render_template, url_for

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


if __name__ == '__main__':
	app.run(debug=True)