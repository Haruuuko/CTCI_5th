from LinkedList import *

def isPalindrome(linkedList):
    newlist = []
    slow, fast = linkedList.head, linkedList.head
    while fast and fast.next:
        newlist.append(slow.value)
        slow, fast = slow.next, fast.next.next
    if fast: slow = slow.next
    while slow:
        if slow.value != newlist.pop():
            return False
        slow = slow.next
    return True

test = LinkedList()
test.addNode(1)
test.addNode(2)
test.addNode(3)
test.addNode(4)
test.addNode(3)
test.addNode(2)
test.addNode(1)

print(test)
print(isPalindrome(test))

    
