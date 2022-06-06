class Node:
    def __init__(self, key):
        self.value = key
        self.left = None
        self.right = None

n1 = Node(0)
n2 = Node(1)
n3 = Node(0)
n4 = Node(1)
n5 = Node(1)
n6 = Node(1)
n7 = Node(0)

n1.right = n3
n1.left = n2
n3.left = n4
n4.left = n5
n4.right = n6
n3.right = n7

def count_unival_subtrees(root):
    count, _ = helper(root)
    return count

# Also returns number of unival subtrees, and whether it is itself a unival subtree.
def helper(root):
    if root is None:
        return 0, True

    contador_esquerdo, eh_unival_esquerdo = helper(root.left)
    contador_direito, eh_unival_direito = helper(root.right)
    contator_total = contador_esquerdo + contador_direito

    if eh_unival_esquerdo and eh_unival_direito:
        if root.left is not None and root.value != root.left.value:
            return contator_total, False
    
        if root.right is not None and root.value != root.right.value:
            return contator_total, False
    
        return contator_total + 1, True
    return contator_total, False

print(count_unival_subtrees(n1))