from Matriz import *
import copy

def maximizar(qtd_var, qtd_regras, funcao, regras):
	tables = []
	vq = Matriz(qtd_var,qtd_regras)
	vq.setFunctionMax(funcao)
	vq.setRules(regras)
	#print(vq)
	#print()

	while vq.zHasNegative():
		min_col_idx = vq.getMinColumnIndex()
		lin_out_idx = vq.getOutLineIndex(min_col_idx)
		vq.normaline(lin_out_idx, min_col_idx)
		#print(vq)
		vq.escalonamento(lin_out_idx, min_col_idx)
		#print(vq)
		# break
		tables.append(copy.copy(vq))
	#for i in tables:
	#	print(i)
	return tables

def minimizar(qtd_var, qtd_regras, funcao, regras):
	tables = []
	vq = Matriz(qtd_var, qtd_regras)

	vq.setFunctionMin(funcao)
	vq.setRules(regras)
	#print(vq)
	#print()

	while vq.zHasNegative():
		min_col_idx = vq.getMinColumnIndex()
		lin_out_idx = vq.getOutLineIndex(min_col_idx)
		vq.normaline(lin_out_idx, min_col_idx)
		#print(vq)
		vq.escalonamento(lin_out_idx, min_col_idx)
		#print(vq)
		# break
		tables.append(copy.copy(vq))
	vq.trocaSignal()
	tables.append(copy.copy(vq))
	return tables

maximizar(2,2,[11, 12],[[1, 4, 10000],[5, 2, 30000]])
#minimizar(2, 2, [-11, 12], [[1, 4, 10000], [5, 2, 30000]])
