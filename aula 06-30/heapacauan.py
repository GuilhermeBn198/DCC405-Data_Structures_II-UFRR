def maxHeapify(heap, i):
    esquerd = 2*i
    direit = 2*i + 1
    if esquerd <= len(heap)-1 and heap[esquerd] > heap[i]:
        maior = esquerd
    else:
        maior = i
    if direit <= len(heap)-1 and heap[direit] > heap[maior]:
        maior = direit
    if maior != i:
        heap[i], heap[maior] = heap[maior], heap[i]
        maxHeapify(heap, maior)

def buildHeap(A):
    heapSize = len(A)-1
    for i in range(heapSize//2, 1, -1):
        maxHeapify(A, i)



#--main--
A = [8, 18, 14, 17, 12, 13, 11, 15, 16]
print(A)
buildHeap(A)
print(A)    