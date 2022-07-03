import queue
import time

class Node:
    def __init__(self, value=None):
        self.value = value
        self.esq = None
        self.dir = None
        self.daltura = 0

# funções de alteração da arvore
def insertNode(root, value):
    if root is None:
        return Node(value)
    else:
        if value < root.value:
            root.esq = insertNode(root.esq, value)
        elif value > root.value:
            root.dir = insertNode(root.dir, value)
    root.daltura = max(findHeight(root.esq), findHeight(root.dir)) + 1

    balanceFactor = getBalance(root)

    if (balanceFactor < -1):
      if (value > root.dir.value): #Rotação simples à Esquerda
        return leftRotate(root)
      else: # Rotação Dupla à Esquerda
        root.dir = rightRotate(root.dir)
        return leftRotate(root)
    if (balanceFactor > 1):
      if (value < root.esq.value): #Rotação simples à direita
        return rightRotate(root)
      else: # Rotação dupla à direita
        root.esq = leftRotate(root.dir)
      return rightRotate(root)

    return root

def deleteDeepest(root, d_node):
    q = []
    q.append(root)
    while(len(q)):
        temp = q.pop(0)
        if temp is d_node:
            temp = None
            return
        if temp.dir:
            if temp.dir is d_node:
                temp.dir = None
                return
            else:
                q.append(temp.dir)
        if temp.esq:
            if temp.esq is d_node:
                temp.esq = None
                return
            else:
                q.append(temp.esq)

def deletion(root, key):
    if root == None:
        return None
    if root.esq == None and root.dir == None:
        if root.key == key:
            return None
        else:
            return root
    key_node = None
    q = []
    q.append(root)
    temp = None
    while(len(q)):
        temp = q.pop(0)
        if temp.value == key:
            key_node = temp
        if temp.esq:
            q.append(temp.esq)
        if temp.dir:
            q.append(temp.dir)
    if key_node:
        x = temp.value
        deleteDeepest(root, temp)
        key_node.value = x
    return root

def deleteNode(root, value):
    if root is None:
        return None
    elif value < root.value:
        root.esq = deleteNode(root.esq, value)
    elif value > root.value:
        root.dir = deleteNode(root.dir, value)
    else:  # Nó foi encontrado
        # Caso 1: Nó folha
        if root.esq and root.dir is None:
            root = None
        # Caso 2: Nó tem um filho
        elif root.esq is None:
            temp = root
            root = root.dir
            temp = None
        elif root.dir is None:
            temp = root
            root = root.esq
            temp = None
        # Caso 3: Nó tem dois filhos
        else:
            minNode = findMin(root.dir)
            root.value = minNode.value
            root.dir = deleteNode(root.dir, minNode.value)
    return root



# funções de print
def inOrder(root):
    if root:
        inOrder(root.esq)
        print(root.value, end=" ")
        inOrder(root.dir)

def preOrdem(root):
    if root:
        print(root.value)
        preOrdem(root.esq)
        preOrdem(root.dir)

def printTree(root, level=0):
    if root is not None:
        printTree(root.dir, level+1)
        print(' ' * 4 * level + '-> ' + str(root.value))
        printTree(root.esq, level+1)

q = queue.Queue()
def levelOrder(root):
    if root is None:
        return None
    q.put(root)
    while not q.empty():
        current = q.queue[0]
        print(current.value, end=" ")
        if current.esq is not None:
            q.put(current.esq)
        if current.dir is not None:
            q.put(current.dir)
        q.get()


# Funções de busca
def getHeight(root):
    if root is None:
        return -1
    return root.daltura

def getBalance(root):
  if root is None:
    return 0
  return getHeight(root.esq) - getHeight(root.dir)

def findMin(root):
    if root is None:
        return None
    while root.esq != None:
        root = root.esq
    return root

def findMax(root):
    if root is None:
        return None
    while root.dir != None:
        root = root.dir
    return root

def findHeight(root):
    if root is None:
        return -1
    leftH = findHeight(root.esq)
    rightH = findHeight(root.dir)
    return max(leftH, rightH) + 1

# Funções de Rotação!
def leftRotate(z):
  y = z.dir
  z.dir = y.esq
  y.esq = z
  z.daltura = findHeight(z)
  y.daltura = findHeight(y)
  return y

def rightRotate(z):
  y = z.esq
  z.esq = y.dir
  y.dir = z
  z.daltura = findHeight(z)
  y.daltura = findHeight(y)
  return y



# Main
root = None
root = insertNode(root, 1)
root = insertNode(root, 4)
root = insertNode(root, 3)
root = insertNode(root, 5)
root = insertNode(root, 6)
root = insertNode(root, 2)
print('imprimindo a arvore agora!')
time.sleep(1)
printTree(root)
time.sleep(1)
print('')
print('agora outras estatisticas interessantes!')
print('min: ', findMin(root).value)
print('max: ', findMax(root).value)
print('altura: ', findHeight(root))
print('ordem por nível: ')
levelOrder(root)
print('')
time.sleep(1)
print('agora apagando o nó 6')
# deletion(root, 3)
deleteNode(root, 6)
time.sleep(1)
printTree(root)