from LinkedList import *

def addList(list1, list2):
    a, b = list1.head, list2.head
    result = LinkedList()
    temp = 0
    while a and b:
        num = (a.value + b.value + temp) % 10
        result.addNode(num)
        temp = (a.value + b.value + temp) / 10
        a, b = a.next, b.next
    if a:
        result.addNode(a.value + temp)
        reuslt.tail.next = a.next
    elif b:
        result.addNode(b.value + temp)
        result.tail.next = b.next
    return result

l1, l2 = LinkedList(), LinkedList()
l1.generate(5, 0, 9)
l2.generate(6, 0, 9)
print(l1)
print(l2)
print(addList(l1, l2))

