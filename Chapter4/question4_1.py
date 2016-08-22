import random

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return "( " + str(self.value) + " ( " + str(self.left) + " | " + str(self.right) + "))" 

def isBalancedBinaryTree(root):
    return False if checkHeight(root) == -1 else True

def checkHeight(root):
    if root == None: return 0
    leftHeight = checkHeight(root.left)
    if leftHeight == -1: return -1
    rightHeight = checkHeight(root.right)
    if rightHeight == -1: return -1

    if abs(leftHeight - rightHeight) > 1:
        return -1
    else:
        return max(leftHeight, rightHeight) + 1


#unittest
ubt = TreeNode(random.randint(0, 100))
for c1 in xrange(0,9):
    bt2 = TreeNode(random.randint(0, 100))
    bt2.left = ubt
    ubt=bt2

def makeRandomBalancedTree(depth):
    if depth>0:
        node = TreeNode(random.randint(0, 100))
        node.left=makeRandomBalancedTree(depth-1)
        node.right=makeRandomBalancedTree(depth-1)
        return node
    else:
        return None

bt = makeRandomBalancedTree(3)

print(ubt)
print(isBalancedBinaryTree(ubt))

print(bt)
print(isBalancedBinaryTree(bt))

