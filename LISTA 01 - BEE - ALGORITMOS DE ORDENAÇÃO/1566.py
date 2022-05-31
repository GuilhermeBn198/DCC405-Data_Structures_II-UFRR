def countingSort(A):
  # Encontra maximo de A
  maxElement= max(A)
  
  # Inicializa C com (max+1) zeros 
  C = [0] * (maxElement+1) #preenche vetor com 0s
  
  # Conta os elementos
  for a in A: 
    C[a] += 1
  
  print(C)
  
  result = []
  for i in range(len(C)):
    for j in range(C[i]):
      result.append(i)
  
  return result
#-------------------------------#
#----main----#
altura = [231]
numcasos = int(input("digite aqui a quantidade de casos a serem analisados:  "))
while numcasos > 0:
  print (numcasos)
  numpessoas = int(input("digite aqui a quantidade de pessoas a serem analisadas nesse caso: "))
  while numpessoas > 0:
    print("digite a altura das pessoas do caso: ")

    vetorpessoas = list(map(input(),split()))

    countingSort(vetorpessoas)

    print(' '.join(str(x) for x in vetorpessoas))
    numpessoas = numpessoas - 1
  numcasos = numcasos - 1
