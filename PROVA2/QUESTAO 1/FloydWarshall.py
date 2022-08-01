# Função recursivo para imprimir o caminho de um determinado vértice `u` do vértice de origem `v`
def printPath(path, v, u, route):
    if path[v][u] == v:
        return
    printPath(path, v, path[v][u], route)
    route.append(path[v][u])
 
 
# Função para imprimir o menor custo com caminho
# Informação # entre todos os pares de vértices
def printSolution(path, n):
    for v in range(n):
        for u in range(n):
            if u != v and path[v][u] != -1:
                route = [v]
                printPath(path, v, u, route)
                route.append(u)
                print(f'The shortest path from {v} —> {u} is', route)
 
 
# Função para executar o algoritmo Floyd-Warshall
def floydWarshall(adjMatrix):
 
    # caso básico
    if not adjMatrix:
        return
 
    # número total de vértices no `adjMatrix`
    n = len(adjMatrix)
 
    # A matriz de custo e caminho # armazena o caminho mais curto
    # (custo mais curto/rota mais curta)
 
    # inicialmente, o custo seria o mesmo que o peso de uma aresta
    cost = adjMatrix.copy()
    path = [[None for x in range(n)] for y in range(n)]
 
    # inicializa custo e caminho
    for v in range(n):
        for u in range(n):
            if v == u:
                path[v][u] = 0
            elif cost[v][u] != float('inf'):
                path[v][u] = v
            else:
                path[v][u] = -1
 
    # roda Floyd–Warshall
    for k in range(n):
        for v in range(n):
            for u in range(n):
                # Se o vértice `k` estiver no caminho mais curto de `v` para `u`,
                #, em seguida, atualize o valor de cost[v][u] e path[v][u]
                if cost[v][k] != float('inf') and cost[k][u] != float('inf') \
                        and (cost[v][k] + cost[k][u] < cost[v][u]):
                    cost[v][u] = cost[v][k] + cost[k][u]
                    path[v][u] = path[k][u]
 
            # se os elementos diagonais se tornarem negativos, o
            # O gráfico # contém um ciclo de peso negativo
            if cost[v][v] < 0:
                print('Negative-weight cycle found')
                return
 
    # Imprime o caminho mais curto entre todos os pares de vértices
    printSolution(path, n)
 
 
if __name__ == '__main__':
 
    # define o infinito
    I = float('inf')
 
    # dada a representação de adjacência da matriz
    adjMatrix = [
        [0, I, -2, I],
        [4, 0, 3, I],
        [I, I, 0, 2],
        [I, -1, I, 0]
    ]
 
    # Executar algoritmo Floyd-Warshall
    floydWarshall(adjMatrix)