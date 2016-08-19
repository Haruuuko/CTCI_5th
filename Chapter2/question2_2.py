from LinkedList import *

def kthNode(linkedList, k):
    if not linkedList.head: return None
    slow = fast = linkedList.head
    while k:
        fast = fast.next
        k -= 1 
    while fast.next:
        slow, fast = slow.next, fast.next
    return slow.next

test = LinkedList()
test.generate(20, 0, 9)
print (test)
print(kthNode(test, 3).value)

