from LinkedList import *

def removeDup(linkedList):
    if linkedList.head is None: return
    current = linkedList.head
    listSet = set([current.value])
    while current.next:
        if current.next.value in listSet:
            current.next = current.next.next
        else:
            listSet.add(current.next.value)
            current = current.next
    return linkedList

def removeDupWithoutTemp(linkedList):
    if linkedList.head is None: return
    current = linkedList.head
    while current:
        runner = current
        while runner.next:
            if runner.next.value == current.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next


test = LinkedList()
test.generate(20, 0, 9)
print (test)
removeDup(test)
print(test)

test.generate(20, 0, 9)
print(test)
removeDupWithoutTemp(test)
print(test)





