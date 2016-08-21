class StackWithMin(object):
    def __init__(self):
        self.stack = []
        self.minimum = []

    def push(self, value):
        self.stack.append(value)
        if self.minimum == [] or self.minimum[-1] >= value:
            self.minimum.append(value)

    def pop(self):
        if self.stack == []:
            return None
        item = self.stack.pop()
        if item == self.minimum[-1]:
            self.minimum.pop()
        return item
    
    def getmin(self):
        if self.minimum == []:
            return None
        return self.minimum[-1]

if __name__ == "__main__":
    array = StackWithMin()
    array.push(6)
    array.push(3)
    array.push(4)
    array.push(2)
    print(array.getmin())
    array.pop()
    print(array.getmin())
