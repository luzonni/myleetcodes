class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#Resolução do leetcode 104.

def maxDepth(root):
    if not root:
        return 0
    leftDepth = maxDepth(root.left)
    rightDepth = maxDepth(root.right)
    return max(leftDepth, rightDepth) + 1


#Postorder

def postorderCount(root):
    if not root:
        return 0
    return postorderCount(root.left) + postorderCount(root.right) + 1

def postorderTraversal(root):
    if not root:
        return []
    return postorderTraversal(root.left) + postorderTraversal(root.right) + [root.val]


#Preorder

def preorderCount(root):
    if not root:
        return 0
    return 1 + preorderCount(root.left) + preorderCount(root.right)

def preorderTraversal(root):
    if not root:
        return []
    return [root.val] + preorderTraversal(root.left) + preorderTraversal(root.right)

#Inorder

def inorderCount(root):
    if not root:
        return 0
    return inorderCount(root.left) + 1 + inorderCount(root.right)

def inorderTraversal(root):
    if not root:
        return []
    return inorderTraversal(root.left) + [root.val] + inorderTraversal(root.right)


#Execução

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

print("Profundidade Máxima:", maxDepth(root))
print("Número de nós percorridos na Preorder:", preorderCount(root))
print("Número de nós percorridos na Inorder:", inorderCount(root))
print("Número de nós percorridos na Postorder:", postorderCount(root))
print("Preorder:", preorderTraversal(root))
print("Inorder:", inorderTraversal(root))
print("Postorder:", postorderTraversal(root))

