class MyQueue:
    def __init__(self):
        self.stack = []
        self.reverse = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.reverse != []:
            return self.reverse.pop()
        while self.stack != []:
            self.reverse.append(self.stack.pop())
        if self.reverse == []:
            return None
        return self.reverse.pop()

    def peek(self):
        if self.reverse != []:
            return self.reverse[-1]
        while self.stack != []:
            self.reverse.append(self.stack.pop())
        if self.reverse == []:
            return None
        return self.reverse

if __name__ == "__main__":
    queue = MyQueue()
    queue.push(2)
    queue.push(3)
    queue.push(4)
    print(queue.pop())
    print(queue.peek())


