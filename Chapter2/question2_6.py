from LinkedList import *

def loopBegin(linkedList):
    slow, fast, start = linkedList.head, linkedList.head, linkedList.head
    while slow and fast:
        slow, fast = slow.next, fast.next.next
        if slow == fast: break
    while start and slow:
        start, slow = start.next, slow.next
        if start == slow: break
    return start

test = LinkedList()
test.generate(20, 0, 9)
print(test)
test.tail.next = test.head.next.next.next
print(loopBegin(test).value)

