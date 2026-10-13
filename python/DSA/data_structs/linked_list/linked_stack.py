from ..errors import Empty


class LinkedStack:
    def __init__(self):
        """Creating an emtpy stack"""
        self.head = None
        self.size = 0

    def __len__(self):
        """making sure len returns size of the stack"""
        return self.size

    def is_empty(self):
        """Check if the stack is emtpy"""
        return self.size == 0

    def push(self, e):
        """Push element e to the top of the stack, then ++ to size"""
        self.head = e
        self.size += 1

    def top(self):
        """Return top element, without destroying it"""
        if self.is_empty():
            raise Empty("Stack is Empty")
        return self.head

    def pop(self):
        if self.is_empty():
            raise Empty("Stack is Empty")
        else:
            value = self.head
            self.size -= 1
            return value
