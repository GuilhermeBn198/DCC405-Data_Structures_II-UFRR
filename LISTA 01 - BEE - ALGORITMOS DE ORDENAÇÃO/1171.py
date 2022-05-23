n = int(input())
numbers = []

for i in range(n):
    entry = int(input())
    numbers.append(entry)
	#cria-se a primeira lista de numeros 

#[8, 10, 8, 260, 4, 10, 10]
aux = sorted(set(numbers)) #cria-se uma variavel auxiliar para ordenar em orden crescente os numeros da primeira lista e a função set não deixa eles repetirem
#[4, 8, 10, 260]

for l in range(len(aux)): # agora para printar no console uma lista do tamanho da lista auxiliar com a quantidade de vezes que ela vai aparecer
	print('{} aparece {} vez(es)'.format(aux[l], numbers.count(aux[l])))