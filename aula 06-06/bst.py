#->estrutura do nó<-
class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return Node(value)
    else:
        if value < root.value:
            root.left = insert(root.left, value)
        elif value > root.value:
            root.right = insert(root.right, value)
    return root
          
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


#->printando a arvore de ladinho<-
def printTree(root, level = 0):
    if root is not None:
        printTree(root.right, level+1)
        print(' ' * 4*level + '->' + str(root.value))
        printTree(root.left, level+1)


#->achar o menor valor da arvore<-
def findMin(root):
    if root is None:
        return None
    while root.left != None:
        root = root.left
        return root.value


#->achar o maior valor da arvore<-
def findMax(root):
    if root is None:
        return None
    while root.right != None:
        root = root.right
        return root.value


#->achar a altura total da arvore<-
def findHeight(root):
  if root is None:
      return 1
  leftH = findHeight(root.left)
  rightH = findHeight(root.right)
  return max(leftH, rightH) + 1

#remover 1 node da arvore
#def removeNode(root,) #falta implementar!! exercicio pra casa!!!


#->percurso em level(BFS)<-
import queue
q = queue.Queue()
def levelOrder(root):
    if root is None: return None
    q.put(root)
    while not q.empty():
        current = q.queue[0]
        print(current.value, end = " ")
        if current.left is not None: q.put(current.left)
        if current.right is not None: q.put(current.right)
        q.get()


#->!implementando a arvore!<-
root = None
root = insert(root, 10)
root = insert(root, 5)
root = insert(root, 2)
root = insert(root, 35)
root = insert(root, 8)
root = insert(root, 40)
root = insert(root, 38)
root = insert(root, 51)

#->!imprimindo tudo!<-
printTree(root)
print("Min: ", findMin(root))
print("Max: ", findMax(root))
print("Altura: ", findHeight(root))
print(levelOrder(root))