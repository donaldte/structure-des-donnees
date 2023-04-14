class LinkStack:
    """ Implementation d'une pile en utilisant une liste chainee simple"""
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, element):
        self._head = self._Node(element, self._head)
        self._size += 1

    def top(self):
        if not self.is_empty():
            return self._head._element
        return None

    def pop(self):
        if not self.is_empty():
            obj = self._head._element
            self._head = self._head._next
            self._size -= 1
            return obj
        return None


linkedStack = LinkStack()
linkedStack.push(2)
linkedStack.push(3)
linkedStack.push(4)
print(linkedStack.is_empty())
print(linkedStack.top())
print(linkedStack.pop())
print(linkedStack.pop())
print(linkedStack.top())
