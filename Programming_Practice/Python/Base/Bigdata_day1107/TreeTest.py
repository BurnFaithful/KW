from Bigdata_day1106.BinaryTree import *

if __name__ == "__main__":
    tree = BinaryTree()
    n1 = TreeNode('A')
    n2 = TreeNode('B')
    n3 = TreeNode('C')
    n4 = TreeNode('D')
    n5 = TreeNode('E')
    n6 = TreeNode('F')
    n7 = TreeNode('G')
    n8 = TreeNode('H')
    n1.left = n2; n1.right = n3
    n2.left = n4; n2.right = n5
    n3.left = n6; n3.right = n7
    n4.left = n8
    tree.root = n1

    print(f"tree의 깊이 : {tree.depth(tree.root)}")
    print(f"tree의 노드 갯수 : {tree.size(tree.root)}")
    tree_copy = BinaryTree()
    tree_copy.root = tree.copy(tree.root)
    print(f"tree와 tree_copy 비교 : {tree.isEqual(tree.root, tree_copy.root)}")

    print(f"{'preorder : ':<15}", end='')
    tree.preOrder(tree.root)
    print()
    print(f"{'inorder : ':<15}", end='')
    tree.inOrder(tree.root)
    print()
    print(f"{'postorder : ':<15}", end='')
    tree.postOrder(tree.root)
    print()
    print(f"{'levelorder : ':<15}", end='')
    tree.levelOrder(tree.root)
    print()