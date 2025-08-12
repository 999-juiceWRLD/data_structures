from .linked_list import LinkedList
from .node import NodePriorityQueue

# [ front ... end ]

class QueueArray:
    def __init__(self, *args):
        self.array = []
        for arg in args:
            self.enqueue(arg)
    
    @property
    def size(self):
        return len(self.array)
    
    @property
    def front(self):
        return self.array[0] if not self.is_empty() else None

    @property
    def rear(self):
        return self.array[-1] if not self.is_empty() else None
    
    def __str__(self):
        return "[ " + " ".join(str(element) for element in self.array) + " ]"

    def __len__(self):
        return self.size

    def __getitem__(self, index):
        if index < 0:
            index += self.size
        if not 0 <= index < self.size:
            raise IndexError(f"Index {index} is out of bounds")
        else:
            return self.array[index]
    
    def enqueue(self, value):
        self.array.append(value)
    
    def dequeue(self): # O(n)
        return self.array.pop(0)

    def is_empty(self):
        return self.size == 0
    
    def clear(self):
        self.array.clear()
    
    def copy(self):
        return QueueArray(*self.array)

class LinkedQueue(LinkedList):
    def __init__(self, *values):
        super().__init__()
        for value in values:
            self.insert_tail(value)
        
    @property
    def front(self):
        return self.head_node.value if not self.is_empty() else None

    @property
    def rear(self):
        return self.tail_node.value if not self.is_empty() else None

    def enqueue(self, value): # O(1)
        self.insert_tail(value)
    
    def dequeue(self): # O(1)
        return self.delete_head()

    def is_empty(self):
        return self.size == 0

    def clear(self):
        while not self.is_empty():
            self.delete_head()

    def copy(self):
        return LinkedQueue(*self)

class CircularQueue:
    def __init__(self, *values, capacity=50):
        self.capacity = capacity
        self.array = [ None ] * self.capacity
        self.front_idx = -1
        self.rear_idx = -1
        self._size = 0
        for value in values:
            self.enqueue(value)
    
    @property
    def size(self):
        return self._size
    
    @property
    def front(self):
        return self.array[self.front_idx] if not self.is_empty() else None

    @property
    def rear(self):
        return self.array[self.rear_idx] if not self.is_empty() else None
    
    def __str__(self):
        string = "[ "
        idx = self.front_idx
        for _ in range(self.size):
            string += str(self.array[idx]) + " "
            idx = (idx + 1) % self.capacity 
        return string + "]"

    def __repr__(self):
        return (f"CircularQueue(array={self.array}, "
            f"capacity={self.capacity}, "
            f"front_idx={self.front_idx}, "
            f"rear_idx={self.rear_idx}, "
            f"size={self.size})")
    
    def __len__(self):
        return self._size

    def __getitem__(self, index):
        if index < 0:
            index += self.size
        if not 0 <= index < self.size:
            raise IndexError(f"Index {index} is out of bounds")
        else:
            physical_index = (self.front_idx + index)  % self.capacity
            return self.array[physical_index]
    
    def __iter__(self):
        for i in range(self.size):
            physical_index = (self.front_idx + i) % self.capacity
            yield self.array[physical_index]
    
    def enqueue(self, value): # manual implementation instead of using %
        if self.is_full():
            raise Exception("The circular queue is full")
        elif self.is_empty():
            self.front_idx = self.rear_idx = 0
        elif self.is_rear_idx_reached() and self.front_idx != 0:
            self.rear_idx = 0
        else:
            self.rear_idx = self.rear_idx + 1
        self.array[self.rear_idx] = value
        self._size += 1
        
    def dequeue(self):
        if self.is_empty():
            raise Exception("The circular queue is empty")
        value = self.array[self.front_idx]
        self.array[self.front_idx] = None
        self.front_idx = (self.front_idx + 1) % self.capacity
        self._size -= 1
        if self._size == 0:
            self.front_idx = -1
            self.rear_idx = -1
        return value
        
    def is_empty(self):
        return self.size == 0
    
    def is_full(self):
        return (self.rear_idx + 1) % self.capacity == self.front_idx
    
    def is_rear_idx_reached(self):
        return self.rear_idx == self.capacity - 1
    
    def clear(self):
        self.array = [ None ] * self.capacity
        self.front_idx = -1
        self.rear_idx = -1   
        self._size = 0
    
    def copy(self):
        return CircularQueue(*self, capacity=self.capacity)

class PriorityQueue(LinkedList):
    def __init__(self, value=None):
        super().__init__(value, node=NodePriorityQueue)

    @property
    def front(self):
        return self.head_node.value if not self.is_empty() else None
    
    @property
    def rear(self):
        return self.tail_node.value if not self.is_empty() else None
    
    def enqueue(self, value, priority):
        new_node = self._Node(value, priority)
        current_node = self.head_node
        prev_node = None
        
        while current_node is not None:
            if new_node.priority > current_node.priority:
                if prev_node is None:
                    self.insert_node_head(new_node)
                    return
                else:
                    prev_node.next_node = new_node
                    new_node.next_node = current_node
                    self._size += 1
                return
            elif new_node.priority == current_node.priority:
                new_node.next_node = current_node.next_node
                current_node.next_node = new_node
                self._size += 1
                return
            prev_node = current_node
            current_node = current_node.next_node
        
        if prev_node is not None:
            prev_node.next_node = new_node
            self.tail_node = new_node
        else:
            self.head_node = new_node
        self._size += 1

    def dequeue(self):
        if self.size == 0:
            raise Exception("The priority queue is empty")
        value = self.head_node.value
        self.delete_head()
        return value

    def insert_node_head(self, new_node):
        new_node.next_node = self.head_node
        self.head_node = new_node
        self._size += 1
        if self._size == 1:
            self.tail_node = new_node
    
    def is_empty(self):
        return self.size == 0

    def clear(self):
        while not self.is_empty():
            self.delete_head()
    
    def copy(self):
        new_queue = PriorityQueue()
        current_node = self.head_node
        while current_node is not None:
            new_queue.enqueue(current_node.value, current_node.priority)
            current_node = current_node.next_node
        return new_queue
