from MatrizPNE import *

vq = Matriz(2,2)

print()
print(vq)
print(vq.zHasNegative())
print()

# print(vq.retornaLinha(2))

vq.setLine(1, [1,4,1,0,10000])
vq.setLine(2, [5,2,0,1,30000])
vq.setLine(3, [-11,-12,0,0,0])
print(vq)
print(vq.zHasNegative())

while vq.zHasNegative():
	min_col_idx = vq.getMinColumnIndex()
	lin_out_idx = vq.getOutLineIndex(min_col_idx)
