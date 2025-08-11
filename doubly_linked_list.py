from node import NodeCore

class Node(NodeCore):
    def __init__(self, value, next_node=None, prev_node=None):
        super().__init__(value, next_node)
        self._prev_node = prev_node
    
    @property
    def prev_node(self):
        return self._prev_node
    
    @prev_node.setter
    def prev_node(self, value):
        self._prev_node = value

class DoublyLinkedList:
    def __init__(self, value=None):
        if value is not None:
            self.head_node = Node(value)
            self.tail_node = self.head_node
            self._size = 1
        else:
            self.head_node = None
            self.tail_node = None
            self._size = 0
    
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
        if self._size == 0:
            self.head_node = Node(value)
            self.tail_node = self.head_node
        else:
            new_node = Node(value)
            new_node.next_node = self.head_node
            self.head_node.prev_node = new_node
            self.head_node = new_node
        self._size += 1
    
    def insert_tail(self, value):
        new_node = Node(value)
        if self._size == 0:
            self.head_node = new_node
            self.tail_node = self.head_node
        else:
            self.tail_node.next_node = new_node
            final_node = self.tail_node.next_node
            final_node.prev_node = self.tail_node
            self.tail_node = final_node
        self._size += 1
    
    def delete_head(self):
        if self._size == 0:
            raise Exception("Cannot delete from an empty list")
        elif self._size == 1:
            self.head_node = None
            self.tail_node = None
        else:    
            self.head_node = self.head_node.next_node
            self.head_node.prev_node = None
        self._size -= 1
    
    def delete_tail(self):
        if self._size == 0:
            raise Exception("Cannot delete from an empty list")
        elif self._size == 1:
            self.head_node = None
            self.tail_node = None
        else:
            self.tail_node = self.tail_node.prev_node
            self.tail_node.next_node = None
        self._size -= 1

    def delete_index(self, index):
        if index < 0 or index > self._size - 1:
            raise IndexError(f"Index {index} is out of bounds")
        current_node = self.head_node
        counter = 0
        if self._size == 1 or index == 0:
            self.delete_head()
        else:
            while counter < index - 1:
                current_node = current_node.next_node
                counter += 1
            next_node = current_node.next_node.next_node
            current_node.next_node = next_node
            if next_node is None:
                self.tail_node = current_node
            else:
                next_node.prev_node = current_node
            self._size -= 1
            return
        
    def delete_value(self, value):
        if self._size == 0:
            raise Exception(f"Cannot delete from an empty list")
        else:
            current_node = self.head_node
            prev_node = None
            while current_node is not None:
                if current_node.value == value:
                    if prev_node is None: # if it's the first node
                        self.delete_head()
                    else:
                        next_node = current_node.next_node
                        prev_node.next_node = next_node
                        if next_node is None:
                            self.tail_node = prev_node
                        else:
                            next_node.prev_node = prev_node
                        self._size -= 1
                    return
                prev_node = current_node
                current_node = current_node.next_node
        raise Exception(f"{value} cannot be found in the list")

    def find_by_index(self, index):
        if index < 0 or index > self._size - 1:
            raise IndexError(f"Index {index} is out of bounds")
        counter = 0
        current_node = self.head_node
        while current_node is not None:
            if counter == index:
                return current_node.value
            current_node = current_node.next_node
            counter += 1
                
    def find_by_value(self, value):
        if self._size == 0:
            raise Exception("Cannot find a value in an empty list.")
        else:
            current_node = self.head_node
            idx = 0
            while current_node is not None:
                if current_node.value == value:
                    print(f"{value} is found at index {idx}")
                    return
                else:
                    current_node = current_node.next_node
                    idx += 1
        raise Exception(f"{value} cannot be found in the list")

    def reverse_find_by_value(self, value):
        if self._size == 0:
            raise Exception("Cannot find a value in an empty list.")
        current_node = self.tail_node
        reverse_idx = 0
        while current_node is not None:
            if current_node.value == value:
                print(f"{value} is found at index {self._size - reverse_idx - 1}")
                return
            current_node = current_node.prev_node
            reverse_idx += 1
        raise Exception("f{value} cannot be found in the list")
             
    def traverse(self):
        current_node = self.head_node
        while current_node is not None:
            print(current_node.value)
            current_node = current_node.next_node
    