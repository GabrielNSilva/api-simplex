from flask import *
from simplex import *
import json
import copy
from flask_cors import CORS

app = Flask(__name__)
app.debug = True
CORS(app)

@app.route("/simplex")
def index():
    return "hello"


@app.route('/simplex/maximizar', methods=['POST'])
def SimplexMax():
    if request.method == 'POST':
        data = request.get_json()
        # return data
        qtd_var = data['qtd_var']
        qtd_regras = data['qtd_regras']
        funcao = data['funcao']
        regras = data['regras']
        qtd_iterações = data['iteracoes']
        resposta = maximizar(qtd_var, qtd_regras, funcao, regras)
        #print(type(resposta))
        #print(resposta)
        aux = []
        cont=0
        #print(resposta)
        for resp in resposta:
            cont +=1
            if(qtd_iterações >= cont):
                aux2={}
                aux2["labels"] = resp.getLabels()
                for i in range(1, resp.linhas):
                    aux2[aux2["labels"][i-1]] = resp.getLine(i)
                #aux2 = jsonify({"data": aux2})
                aux.append(aux2)
        #for i in aux:   
        #    print(i)
        aux = jsonify({"data": aux})
        return aux
    return jsonify("error")
@app.route('/simplex/minimizar', methods=['POST'])
def SimplexMin():
    if request.method == 'POST':
        data = request.get_json()
        qtd_var = data['qtd_var']
        qtd_regras = data['qtd_regras']
        funcao = data['funcao']
        regras = data['regras']
        qtd_iterações = data['iteracoes']
        aux = [qtd_var, qtd_regras, funcao, regras]
        resposta = minimizar(qtd_var, qtd_regras, funcao, regras)
        aux = []
        cont = 0
        for resp in resposta:
            cont += 1
            if(qtd_iterações >= cont):
                aux2 = {}
                aux2["labels"] = resp.getLabels()
                for i in range(1, resp.linhas):
                    aux2[aux2["labels"][i-1]] = resp.getLine(i)
                #aux2 = jsonify({"data": aux2})
                aux.append(aux2)
        #for i in aux:
        #    print(i)
        aux = jsonify({"data": aux})
        return aux
    return jsonify("error")


@app.route('/simplex/precosoma', methods=['POST'])
def PrecoSoma():
    data = request.get_json()
    resposta = precoSomaCalculo(data)
    return jsonify(resposta)

if __name__ == "__main__":

	app.run()

# consultar https://www.vivaolinux.com.br/script/Servidor-REST
