from LinkedList import *

def partition(linkedList, x):
    small, large = LinkedList(), LinkedList();
    node = linkedList.head
    while node:
        if node.value < x:
            small.addNode(node.value)
        else:
            large.addNode(node.value)
        node = node.next
    small.tail.next = large.head
    return small

test = LinkedList()
test.generate(20, 0, 9)
print(test)
print(partition(test, 8))


