from node import NodeCore as Node

class LinkedList:
    def __init__(self, value=None, node=Node):
        self._Node = node
        if value is not None:
            self.head_node = self._Node(value)
            self.tail_node = self.head_node
            self._size = 1
        else:
            self.head_node = None
            self.tail_node = None
            self._size = 0
    
    @property
    def size(self):
        return self._size
    
    def __str__(self):
        return "[ " + " ".join(str(node) for node in self) + " ]"
    
    def __len__(self):
        return self._size
    
    def __getitem__(self, index):
        if index < 0:
            index += self._size
        if not 0 <= index < self._size:
            raise IndexError(f"Index {index} is out of bounds")
        else:
            return self.find_by_index(index)
    
    def __iter__(self):
        current_node = self.head_node
        while current_node:
            yield current_node.value
            current_node = current_node.next_node
        
    def insert_head(self, value):
        new_node = self._Node(value)
        new_node.next_node = self.head_node
        self._size += 1
        self.head_node = new_node
        if self._size == 1:
            self.tail_node = new_node
        
    def insert_tail(self, value):
        new_node = self._Node(value)
        if self._size == 0:
            self.head_node = new_node
            self.tail_node = self.head_node
        else:
            self.tail_node.next_node = new_node
            self.tail_node = new_node
        self._size += 1
    
    def insert_index(self, index, value):
        if index < 0 or index > self._size - 1:
            raise IndexError(f"Index {index} out of bounds for insertion")
        else:
            if index == 0:
                self.insert_head(value)
                return
            current_node = self.head_node
            counter = 0
            while counter < index - 1:
                current_node = current_node.next_node
                counter += 1
            new_node = self._Node(value)
            next_node = current_node.next_node
            current_node.next_node = new_node
            self._size += 1
            new_node.next_node = next_node
    
    def delete_head(self):
        if self.head_node is None:
            raise Exception("Cannot delete from an empty list")
        second_node = self.head_node.next_node
        self._size -= 1
        self.head_node = second_node

    def delete_tail(self):
        if self.head_node is None:
            raise Exception("Cannot delete from an empty list")
        elif self._size == 1:
            self.head_node = None
            self.tail_node = None
        else:
            current_node = self.head_node        
            while current_node.next_node.next_node is not None:
                current_node = current_node.next_node
            self.tail_node = current_node
            current_node.next_node = None
        self._size -= 1
    
    def delete_index(self, index):
        if index < 0 or index > self._size - 1:
            raise IndexError(f"Index {index} is out of bounds for deletion - List size: {self._size}")
        current_node = self.head_node
        counter = 0
        if self._size == 1 or index == 0:
            self.delete_head()
        else:
            while counter < index - 1: # get to the previous node of the node we want to delete
                current_node = current_node.next_node
                counter += 1
            next_node = current_node.next_node.next_node
            current_node.next_node = next_node
            self._size -= 1
            
    def delete_value(self, value):
        current_node = self.head_node
        previous_node = None
        
        while current_node is not None:
            if current_node.value == value:
                if previous_node is None:
                    self.delete_head()
                    return
                else:
                    previous_node.next_node = current_node.next_node
                    self._size -= 1
                    return
            previous_node = current_node
            current_node = current_node.next_node
        
        raise ValueError(f"{value} is not in the list")
                  
    def find_by_index(self, index):
        if index < 0:
            index += self._size
        if index > self._size - 1:
            raise IndexError(f"Index {index} is out of bounds for check")
        current_node = self.head_node
        counter = 0
        while current_node is not None:
            if counter == index:
                return current_node.value
            else:
                current_node = current_node.next_node
                counter += 1
        
    def traverse(self):
        current_node = self.head_node
        while current_node is not None:
            print(current_node.value)
            current_node = current_node.next_node
