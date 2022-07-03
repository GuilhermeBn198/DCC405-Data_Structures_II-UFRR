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
arr = [70, 80, 33]
n = len(arr)
print('array sem a aplicação do buildHeap')
print(arr)
time.sleep(1)
print('o array inicial é um heap?')
print(isHeap(arr, 0, n))
time.sleep(1)
print('')
buildHeap(arr) 
printHeap(arr)
time.sleep(1)
print('o array após a aplicação do buildHeap é um heap?')
print(isHeap(arr, 0, n))
