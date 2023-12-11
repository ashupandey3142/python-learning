class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class QueueUsingLinkedList:
    def __init__(self):
        self.front = self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            return None
        removed_item = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return removed_item

    def front_element(self):
        if self.is_empty():
            return None
        return self.front.data

    def size(self):
        count = 0
        current = self.front
        while current:
            count += 1
            current = current.next
        return count

    def display(self):
        current = self.front
        while current:
            print(current.data, end=" ")
            current = current.next
        print()


# Example Usage of Queue
queue = QueueUsingLinkedList()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.display()

dequeued_element = queue.dequeue()
print(f"Dequeued Element: {dequeued_element}")
queue.display()

print(f"Front Element: {queue.front_element()}")
print(f"Queue Size: {queue.size()}")
