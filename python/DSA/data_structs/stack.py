



class Stack:
    def __init__(self):
        self.elements: list = []
    
    def push(self, element):
        self.elements.append(element)

    def pop(self):
        if self.__is_empty():
            raise IndexError("Stack is empty")
        else:
            return self.elements.pop()

    def top(self):
        return self.elements[-1]

    def __len__(self):
        return len(self.elements)

    def __is_empty(self):
        if len(self.elements) == 0:
            return True
        else:
            return False


