from Matriz import *

def maximizar(qtd_var, qtd_regras, funcao, regras):
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
	return vq

def minimizar(qtd_var, qtd_regras, funcao, regras):
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
	vq.trocaSignal()
	return vq
#maximizar(2,2,[11, 12],[[1, 4, 10000],[5, 2, 30000]])
#minimizar(2, 2, [-11, 12], [[1, 4, 10000], [5, 2, 30000]])
