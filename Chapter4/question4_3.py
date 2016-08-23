class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return "( " + str(self.value) + " ( " + str(self.left) + " | " + str(self.right) + "))" 

def createMinBST(arr, start, end):
    if end < start: return None
    mid = (start + end)/2
    node = TreeNode(arr[mid])
    node.left = createMinBST(arr, start, mid - 1)
    node.right = createMinBST(arr, mid + 1, end)
    return node

#testing

array1=[1,2,3,4,5,6,7,8,9,10,12,15,18,22,43,44,51]
array2=[1,2,3,4,5,6,7,8,9,10,12,15,18,22,43,44,51,55]

print(createMinBST(array1, 0, len(array1) - 1))
print(createMinBST(array2, 0, len(array2) - 1))
