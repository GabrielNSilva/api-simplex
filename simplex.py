from Matriz import *
import copy


def maximizar(qtd_var, qtd_regras, funcao, regras, qtd_iterações):
	tables = []
	vq = Matriz(qtd_var,qtd_regras)
	vq.setFunctionMax(funcao)
	vq.setRules(regras)

	cont = 0
	while vq.zHasNegative():
		min_col_idx = vq.getMinColumnIndex()
		lin_out_idx = vq.getOutLineIndex(min_col_idx)
		vq.normaline(lin_out_idx, min_col_idx)

		vq.escalonamento(lin_out_idx, min_col_idx)


		tables.append(copy.deepcopy(vq))

		cont += 1
		if cont > qtd_iterações:
			break

	#for i in tables:
		#print (i)
	return [tables, cont]


def minimizar(qtd_var, qtd_regras, funcao, regras, qtd_iterações):
	tables = []
	vq = Matriz(qtd_var, qtd_regras)

	vq.setFunctionMin(funcao)
	vq.setRules(regras)

	cont = 0
	while vq.zHasNegative():
		min_col_idx = vq.getMinColumnIndex()
		lin_out_idx = vq.getOutLineIndex(min_col_idx)
		vq.normaline(lin_out_idx, min_col_idx)

		vq.escalonamento(lin_out_idx, min_col_idx)
		tables.append(copy.deepcopy(vq))
		cont+=1
		if cont > qtd_iterações:
			break
	vq.trocaSignal()
	tables.pop()
	tables.append(copy.deepcopy(vq))
	return [tables,cont]


def precoSomaCalculo(obj):

	#print(obj)
	# variavel/V.F/Preço Soma/+/-
	resposta = {}
	coluns = len(obj[obj["labels"][0]])
	lines = len(obj)-1
	regras = lines - 1
	xs = coluns - regras-1
	label = []
	for i in obj:
		if i != "labels" and i[0]=="X":
			j = len(obj[i])-1
			resposta[i] = [ obj[i][j],"-","-","-"]
			label.append(i)
	for x in range(xs):
		x_aux = 'X'+str(x+1)
		exist = False
		for i in obj:
			if i != "labels" and i == x_aux:
				exist= True
				break
		if exist==False :
			resposta[x_aux] = [0, "-", "-", "-"]
			label.append(x_aux)
			print("AAAA")
	for f in range(regras):
		fs = 'F'+str(f+1)
		label.append(fs)
		found = False
		for j in obj:
			if(fs == j):
				found = True
				break

		if(found):	#se existe com um valor
			j = len(obj[fs])-1
			resposta[fs] = [obj[fs][j], precoSoma(xs, fs, obj), precoSomaMM("+", fs, obj, xs), precoSomaMM("-", fs, obj, xs)]
		else:		#se nao existe com um valor
			resposta[fs] = [0, precoSoma(xs,fs, obj), precoSomaMM("+", fs, obj, xs), precoSomaMM("-", fs, obj, xs)]

	#print(label)
	resposta["labels"] = label
	return resposta


def precoSoma(xs,fs,obj):
	for i in obj:
		if (i == "Z"):
			return obj[i][xs+int(fs[len(fs)-1])-1]
	return "-"


def precoSomaMM(signal, fs, obj, xs):

	prox_pos= None
	prox_neg= None

	pos = xs+int(fs[len(fs)-1])-1
	#pos_last = xs + int(fs[len(fs)-1])
	#print("posicoes=", pos,pos_last)
	for i in obj:
		if(i != "labels" and obj[i][pos] != 0):
			result = obj[i][len(obj[i])-1]/obj[i][pos]*(-1)

			#print(obj[i][len(obj[i])-1], "/", obj[i][pos], "*(-1)", " = ", result)
			if ((prox_neg == None) and (result < 0)):
				prox_neg= result
			elif ((prox_pos == None) and (result > 0)):
				prox_pos = result
			elif(result < 0 and result < prox_neg):
				prox_neg = result
			elif(result > 0 and result < prox_pos):
				prox_pos = result
	#print("para o ",fs,"temos + = ",prox_pos," e - = ",prox_neg)

	if(signal == "+"):
		if prox_pos != None:
			return prox_pos
		else:
			return "-"
	else:
		if prox_neg != None:
			return prox_neg*(-1)
		else:
			return "-"

	return "-"
#maximizar(2,2,[11, 12],[[1, 4, 10000],[5, 2, 30000]])
#minimizar(2, 2, [-11, 12], [[1, 4, 10000], [5, 2, 30000]])
