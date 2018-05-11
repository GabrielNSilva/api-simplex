from Matriz import *
import ast

from flask import Flask
from flask import request
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/maximize", methods=['POST'])
def max():
    print(request.form)
    print()

    qtd_var = request.form['qtd_var']
    qtd_regras = request.form['qtd_regras']
    funcao = ast.literal_eval(request.form['funcao'])
    regra = ast.literal_eval(request.form['regra'])

    mat_max = Matriz(qtd_var, qtd_regras)
    mat_max.setFunction(funcao)
    mat_max.setRules(regra)
    print(mat_max.mat)
    while mat_max.zHasNegative():
        min_col_idx = mat_max.getMinColumnIndex()
        lin_out_idx = mat_max.getOutLineIndex(min_col_idx)
        mat_max.normaline(lin_out_idx, min_col_idx)
        print(mat_max)
        mat_max.escalonamento(lin_out_idx, min_col_idx)
        print(mat_max)

    return str(mat_max.mat)
