class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self, data):
        self.root = Node(data)

    def insertNode(self, root, data):
        new_node = Node(data)
        temp = root
        
        while temp is not None:
            if data < temp.data:
                if temp.left is None:
                    temp.left = new_node
                    break
                else:
                    temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    break
                else:
                    temp = temp.right

    def calculate_height(self, node):
        if node is None:
            return -1 

        left_height = self.calculate_height(node.left)
        right_height = self.calculate_height(node.right)

        return 1 + max(left_height, right_height)

    def inorderTraversal(self, node):
        if node is not None:
            self.inorderTraversal(node.left)
            print(node.data, end=" ")
            self.inorderTraversal(node.right)

if __name__ == '__main__':
    n = int(input())
    root_get = int(input())
    bst = BinarySearchTree(root_get)
    
    for i in range(n - 1):
        data = int(input())
        bst.insertNode(bst.root, data)

    print("Inorder traversal: ")
    bst.inorderTraversal(bst.root)
    print("\nHeight of the tree: ")
    print(bst.calculate_height(bst.root))