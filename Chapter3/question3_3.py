class SetOfStacks:
    def __init__(self, size):
        self.size = size
        self.stack = []

    def push(self, value):
        if self.stack == [] or len(self.stack[-1]) == self.size:
            self.stack.append([])
        self.stack[-1].append(value)

    def pop(self):
        if self.stack == []:
            return None
        item = self.stack[-1].pop()
        if self.stack[-1] == []:
            self.stack.pop()
        return item

    def popAt(self, index):
        if self.stack == []:
            return None
        return self.stack[index - 1].pop()

if __name__ == "__main__":
    array = SetOfStacks(3)
    array.push(2)
    array.push(3)
    array.push(4)
    array.push(5)
    array.push(6)
    print(array.popAt(1))
    print(array.pop())

