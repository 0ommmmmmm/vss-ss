class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(node, key):
    if node is None:
        return Node(key)
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
    return node

def deleteNode(root, key):
    if root is None:
        return root
    if key < root.key:
        root.left = deleteNode(root.left, key)
    elif key > root.key:
        root.right = deleteNode(root.right, key)
    else:
        # one child or no child
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
        # two children — find inorder successor (smallest in right subtree)
        successor = root.right
        while successor.left is not None:
            successor = successor.left
        root.key = successor.key
        root.right = deleteNode(root.right, successor.key)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)

# Test
root = None
for k in [5, 3, 7, 2, 4, 6, 8]:
    root = insert(root, k)

print("Before delete:"); inorder(root)
root = deleteNode(root, 3)
print("\nAfter delete 3:"); inorder(root)