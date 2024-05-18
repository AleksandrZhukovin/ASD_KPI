from random import shuffle


class Node:
    def __init__(self, key, data=None, left=None, right=None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return f'Node {self.key} | ({self.data})'


class BinaryTree:
    def __init__(self):
        self.root = None

    def inorder_walk(self, node):
        if node is not None:
            return self.inorder_walk(node.left) + [node] + self.inorder_walk(node.right)
        else:
            return []

    def search(self, key, node):
        if node is None or key == node.key:
            return node
        if key < node.key:
            return self.search(key, node.left)
        else:
            return self.search(key, node.right)

    def insert(self, key, data, node):
        if self.root is None:
            self.root = Node(key, data)
        else:
            if key < node.key:
                if node.left is None:
                    node.left = Node(key, data)
                else:
                    self.insert(key, data, node.left)
            else:
                if node.right is None:
                    node.right = Node(key, data)
                else:
                    self.insert(key, data, node.right)

    def delete(self, root, key):
        if root is None:
            return root

        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            temp_key = self.min_node(root.right).key
            root.key = temp_key
            root.right = self.delete(root.right, temp_key)

        return root

    @staticmethod
    def min_node(node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def print_tree(self, node):
        if node.right is None and node.left is None:
            line = f'{node.key}({node.data})'
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        if node.right is None:
            lines, n, p, x = self.print_tree(node.left)
            s = f'{node.key}({node.data})'
            u = len(s)
            first_line = s + (n - x) * ' ' + (u - x) * ' '
            second_line = ' ' * x + '/' + (n - x - 1) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        if node.left is None:
            lines, n, p, x = self.print_tree(node.right)
            s = f'{node.key}({node.data})'
            u = len(s)
            first_line = s + x * ' ' + (u - x) * ' '
            second_line = (u - 1) * ' ' + '\\' + (x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        left, n, p, x = self.print_tree(node.left)
        right, m, q, y = self.print_tree(node.right)
        s = f'{node.key}({node.data})'
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first + u * ' ' + second for first, second in zipped_lines]
        return [first_line, second_line] + lines, n + m + u, max(p, q) + 2, n + u // 2


tree = BinaryTree()
with open('text.txt', 'r') as file:
    words = file.readline().split()
    keys = [key for key in range(len(words))]
    shuffle(keys)
    n = 0
    for word in words:
        tree.insert(keys[n], word.lower(), tree.root)
        n += 1

for i in tree.print_tree(tree.root)[0]:
    print(i)

nodes_to_delete = []

for node in tree.inorder_walk(tree.root):
    if node.data[0].lower() == 'w':
        nodes_to_delete.append(node)

for node in nodes_to_delete:
    tree.delete(tree.root, node.key)

print('=' * 50)

for i in tree.print_tree(tree.root)[0]:
    print(i)
