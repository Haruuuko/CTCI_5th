class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return "( " + str(self.value) + " ( " + str(self.left) + " | " + str(self.right) + "))" 

def createLevelLinkedListDFS(root, lists, level):
    if root == None: return
    if len(lists) == level:
        lists.append([])
    lists[level].append(root.value)
    createLevelLinkedListDFS(root.left, lists, level + 1);
    createLevelLinkedListDFS(root.right, lists, level + 1);
    return lists

def createLevelLinkedListBFS(root):
    lists = []
    if root: listbuf = [root]
    while listbuf:
        lists.append(listbuf)
        nodes, listbuf = listbuf, []
        for n in nodes:
            if n.left: listbuf.append(n.left)
            if n.right: listbuf.append(n.right)
    return lists

n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n1.left = n2
n1.right = n4
n2.left = n3
n2.right = n5

print(n1)
print(createLevelLinkedListDFS(n1, [], 0))
print(createLevelLinkedListBFS(n1))


