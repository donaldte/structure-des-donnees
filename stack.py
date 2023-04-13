class Pile:
    def __init__(self):
        self.elements = []

    def push(self, element):
        self.elements.append(element)

    def is_empty(self):
        return len(self.elements) == 0

    def pop(self):
        if not self.is_empty():
            return self.elements.pop()

    def peek(self):
        if not self.is_empty():
            return self.elements[-1]


stack = Pile()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

print(stack.elements)

print(stack.pop())
print(stack.peek())
print(stack.elements)
print(stack.is_empty())