class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def insert_node(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root= new_node
        else:
            self.insert_recursive(self.root, new_node)

    def insert_recursive(self, node, new_node):
        if new_node.data < node.data:
            if node.left is None:
                node.left = new_node
            else:
                self.insert_recursive(node.left, new_node)
        if new_node.data > node.data:
            if node.right is None:
                node.right = new_node
            else:
                self.insert_recursive(node.right, new_node)

    def in_order_taversal(self):
        self.in_order_taversal_recursive(self.root)
        print()

    def in_order_taversal_recursive(self, node):
        if node:
            self.in_order_taversal_recursive(node.left)
            print(node.data)
            self.in_order_taversal_recursive(node.right)

    def pre_order_traversal(self):
        self.pre_order_traversal_recursive(self.root)
        print()

    def pre_order_traversal_recursive(self, node):
        if node:
            print(node.data)
            self.pre_order_traversal_recursive(node.left)
            self.pre_order_traversal_recursive(node.right)

    def post_order_traversal(self):
        self.post_order_traversal_recursive(self.root)

    def post_order_traversal_recursive(self, node):
        if node:
            self.post_order_traversal_recursive(node.left)
            self.post_order_traversal_recursive(node.right)
            print(node.data)

if __name__ == '__main__':
    tree = Tree()

    data = [50, 30, 70, 40, 20, 60, 80]
    for dat in data:
        tree.insert_node(dat)

    tree.in_order_taversal()
    tree.pre_order_traversal()
    tree.post_order_traversal()

