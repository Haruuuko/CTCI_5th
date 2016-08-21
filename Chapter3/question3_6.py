class Stack(list):
    def push(self, value):
        self.append(value)

    def peek(self):
        return self[-1]

    def empty(self):
        return len(self) == 0

    def sortStack(self):
        sort = Stack()
        while self:
            if not sort or self[-1] >= sort[-1]:
                sort.push(self.pop())
            else:
                tmp = self.pop()
                while sort and sort[-1] > tmp:
                    self.push(sort.pop())
                sort.push(tmp)
        return sort

stack = Stack([9,4,6,2,5,7,1,5,10])
print(stack.sortStack())
