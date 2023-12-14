class StackUsingArray:
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        return len(self.items)

    def display(self):
        print("Stack:", self.items)


# Example Usage of Stack
stack = StackUsingArray()
stack.push(10)
stack.push(20)
stack.push(30)
stack.display()

popped_element = stack.pop()
print(f"Popped Element: {popped_element}")
stack.display()

print(f"Top Element: {stack.peek()}")
print(f"Stack Size: {stack.size()}")
