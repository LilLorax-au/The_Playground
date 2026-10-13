from linked_list import _Node




class SinglyLinkedList:

    def __init__(self):
        self.head: _Node | None = None
        self.size: int = 0

    def append(self, e):
        old = self.head
        self.head = _Node(e, old)

        self.size += 1

