class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if node is None:
            return Node(key)
        if key < node.key:
            node.left = self._insert_recursive(node.left, key)
        else:
            node.right = self._insert_recursive(node.right, key)
        return node

    def find_max(self):
        if self.root is None:
            return None
        current = self.root
        while current.right:
            current = current.right
        return current.key

    def find_min(self):
        if self.root is None:
            return None
        current = self.root
        while current.left:
            current = current.left
        return current.key

    def sum_values(self):
        return self._sum_recursive(self.root)

    def _sum_recursive(self, node):
        if node is None:
            return 0
        return node.key + self._sum_recursive(node.left) + self._sum_recursive(node.right)


# Example usage
binary_search_tree = BinarySearchTree()
binary_search_tree.insert(20)
binary_search_tree.insert(10)
binary_search_tree.insert(300)
binary_search_tree.insert(25)
binary_search_tree.insert(40)

print("Maximum value in the tree:", binary_search_tree.find_max())
print("Minimum value in the tree:", binary_search_tree.find_min())
print("Sum of all values in the tree:", binary_search_tree.sum_values())
