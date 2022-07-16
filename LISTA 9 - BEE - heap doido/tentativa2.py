import time

#percorrer array
def left(index):
  return 2 * index + 1

def right(index):
  return 2 * (index + 2)

def parent(index):
  return index - 1 // 2

def getLastNonLeaf(n):
  return n // 2 - 1

# função auxiliar de construção do heap
def heapify(arr, i):
    n = len(arr)
    bignum = i  # Initialize bignum as root
    if left(i) < n and arr[left(i)] > arr[bignum]:
        bignum = left(i)
        
    # If right child is larger than bignum so far
    if right(i) < n and arr[right(i)] > arr[bignum]:
        bignum = right(i)
        
    # If bignum is not root
    if bignum != i:
        arr[i], arr[bignum] = arr[bignum], arr[i]
        
        # Recursively heapify the affected sub-tree
        heapify(arr, bignum)

def buildHeap(arr):
    n = len(arr)
    startIdx = getLastNonLeaf(n) # Index of last non-leaf node
    # Perform reverse level order traversal
    # from last non-leaf node and heapify
    # each node
    for i in range(startIdx, -1, -1):
        heapify(arr, i)

def printHeap(arr):
    n = len(arr)
    print("Array representation of Heap is:")
    for i in range(n):
        print(arr[i], end=" ")
    print()

def isHeap(arr, i, n):
    # If a leaf node
    if (i >= (n - 2) / 2):
        return True
 
    # se um nó interno é maior que seu filho esquerdo e maior que seu filho direito, recursivamente chama a função isHeap novamente para os filhos
    if arr[i] >= arr[2 * i + 1] and arr[i] >= arr[2 * i + 2] and isHeap(arr, 2 * i + 1, n) and isHeap(arr, 2 * i + 2, n):
        return True
 
    return False

#main

class MaxHeap:
    def __init__(self):
        self.heap = []

    def hasParent(self, i):
        return parent(i) < len(self.heap)

    def hasLeftChild(self, i):
        return left(i) < len(self.heap)

    def hasRightChild(self, i):
        return right(i) < len(self.heap)

    def insert(self, key):
        heap.append(key)
        heapify(len(self.heap) - 1)

    def getMax(self):
        return self.heap[0]
    
    def printHeap(self):
        print(self.heap) 

    def printLeftRootRight(self, low, high): # PROF! NÃO CONSEGUI FORMATAR O PRINT COM OS PARENTESES CORRETAMENTE
      if low > high:
        return
      self.printLeftRootRight(low*2 + 1, high)
      print("{left}/{right}".format(left = self.heap[low][0], right = self.heap[low][1]), end=" ")
      self.printLeftRootRight(low*2 + 2, high)

while True:
  heap = MaxHeap()
  data = input().split(' ')
  n = int(data[0])
  if (n == 0): break
  cases = data[1: n + 1]

  for val in cases:
    nodeval, priority = val.split('/')
    heap.insert((nodeval, priority))
  heap.printLeftRootRight(0, len(heap.heap) - 1)

heap = MaxHeap()
heap.insert(('a', 3))
heap.insert(('b', 6))
heap.insert(('c', 4))
heap.insert(('d', 7))
heap.insert(('e', 2))
heap.insert(('f', 5))
heap.insert(('g', 1))
heap.printHeap()
heap.printLeftRootRight(0, len(heap.heap) - 1)



# maxHeap = MaxHeap(15)
# maxHeap.insert(5)
# maxHeap.insert(3)
# maxHeap.insert(17)
# maxHeap.insert(10)
# maxHeap.insert(84)
# maxHeap.insert(19)
# maxHeap.insert(6)
# maxHeap.insert(22)
# maxHeap.insert(9)

