from flask import *
from simplex import *
import json
app = Flask(__name__)

@app.route("/simplex")
def index():
    return "hello"


@app.route('/simplex/maximizar', methods=['POST'])
def SimplexMax():
    if request.method == 'POST':
        data = request.get_json()
        qtd_var = data['qtd_var']
        qtd_regras = data['qtd_regras']
        funcao = data['funcao']
        regras = data['regras']
        resposta = maximizar(qtd_var, qtd_regras, funcao, regras)
        aux = str(resposta)
        #print(aux)
        return jsonify({"data": aux})
    return jsonify("error")
@app.route('/simplex/minimizar', methods=['POST'])
def SimplexMin():
    if request.method == 'POST':
        data = request.get_json()
        qtd_var = data['qtd_var']
        qtd_regras = data['qtd_regras']
        funcao = data['funcao']
        regras = data['regras']
        aux = [qtd_var, qtd_regras, funcao, regras]
        resposta = minimizar(qtd_var, qtd_regras, funcao, regras)
        aux = str(resposta)
        #print(aux)
        return jsonify({"data": aux})
    return jsonify("error")

if __name__ == "__main__":

	app.run()

# consultar https://www.vivaolinux.com.br/script/Servidor-REST

