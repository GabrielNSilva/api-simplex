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
				for i in range(1,self.colunas):
					self.mat[num][i] = vet[i-1]
		# except IndexError as e:
		# 	raise e

	def zHasNegative(self):
		if min(self.getLine(self.linhas-1)) < 0:
			return True
		return False

	def getMinColumnIndex(self):
		a = self.getLine(self.linhas-1)
		return a.index(min(a))

	def getOutLineIndex(self,col):
		aux = self.mat[1][self.colunas-1]/self.mat[1][col]
		idx = 1

		for i in range(1,self.linhas-1):
			res = self.mat[i][self.colunas-1]/self.mat[i][col]
			if res < aux and res > 0:
				aux = res
				idx = i
		return idx

	def normaline(self, row_idx, col_idx):
		pivo = self.mat[row_idx][col_idx]



	def escalonamento():
