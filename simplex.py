from Matriz import *

def maximizar(qtd_var, qtd_regras, funcao, regras):
	vq = Matriz(qtd_var,qtd_regras)

	vq.setFunction(funcao)
	vq.setRules(regras)
	print(vq)
	print()

	while vq.zHasNegative():
		min_col_idx = vq.getMinColumnIndex()
		lin_out_idx = vq.getOutLineIndex(min_col_idx)
		vq.normaline(lin_out_idx, min_col_idx)
		print(vq)
		vq.escalonamento(lin_out_idx, min_col_idx)
		print(vq)
		# break

maximizar(2,2,[11, 12],[[1, 4, 10000],[5, 2, 30000]])
