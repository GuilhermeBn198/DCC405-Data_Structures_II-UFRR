def calcdist(mindis, maxdis):
	if(mindis < maxdis): return mindis
	return maxdis

def maxdist(distD, salaA):
	if(distD > salaA): return distD
	return salaA

def main():
	mindist = 250 #valor inicial de mindist, conforme a funçãor for iterando seu valor irá se reduzindo até chegar na distancia minima correta
	salas, path = map(int,input().split()) #pega a quantidade de salas e de corredores

	mounter = [[31 if(i != j) else 0 for i in range(250)] for j in range(250)] #lista de lista com 250 entradas, correspondente ao numero total de salas possiveis no pedido da questão
  
	for k in range(0,salas):
		for i in range(0,salas):
			for j in range(0,salas):
				mounter[i][j] = calcdist(mounter[i][j], mounter[i][k] + mounter[k][j])
    
	for i in range(0, path):
		distD, salaA, salaB = map(int,input().split()) #define as variaveis da distancia das salas
		distD-= 1
		salaA-= 1
		mounter[distD][salaA] = salaB
		mounter[salaA][distD] = salaB
  
	for i in range(0, salas):
		maximo = 0
		for j in range(0, salas):
			maximo = maxdist(maximo, mounter[i][j])
		mindist = calcdist(mindist, maximo)

	print(mindist)


#----main----
main()