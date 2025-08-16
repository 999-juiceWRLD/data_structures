# Implementation of Data Structures

This repo contains implementations of various data structures. Each article lists the implemented features. Currently trying to make this a fully functioning library where you can basically use implemented data structures as-intended. I will implement AVL & red-black trees, and hopefully graphs.

You can see the generated document with pdoc [here](https://999-juicewrld.github.io/data_structures/data_structures.html).

## Linked List & Doubly Linked List Common Methods

- `insert_head()`: insert a new element to the head of the list.
- `insert_tail()`: same but to the end of the list.
- `delete_head()`: delete the first element.
- `delete_tail()`: delete the last element.
- `delete_index()`: delete the element from a given index. index is checked if it's within the bounds.
- `delete_value(value)`: delete the first occurence of the value.
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
- `size`: return the number of nodes in the tree
- `is_empty`: return `True` if root is None else `False`
- `inorder_traversal(output_type=default_keyword)`: traverse the tree in-order. as default returns a list
- `preorder_traversal(output_type=default_keyword)`: traverse the tree pre-order. as default returns a list
- `postorder_traversal(output_type=default_keyword)`: traverse the tree post-order. as default returns a list
- `levelorder_traversal()`: traverse each level using `QueueArray`
- `insert(data, node=None)`: insert a new node into the tree
- `search_element(value, node=None)`: search for an element and return `self._Node` else `None`
- `delete_node(value, node=None)`: delete an element from the tree. raise `Exception` if the tree is empty
- `find_min(node=None, return_value=False)`: return the node of the minimum value. if `return_value=True`, return the value of the node
- `find_max(node=None, return_value=False)`: return the node of the maximum value. if `return_value=True`, return the value of the node
- `height(opt_node=None)`: return the height of the tree. if `opt_node` is `self._Node` object, then treat that object as the root node, therefore return the subtree height
- `get_size()`: compute the number of nodes recursively.
- `clear()`: clear the tree
- `copy(method="recursive")`: deep copy the instance and return. if `method="iterative"` use iterative internal function.
- `is_balanced(node=None)`: return `True` if the height of the node parameter is balanced, or `False`. if `node=None` checks for the root node.
