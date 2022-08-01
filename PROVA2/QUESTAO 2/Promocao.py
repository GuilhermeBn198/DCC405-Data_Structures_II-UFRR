# reconhece os inputs
rock = int(input())
#recolhe os inputs
graph = [[] for i in range(rock)] #faz um grafo os do tamanho do input inicial com []

cache = [[-1]*rock, [-1]*rock]

for i in range(rock-1): #f
    rodA, rodB, empres = (int(i) for i in input().split()) #aqui pega-se os valores para os vertices do grafo fazendo um append
    graph[rodA - 1].append((rodB - 1, empres))
    graph[rodB - 1].append((rodA - 1, empres))

def caminhoTop(vertice, empresa_anterior):
    maior = 0    
    for vizinho, empresa in graph[vertice]:
        if empresa != empresa_anterior:
            cami = cache[empresa][vizinho] #apos verificar se a empresa atual é diferente da empresa anterior que é passada como Nula no inicio das iterações é atribuido o cache[empresa][vizinho] para cami, na primeira iteração observa-se que o cami resultará em -1 assim ativando a trilha de recursividade mas agora passando a empresa atual pelo argumento da função e atualizando o cache
            if cami == -1:
                cami = caminhoTop(vizinho, empresa)
                cache[empresa][vizinho] = cami        
            if cami > maior:
                maior = cami
    return maior + 1

resultado = 0
for i in range(rock):
    caminho = caminhoTop(i, None)
    if caminho > resultado:
        resultado = caminho

print(resultado)