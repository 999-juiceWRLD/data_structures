# Implementation of Data Structures

This repo contains implementations of various data structures. Each article lists the implemented features.

## Linked List & Doubly Linked List Common Methods

- `insert_head()`: insert a new element to the head of the list.
- `insert_tail()`: same but to the end of the list.
- `delete_head()`: delete the first element.
- `delete_tail()`: delete the last element.
- `delete_index()`: delete the element from a given index. index is checked if it's within the bounds.
- `find_by_index()`: returns the value where the index at. index is checked if it's within the bounds.
- `traverse()`: print each value in the list.

### Linked List

- `insert_index()`: insert to element to a given index. index is checked if it's within the bounds.

### Doubly Linked List

- `find_by_value()`: find the first occurence of a value in the list.
- `reverse_find_by_value()`: find the last occurence of a value in the list.

## Stacks (Array Stack & Linked Stack)

- `size`: returns the size of the stack
- `top`: returns the topmost element
- `push()`: add a new element to the topmost position in the stack
- `pop()`: remove the topmost element
- `peek()`: return the topmost element without removing it from the stack
- `is_empty()`: return `True` if the stack is empty else `False`
- `clear()`: remove all the elements of the stack
- `copy()`: duplicate the stack without sharing the underlying list

## Queues (Array Queue, Linked Queue, Circular Queue, Priority Queue)

- `size`: returns the size of the queue
- `front`: returns the first element in the queue
- `rear`: returns the last element in the queue
- `enqueue()`: adds the element to the queue
- `dequeue()`: removes element from the queue
- `is_empty()`: returns `True` if the queue is empty else `False`
- `clear()`: remove all the elements of the queue
- `copy()`: returns a deep copy of the queue

### Circular Queue

- `is_full()`: return `True` if the array is full else `False`
- `is_rear_idx_reached()`: return `True` if the rear index reached to the final index (`len(self.array) - 1`)

### Priority Queue

- `insert_node_head()`: instead of entering just the value (data), this method takes `PriorityQueueNode` object as parameter and inserts it at the head of the list

## Binary Search Tree

- `root`: return the root value
- `min`: return the minimum value, using `find_min()` internally
- `max`: return the maximum value, using `find_max()` internally
- `inorder_traversal`: traverse the tree in-order
- `preorder_traversal`: traverse the tree pre-order
- `postorder_traversal`: traverse the tree post-order
- `levelorder_traversal`: traverse each level using `QueueArray`
- `insert()`: insert a new node into the tree
- `search_element()`: search for an element and return `self._Node` else `None`
- `delete_node()`: delete an element from the tree. raise `Exception` if the tree is empty
- `find_min()`: return the node of the minimum value. if `return_value=True`, return the value of the node
- `find_max()`: return the node of the maximum value. if `return_value=True`, return the value of the node

### **To Do's**
- Index'li fonksiyonlara `index += length` diyerek negatif index ekleme özelliği
- `__repr__` fonksiyonu ekle?
- Linked list'lere raise error testi ekle
- Arama metodlarıda `print()` yerine `Node` döndürme?
- Doubly linked list için `insert_index()` metodu ekle.