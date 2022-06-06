class Node:
    def __init__(self, key):
        self.value = key
        self.left = None
        self.right = None

n2 = Node(2)
n3 = Node(3)
n5 = Node(5)
n6 = Node(6)
n4 = Node(4)

n2.right = n4
n2.left = n3
n3.left = n5
n3.right = n6


def addBT(root):
    if (root == None):
        return 0
    return (root.value + addBT(root.left) + addBT(root.right)) # recursivamente percorre toda a extensão da árvore buscando valores NONE, quando os acha, para a execução e retorna 0, a somas irão crescer infinitamente até o percurso da arvore estar finalizado

def find_sum(root):
    
    if root:
        print("valor do nó: ")
        print(root.value)
        # var1 = root.value
        # aux = var1 + aux
        # print("valor da soma atual de todos os nós: ", aux)
        find_sum(root.left) #chama a própria função recursivamente até esse ponto até que o ultimo nó à esquerda da arvore apresente NONE, daí continua a função agora imprimindo os valores da direita da arvore
        find_sum(root.right)


find_sum(n2)
print("o valor da soma final de todos os nós é: ", addBT(n2))