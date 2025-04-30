class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def max_depth(root):
    if not root:
        return 0
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)
    return max(left_depth, right_depth) + 1

def preorder_traversal(root):
    if not root:
        return []
    return [root.val] + preorder_traversal(root.left) + preorder_traversal(root.right)

def inorder_traversal(root):
    if not root:
        return []
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)

def postorder_traversal(root):
    if not root:
        return []
    return postorder_traversal(root.left) + postorder_traversal(root.right) + [root.val]

def preorder_count(root):
    if not root:
        return 0
    return 1 + preorder_count(root.left) + preorder_count(root.right)

def inorder_count(root):
    if not root:
        return 0
    return inorder_count(root.left) + 1 + inorder_count(root.right)

def postorder_count(root):
    if not root:
        return 0
    return postorder_count(root.left) + postorder_count(root.right) + 1

# Exemplo de uso:
root = TreeNode(1, 
    TreeNode(2, 
        TreeNode(4, 
            TreeNode(8), TreeNode(9)
        ), 
        TreeNode(5, 
            TreeNode(10), TreeNode(11)
        )
    ), 
    TreeNode(3, 
        TreeNode(6, 
            TreeNode(12), TreeNode(13)
        ), 
        TreeNode(7, 
            TreeNode(14), TreeNode(15)
        )
    )
)

print("Profundidade Máxima:", max_depth(root))
print("Número de nós percorridos na Pré-ordem:", preorder_count(root))
print("Número de nós percorridos na Em ordem:", inorder_count(root))
print("Número de nós percorridos na Pós-ordem:", postorder_count(root))
print("Pré-ordem:", preorder_traversal(root))
print("Em ordem:", inorder_traversal(root))
print("Pós-ordem:", postorder_traversal(root))
