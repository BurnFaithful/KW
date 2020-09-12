from Bigdata_day1106.BinaryTree import *


class BSTNode:
    def __init__(self, key, value, left=None, right=None, parent=None):
        self.key = key
        self.value = value
        self._left = left
        self._right = right
        self.parent = parent

    @property
    def left(self):
        return self._left

    @property
    def right(self):
        return self._right

    @left.setter
    def left(self, node):
        if self._left:
            self._left.parent = None

        if node is not None:
            node.parent = self
            self._left = node

    @right.setter
    def right(self, node):
        if self._right:
            self._right.parent = None

        if node is not None:
            node.parent = self
        self._right = node

    def isLeftChild(self):
        return self.parent and self.parent.left is self

    def isRightChild(self):
        return self.parent and self.parent.right is self

    def hasLeftChild(self):
        return self._left is not None

    def hasRightChild(self):
        return self._right is not None

    def hasBothChild(self):
        return self._left is not None and self._right is not None

    def isRoot(self):
        return self.parent is None

    def isLeaf(self):
        return self._left is None and self._right is None


'''
없는 키로 탐색을 하면 None을 반환.
중복되는 키값을 추가하면 노드를 갱신.
삭제하려는 노드의 자노드가 모두 있다면, 우측 노드의 최소키 노드를 이동하는 정책을 사용.
'''
class BinarySearchTree:
    def __init__(self, root):
        self.root = root


    def get(self, key):
        if self.root is None:
            return None

        node = self.root
        while node.key != key:
            if node.key > key:
                if node.left is None:
                    return None
                else:
                    node = node.left
            elif node.key < key:
                if node.right is None:
                    return None
                else:
                    node = node.right

        return node

    def put(self, key, value):
        if self.root is None:
            self.root = BSTNode(key, value)
            return

        node = self.root
        while True:
            if node.key > key:
                if node.left is None:
                    node.left = BSTNode(key, value)
                    break
                else:
                    node = node.left
            elif node.key < key:
                if node.right is None:
                    node.right = BSTNode(key, value)
                    break
                else:
                    node = node.right

    def delete_min(self):
        minNode = self.min(self.root)
        if minNode is None:
            return None
        self.delete(minNode.key)

    def delete_max(self):
        maxNode = self.max(self.root)
        if maxNode is None:
            return None
        self.delete(maxNode.key)

    def delete(self, key):
        if key == self.root.key and self.root.isLeaf(): # 지울 노드가 루트이고 루트의 자노드가 없을 때(깊이가 1인 경우)
            self.root = None

        deleteNode = self.get(key)
        if deleteNode is None:
            return None

        # 둘 다 없을 때 -> 부모 노드와의 연결을 끊는다.
        # 오른쪽 자노드가 없을 때 -> 왼쪽 자노드를 올린다.
        # 왼쪽 자노드가 없을 때 -> 오른쪽 자노드를 올린다.
        # 자노드가 2개일 때 -> 정책을 결정 후 정책대로 수행. (left 방향 트리의 최대값을 올리거나, right 방향 트리의 최소값을 올린다.)
        if deleteNode.isLeaf(): # 둘 다 없는 경우
            if deleteNode.isLeftChild():
                deleteNode.parent.left = None
            elif deleteNode.isRightChild():
                deleteNode.parent.right = None
        elif deleteNode.hasBothChild(): # 둘 다 있는 경우
            inheritNode = self.min(deleteNode)
            inheritNode.parent.left = self.sliceTree(inheritNode)
            deleteNode.key, deleteNode.value = inheritNode.key, inheritNode.value
        else: # 한 쪽만 있는 경우
            deleteNode_child = deleteNode.left if deleteNode.hasLeftChild() else deleteNode.right
            deleteNode.left = None
            deleteNode.right = None
            if deleteNode.isRoot():
                self.root = deleteNode_child
            elif deleteNode.isLeftChild():
                deleteNode.parent.left = deleteNode_child
            elif deleteNode.isRightChild():
                deleteNode.parent.right = deleteNode_child


    def sliceTree(self, node):
        iterNode = None
        if node.hasRightChild():
            iterNode = node.right
            node = node.right
            while node.hasRightChild():
                iterNode.right = node.right
                node = node.right

        return iterNode


    def min(self, start):
        node = start
        while node.left is not None:
            node = node.left

        return node

    def max(self, start):
        node = start
        while node.right is not None:
            node = node.right

        return node

    def inOrder(self, node):
        if node is not None:
            if node.left is not None:
                self.inOrder(node.left)
            print(f"[{str(node.key)} : {str(node.value)}] ", end='')
            if node.right is not None:
                self.inOrder(node.right)
