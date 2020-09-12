class Node:
    def __init__(self, name, left = None, right = None):
        self.name = name
        self.left = left
        self.right = right


def map():
    n1 = Node("Y")
    n2 = Node("O")
    n3 = Node("U")
    n4 = Node("N")
    n5 = Node("G")
    n6 = Node("M")
    n7 = Node("I")
    n8 = Node("N")
    n9 = Node("K")
    n10 = Node("W")
    n11 = Node("O")
    n1.left = n2; n1.right = n3
    n2.left = n4; n2.right = n5
    n3.left = n6; n3.right = n7
    n4.left = n8; n4.right = n9
    n5.left = n10; n5.right = n11
    return n1
#          Y
#     O         U
#  N     G   M      I
#N  K   W O

def preOrder(n):
    if n is not None:
        print(n.name, ' => ', end='')
        preOrder(n.left)
        preOrder(n.right)

def postOrder(n):
    if n is not None:
        postOrder(n.left)
        postOrder(n.right)
        print(n.name, ' => ', end='')

def inOrder(n):
    if n is not None:
        inOrder(n.left)
        print(n.name, ' => ', end='')
        inOrder(n.right)

if __name__ == '__main__':
    n = map()
    preOrder(n)
    print()
    postOrder(n)
    print()
    inOrder(n)