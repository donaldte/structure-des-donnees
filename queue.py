class Queue:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return len(self.elements) == 0

    def enqueue(self, element):
        self.elements.append(element)

    def dequeue(self):
        if not self.is_empty():
            return self.elements.pop(0)
        return None

    def rear(self):
        if not self.is_empty():
            return self.elements[-1]
        return None

    def front(self):
        if not self.is_empty():
            return self.elements[0]
        return None



queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue.elements)

print(queue.dequeue())
print(queue.rear())
print(queue.front())
print(queue.elements)
print(queue.dequeue())
print(queue.elements)