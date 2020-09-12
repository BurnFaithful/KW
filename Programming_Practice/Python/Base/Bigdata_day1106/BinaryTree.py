from Bigdata_day1106.TreeNode import TreeNode


class BinaryTree:
    def __init__(self):
        self.__root = None

    @property
    def root(self):
        return self.__root

    @root.setter
    def root(self, value):
        self.__root = value


    def preOrder(self, n):
        if n is not None:
            print(str(n.item), ' ', end='')
            if n.left is not None:
                self.preOrder(n.left)
            if n.right is not None:
                self.preOrder(n.right)


    def inOrder(self, n):
        if n is not None:
            if n.left is not None:
                self.inOrder(n.left)
            print(str(n.item), ' ', end='')
            if n.right is not None:
                self.inOrder(n.right)


    def postOrder(self, n):
        if n is not None:
            if n.left is not None:
                self.postOrder(n.left)
            if n.right is not None:
                self.postOrder(n.right)
            print(str(n.item), ' ', end='')


    def levelOrder(self, root):
        queue = list()
        queue.append(root)
        while queue:
            popNode = queue.pop(0)
            print(str(popNode.item), ' ', end='')

            if popNode.left is not None:
                queue.append(popNode.left)
            if popNode.right is not None:
                queue.append(popNode.right)


    def depth(self, root):
        if root is None:
            return 0
        else:
            return 1 + max(self.depth(root.left), self.depth(root.right))


    def size(self, root):
        if root is None:
            return 0
        else:
            return 1 + self.size(root.left) + self.size(root.right)


    def copy(self, n):
        if n is None:
            return None
        else:
            left = self.copy(n.left)
            right = self.copy(n.right)
            return TreeNode(n.item, left, right)


    def isEqual(self, n, m):
        if n is None and m is None:
            return True

        if n.item != m.item:
            return False
        return self.isEqual(n.left, m.left) and self.isEqual(n.right, m.right)
