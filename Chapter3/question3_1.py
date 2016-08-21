class MultipleStacks(object):

    def __init__(self, size = 100, num = 3):
        self.size = size
        self.num = num
        self.array = [None] * size * num
        self.pointer = [-1] * num

    def push(self, n, value):
        if self.pointer[n] == self.size - 1:
            raise IndexError('stack is full')
        self.pointer[n] += 1
        self.array[n * self.size + self.pointer[n]] = value

    def pop(self, n):
        if self.pointer[n] < 0:
            raise IndexError('can\'t pop from empty stack')
        item = self.array[n * self.size + self.pointer[n]]
        self.pointer[n] -= 1
        return item

    def peek(self, n):
        if self.pointer[n] < 0:
            return None
        return  self.array[n * self.size + self.pointer[n]]

    def isEmpty(self, n):
        return self.pointer[n] == -1

if __name__ == "__main__":
    array = MultipleStacks()
    array.push(2, 11)
    array.push(2, 13)
   # print array.pop(0)  # Trying to pop an empty stack.
    print array.peek(2) # 13
    array.push(0, 20)
    array.push(0, 30)
    print array.pop(0)  # 30
    print array.peek(0) # 20
    print array.isEmpty(1)
