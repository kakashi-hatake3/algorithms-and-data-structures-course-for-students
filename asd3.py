class BNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert_node(root, data):
    if root is None:
        return BNode(data)
    if data < root.data:
        root.left = insert_node(root.left, data)
    else:
        root.right = insert_node(root.right, data)
    return root


def sorted_nodes_in_order(root):
    result = []
    _in_order_traversal(root, result)
    return result


def _in_order_traversal(node, result):
    if node:
        _in_order_traversal(node.left, result)
        result.append(node.data)
        _in_order_traversal(node.right, result)


def print_b(node):
    if node is None:
        return
    print_b(node.left)
    print(node.data, end=" ")
    print_b(node.right)


def construct_tree(expression):
    stack = []
    root = None
    for char in expression:
        if char == "(":
            new_node = BNode(None)
            if root is None:
                root = new_node
            else:
                top = stack[-1]
                if top.left is None:
                    top.left = new_node
                else:
                    top.right = new_node
            stack.append(new_node)
        elif char == ")":
            stack.pop()
        else:
            if char.isdigit():
                if stack[-1].data is None:
                    stack[-1].data = int(char)
                else:
                    stack[-1].data = stack[-1].data * 10 + int(char)
    return root


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def toAVL(self, arr):
        if not arr:
            return None
        mid = len(arr) // 2
        root = Node(arr[mid])
        root.left = self.toAVL(arr[:mid])
        root.right = self.toAVL(arr[mid+1:])
        root.height = 1 + max(self._height(root.left), self._height(root.right))
        return root

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None:
            return False
        if key == node.key:
            return True
        elif key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    def insert(self, key):
        if not self.root:
            self.root = Node(key)
        else:
            self._insert(key, self.root)

    def _insert(self, key, node):
        if key < node.key:
            if node.left:
                self._insert(key, node.left)
            else:
                node.left = Node(key)
        else:
            if node.right:
                self._insert(key, node.right)
            else:
                node.right = Node(key)

        node.height = 1 + max(self._height(node.left), self._height(node.right))

        self._balance(node)

    def delete(self, key):
        self.root = self._delete(key, self.root)

    def _delete(self, key, node):
        if not node:
            return node
        elif key < node.key:
            node.left = self._delete(key, node.left)
        elif key > node.key:
            node.right = self._delete(key, node.right)
        else:
            if not node.left and not node.right:
                node = None
            elif not node.left:
                node = node.right
            elif not node.right:
                node = node.left
            else:
                min_node = self._find_min(node.right)
                node.key = min_node.key
                node.right = self._delete(min_node.key, node.right)

        if not node:
            return node

        node.height = 1 + max(self._height(node.left), self._height(node.right))

        self._balance(node)

        return node

    def _balance(self, node):
        balance_factor = self._height(node.left) - self._height(node.right)
        if balance_factor > 1:
            if self._height(node.left.left) >= self._height(node.left.right):
                node = self._rotate_right(node)
            else:
                node.left = self._rotate_left(node.left)
                node = self._rotate_right(node)
        elif balance_factor < -1:
            if self._height(node.right.right) >= self._height(node.right.left):
                node = self._rotate_left(node)
            else:
                node.right = self._rotate_right(node.right)
                node = self._rotate_left(node)

    def _rotate_right(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self._height(z.left), self._height(z.right))
        y.height = 1 + max(self._height(y.left), self._height(y.right))

        return y

    def _rotate_left(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self._height(z.left), self._height(z.right))
        y.height = 1 + max(self._height(y.left), self._height(y.right))

        return y

    def _height(self, node):
        if not node:
            return 0
        return node.height

    def _find_min(self, node):
        if node.left:
            return self._find_min(node.left)
        return node

    def preorder_traversal(self):
        self._preorder_traversal(self.root)

    def _preorder_traversal(self, root):
        if not root:
            return
        print(root.key, end=" ")
        self._preorder_traversal(root.left)
        self._preorder_traversal(root.right)

    def width_first(self):
        if not self.root:
            return

        queue = [self.root]

        while queue:
            node = queue.pop(0)
            print(node.key, end=" ")

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def depth_first(self):
        stack = [self.root]

        while stack:
            node = stack.pop()
            print(node.key, end=" ")

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

    def depth_second(self, root):
        stack = []
        current = root
        done = False

        while not done:
            if current is not None:
                stack.append(current)
                current = current.left
            else:
                if len(stack) > 0:
                    current = stack.pop()
                    print(current.key, end=" ")
                    current = current.right
                else:
                    done = True

    def depth_third(self):
        stack1 = [self.root]
        stack2 = []

        while stack1:
            node = stack1.pop()
            stack2.append(node)

            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)

        while stack2:
            node = stack2.pop()
            print(node.key, end=" ")


root = BNode(5)
insert_node(root, 3)
insert_node(root, 7)
insert_node(root, 2)
insert_node(root, 4)

print("Вывод двоичного дерева:")
print_b(root)

expression = '(8 (9 (5)) (1))'
tree = construct_tree(expression)
print("\nСкобочная запись: ")
print_b(tree)

avl_tree_from_bst = AVLTree()
avl_tree_from_bst.root = avl_tree_from_bst.toAVL(sorted_nodes_in_order(root))

print("\nПреобразованное AVL-дерево:")
avl_tree_from_bst.preorder_traversal()

print("\nВ ширину:")
avl_tree_from_bst.width_first()

print("\nВ глубину 1:")
avl_tree_from_bst.depth_first()

print("\nВ глубину 2:")
avl_tree_from_bst.depth_second(avl_tree_from_bst.root)

print("\nВ глубину 3:")
avl_tree_from_bst.depth_third()
