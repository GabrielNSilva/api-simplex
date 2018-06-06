class Matriz:

	def __init__(self, qtdX, qtdF):
		qtdF = int(qtdF)
		qtdX = int(qtdX)
		self.qtdX = qtdX
		self.qtdF = qtdF
		self.linhas = qtdF+2
		self.colunas = qtdF+qtdX+2
		self.mat = []
		self.montaMat()
		# #print(self.mat)

	def __str__(self):
		string = ""

		for i in self.mat:
			for j in i:
				string += str(j)+"\t"
			string += "\n"

		return string

	def montaMat(self):
		for i in range(self.linhas):
			self.mat.append([0]*self.colunas)

		self.mat[0][0] = 'Base'
		self.mat[self.qtdF+1][0] = 'Z'
		self.mat[0][self.qtdF+self.qtdX+1] = 'b'

		for i in range(1,self.qtdF+1):
			self.mat[i][0] = 'F'+str(i)
			self.mat[i][i+2] = 1
			self.mat[0][self.qtdX+i] = 'F'+str(i)

		for i in range(1,self.qtdX+1):
			self.mat[0][i] = 'X'+str(i)

	def getLabels(self):
		label = []

		for i in range(1,self.linhas):
			label.append(self.mat[i][0])

		return label

	def getLine(self,num):
		# return self.mat[num]
		linha = []
		for i in range(1,self.colunas):
	  		linha.append(self.mat[num][i])
		return linha

	def setLine(self, num):#, vet):
		# try:
		# 	if len(vet) != self.colunas-1:
		# 		raise IndexError('Quantidade de objetos no vetor INVALIDA!')
		# 	else:
				for i in range(1, self.colunas):
					self.mat[num][i] = vet[i-1]
		# except IndexError as e:
		# 	raise e

	def setFunctionMax(self,values):
		col = 0
		for val in values:
			col = col + 1
			self.mat[self.linhas-1][col] = -val

	def setFunctionMin(self, values):
		col = 0
		for val in values:
			col = col + 1
			self.mat[self.linhas-1][col] = val

	def setRules(self,rules):
		row = col = 0
		for rule in rules:
			row = row + 1
			col = 0
			self.mat[row][self.colunas-1] = rule.pop()
			for val in rule:
				col = col + 1
				# #print("self.mat["+str(row)+"]["+str(col)+"] = "+str(val))
				# #print()
				self.mat[row][col] = val

	def zHasNegative(self):
		if min(self.getLine(self.linhas-1)) < 0:
			return True
		return False

	def getMinColumnIndex(self):
		a = self.getLine(self.linhas-1)
		#print('z line: '+str(a))
		return a.index(min(a))+1

	def getOutLineIndex(self,col):
		if self.mat[1][col] != 0:
			aux = self.mat[1][self.colunas-1]/self.mat[1][col]
		else:
			aux = 99999999999999999999999999999999999999
		idx = 1

		for i in range(1,self.linhas-1):
			if self.mat[i][col] != 0:
				res = self.mat[i][self.colunas-1]/self.mat[i][col]
			else:
				res = 0
			#print('divisao da linha '+str(i)+': '+str(res))
			if 0 < res < aux:
				aux = res
				idx = i
		return idx

	def normaline(self, row_idx, col_idx):
		self.mat[row_idx][0] = self.mat[0][col_idx]
		pivo = self.mat[row_idx][col_idx]
		#print(pivo)
		for n in range(1, self.colunas):
			if pivo != 0:
				self.mat[row_idx][n] /= pivo

	def escalonamento(self, row_idx, col_idx):
		for i in range(1,self.linhas):
			if i != row_idx:
				pivo = self.mat[i][col_idx]
				for j in range(1, self.colunas):
					self.mat[i][j] = (self.mat[row_idx][j] * -pivo) + self.mat[i][j]
				# linha_norm * -pivo + linha_a_zerar

	def trocaSignal(self):

		##print (len(self.mat))
		self.mat[self.linhas - 1][self.colunas - 1] *= -1
