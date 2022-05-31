class Node:
    def __init__(self, key):
        self.value = key
        self.left = None
        self.right = None

n10 = Node(10)
n8 = Node(8)
n25 = Node(25)
n15 = Node(15)

n10.right = n25
n10.left = n8
n25.left = n15

def printBST(root):
    if root:
        print(root.value)
        printBST(root.left) #chama a própria função recursivamente até esse ponto até que o ultimo nó à esquerda da arvore apresente NONE, daí continua a função agora imprimindo os valores da direita da arvore
        printBST(root.right)
        
printBST(n10)