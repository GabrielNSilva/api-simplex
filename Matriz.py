class Matriz:

	def __init__(self, qtdX, qtdF):
		self.qtdX = qtdX
		self.qtdF = qtdF
		self.linhas = qtdF+2
		self.colunas = qtdF+qtdX+2
		self.mat = []
		self.montaMat()
		print(self.mat)

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
			self.mat[0][self.qtdX+i] = 'F'+str(i)

		for i in range(1,self.qtdX+1):
			self.mat[0][i] = 'X'+str(i)

	def getLine(self,num):
		# return self.mat[num]
		linha = []
		for i in range(1,self.colunas):
	  		linha.append(self.mat[num][i])
		return linha

	def setLine(self, num, vet):
		# try:
		# 	if len(vet) != self.colunas-1:
		# 		raise IndexError('Quantidade de objetos no vetor INVALIDA!')
		# 	else:
				for i in range(1, self.colunas):
					self.mat[num][i] = vet[i-1]
		# except IndexError as e:
		# 	raise e

	def zHasNegative(self):
		if min(self.getLine(self.linhas-1)) < 0:
			return True
		return False

	def getMinColumnIndex(self):
		a = self.getLine(self.linhas-1)
		print('z line: '+str(a))
		return a.index(min(a))+1

	def getOutLineIndex(self,col):
		aux = self.mat[1][self.colunas-1]/self.mat[1][col]
		idx = 1

		for i in range(1,self.linhas-1):
			res = self.mat[i][self.colunas-1]/self.mat[i][col]
			print('divisao da linha '+str(i)+': '+str(res))
			if 0 < res < aux:
				aux = res
				idx = i
		return idx

	def normaline(self, row_idx, col_idx):
		self.mat[row_idx][0] = self.mat[0][col_idx]
		pivo = self.mat[row_idx][col_idx]
		print(pivo)
		for n in range(1, self.colunas):
			self.mat[row_idx][n] /= pivo

	def escalonamento(self, row_idx, col_idx):
		for i in range(1,self.linhas):
			pivo = self.mat[i][col_idx]
			if i != row_idx:
				for j in range(1, self.colunas):
					self.mat[i][j] = (self.mat[row_idx][j] * -pivo) + self.mat[i][col_idx]
				# linha_norm * -pivo + linha_a_zerar
