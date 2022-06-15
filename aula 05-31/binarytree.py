class Node:
    def __init__(self, key):
        self.value = key
        self.left = None
        self.right = None

n10 = Node(1)
n8 = Node(6)
n25 = Node(7)
n15 = Node(8)

n10.right = n25
n10.left = n8
n25.left = n15

def printBST(root):
    if root:
        print(root.value)
        printBST(root.left) #chama a própria função recursivamente até esse ponto até que o ultimo nó à esquerda da arvore apresente NONE, daí continua a função agora imprimindo os valores da direita da arvore
        printBST(root.right)
        #->printando a arvore de ladinho<-
def printTree(root, level = 0):
    if root is not None:
        printTree(root.right, level+1)
        print(' ' * 4*level + '->' + str(root.value))
        printTree(root.left, level+1)
#->percursos de profundidade<-
def preOrdem(root):
    if root:
        print(root.value, end = " ")
        preOrdem(root.left)
        preOrdem(root.right)

def inOrdem(root):
    if root:
        inOrdem(root.left)
        print(root.value, end = " ")
        inOrdem(root.right)

def posOrdem(root):
    if root:
        posOrdem(root.left)
        posOrdem(root.right)
        print(root.value, end = " ")
        
printBST(n10)
print('aaaaaaaaaa')
#printTree(n10)
print(preOrdem(n10))
print(inOrdem(n10))
print(posOrdem(n10))