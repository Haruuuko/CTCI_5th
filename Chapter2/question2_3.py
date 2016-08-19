from LinkedList import *

def deleteNode(node):
    if node.next:
        node.value = node.next.value
        node.next = node.next.next
    else:
        node.next = None

test = LinkedList()
test.generate(20, 0, 9)
node = test.head.next.next
print (test)
deleteNode(node)
print(test)

