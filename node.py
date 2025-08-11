class NodeCore:
    def __init__(self, value, next_node=None):
        self._value = value
        self._next_node = next_node
        
    @property
    def value(self):
        return self._value
    
    @property
    def next_node(self):
        return self._next_node

    @next_node.setter
    def next_node(self, value):
        self._next_node = value

class NodePriorityQueue(NodeCore):
    def __init__(self, value, priority=None, next_node=None):
        super().__init__(value, next_node)
        self.priority = priority

class TreeNode:
    def __init__(self, value=None, left_child=None, right_child=None, parent=None):
        self._value = value
        self._left_child = left_child
        self._right_child = right_child
        self._parent = parent
        
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        self._value = value
    
    @property
    def left_child(self):
        return self._left_child
    
    @left_child.setter
    def left_child(self, left_child):
        self._left_child = left_child
        
    @property
    def right_child(self):
        return self._right_child
    
    @right_child.setter
    def right_child(self, right_child):
        self._right_child = right_child
    
    @property
    def left_value(self):
        return self._left_child.value if self._left_child else None
    
    @property
    def right_value(self):
        return self._right_child.value if self._right_child else None
    
    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, parent):
        self._parent = parent