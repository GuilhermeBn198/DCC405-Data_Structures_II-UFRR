def maxHeapify(heap, i):
    e = 2*i
    d = 2*i + 1
    if e <= len(A)-1 and A[e] > A[i]:
        maior = e
    else:
        maior = i
    if d <= len(A)-1 and A[d] > A[maior]:
        maior = d
    if maior != i:
        A[i], A[maior] = A[maior], A[i]
        maxHeapify(A, maior)

def buildHeap(A):
    heapSize = len(A)-1
    for i in range(heapSize//2, 1, -1):
        maxHeapify(A, i)



#--main--
A = [8, 18, 14, 17, 12, 13, 11, 15, 16]
print(A)
buildHeap(A)
print(A)