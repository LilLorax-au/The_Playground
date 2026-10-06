



class Queue:
    DEF_CAP: int = 10

    def __init__(self):
        self.data: list = [None] * Queue.DEF_CAP
        self.size: int = 0
        self.front: int = 0

    def enqueue(self, e):
        if self.size == len(self.data):
            self.resize(len(self.data) * 2)
        avail = (self.front + self.size) % len(self.data)
        self.data[avail] = e
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")

        value = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % len(self.data)
        self.size -= 1
        return value
    
    def resize(self, cap):
        old = self.data
        self.data = [None] * cap
        walk = self.front

        for k in range(self.size):
            self.data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self.front = 0

    def first(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        else:
            return self.data[self.front]

    def __len__(self):
        return self.size

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False
