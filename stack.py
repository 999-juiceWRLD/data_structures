from linked_list import LinkedList

class StackArray:
    def __init__(self, *args):
        self.array = []
        for arg in args:
            self.push(arg)
    
    @property
    def size(self):
        return len(self.array)
    
    @property
    def top(self):
        return self.array[-1] if not self.is_empty() else None
    
    def __str__(self):
        return "[ " + " ".join(str(element) for element in reversed(self.array)) + " ]"

    def __len__(self):
        return self.size
    
    def __iter__(self):
        return reversed(self.array)

    def __contains__(self, value):
        return value in self.array
    
    def push(self, value):
        self.array.append(value)
             
    def pop(self):
        if self.size == 0:
            raise IndexError("The stack is empty")
        else:
            value = self.array.pop()
            return value
    
    def peek(self):
        if self.size == 0:
            raise IndexError("The stack is empty")
        else:
            return self.top
    
    def is_empty(self):
        return self.size == 0

    def clear(self):
        self.array.clear()
        
    def copy(self):
        return StackArray(*self.array) # unpack elements into a new stack

class LinkedStack(LinkedList):
    def __init__(self, *values):
        super().__init__()
        for value in values:
            self.insert_head(value)
    
    @property
    def top(self):
        return self.head_node.value if self.head_node else None
    
    def push(self, value):
        self.insert_head(value)
    
    def pop(self):
        if self.size > 0:
            element = self.head_node.value
            self.delete_by_value(self.head_node.value)
            return element
        else:
            raise Exception("The stack list is empty")
        
    def peek(self):
        if self.size == 0:
            raise IndexError("The stack is empty")
        else:
            return self.top

    def is_empty(self):
        return self.size == 0

    def clear(self):
        while self.size != 0:
            self.delete_head()
    
    def copy(self):
        return LinkedStack(*reversed(list(self)))
    