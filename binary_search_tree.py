from node import TreeNode
from queues import QueueArray

appropriate_keywords = ["print", "list", "generator"]
default_keyword = "list"

class BinarySearchTree:
    def __init__(self, value=None, node=TreeNode):
        self._Node = node
        if value is None:
            self._root = None
        else:
            self._root = self._Node(value)
    
    @property
    def root(self):
        return self._root
    
    @root.setter
    def root(self, value):
        self._root = value
        
    @property
    def min(self):
        return self.find_min().value

    @property
    def max(self):
        return self.find_max().value
    
    def _check_empty(self):
        if self.root is None:
            raise Exception("Binary search tree is empty")
    
    def _check_output_type(self, output_type):
        if not isinstance(output_type, str):
            raise TypeError(f"Invalid type: {type(output_type)} for argument. Enter relevant 'str'" +
                            "keywords from the list {appropriate_keywords}")
        elif output_type not in appropriate_keywords:
            raise Exception(f"Invalid keyword. Choose one in between the list: {appropriate_keywords}")
        
    def inorder_traversal(self, output_type="list"):
        self._check_output_type(output_type)
        self._check_empty()
        
        if output_type == "list":
            # return "[ " + " ".join(str(node) for node in self._inorder(self.root)) + " ]"
            return list(node.value for node in self._inorder(self.root))
        elif output_type == "print":
            for i in self._inorder(self.root):
                print(i.value)
        elif output_type == "generator":
            return self._inorder(self.root)
    
    def _inorder(self, node):
        if node is None:
            return
        yield from self._inorder(node.left_child)
        yield node
        yield from self._inorder(node.right_child)
    
    def preorder_traversal(self, output_type=default_keyword):
        self._check_output_type(output_type)
        self._check_empty()
        
        if output_type == "list":
            return list(self._preorder(self.root))
        else:
            for i in self._preorder(self.root):
                print(i)
    
    def _preorder(self, node):
        if node is None:
            return
        yield node.value
        yield from self._preorder(node.left_child)
        yield from self._preorder(node.right_child)
    
    def postorder_traversal(self, output_type=default_keyword):
        self._check_output_type(output_type)
        self._check_empty()
        
        if output_type == "list":
            return list(self._postorder(self.root))
        else:
            for i in self._postorder(self.root):
                print(i)
    
    def _postorder(self, node):
        if node is None:
            return
        yield from self._postorder(node.left_child)
        yield from self._postorder(node.right_child)
        yield node.value

    def levelorder_traversal(self):
        if self.root is None:
            return None
        queue = QueueArray(self.root)
        result = []
        while queue.size != 0:
            current_node = queue.dequeue()
            result.append(current_node.value)
            if current_node.left_child is not None:
                queue.enqueue(current_node.left_child)
            if current_node.right_child is not None:
                queue.enqueue(current_node.right_child)
        return result

    def insert(self, data, node=None):
        if not isinstance(data, self._Node):
            new_node = self._Node(data)
        else:
            new_node = data
        
        if self._root is None:
            self.root = new_node
        else:
            current_node = self.root if node is None else node
            if new_node.value >= current_node.value:
                if current_node.right_child is None:
                    current_node.right_child = new_node
                    new_node.parent = current_node
                    return
                else:
                    self.insert(new_node, current_node.right_child)
            else:
                if current_node.left_child is None:
                    current_node.left_child = new_node
                    new_node.parent = current_node
                    return
                else:
                    self.insert(new_node, current_node.left_child)

    def search_element(self, value, node=None):
        if not isinstance(value, self._Node):
            searched_node = self._Node(value)
        else:
            searched_node = value
        current_node = self.root if node is None else node
        
        if self._root is None:
            raise Exception("Binary search tree is empty")
        elif current_node.value == searched_node.value:
            return current_node
        else:
            if searched_node.value < current_node.value:
                if current_node.left_child is None:
                    return None
                return self.search_element(searched_node, current_node.left_child)
            else:
                if current_node.right_child is None:
                    return None
                return self.search_element(searched_node, current_node.right_child)

    def delete_node(self, value, node=None):
        if node is None:
            node = self.search_element(value, node=node)
        if node is None:
            raise Exception(f"{value} does not exist in the tree")
        
        parent_node = node.parent
        # deleting a node that has no children
        if node.left_child is None and node.right_child is None:
            if parent_node.left_child == node:
                parent_node.left_child = None
            elif parent_node.right_child == node:
                parent_node.right_child = None
        # deleting a node that has only one child
        elif node.left_child is None and node.right_child is not None:
            if parent_node.left_child == node:
                parent_node.left_child = node.right_child
            else:
                parent_node.right_child = node.right_child
        elif node.left_child is not None and node.right_child is None:
            if parent_node.left_child == node:
                parent_node.left_child = node.left_child
            else:
                parent_node.right_child = node.left_child
        # deleting a node with two children (using in order successor)
        else:
            in_order_successor = node.right_child
            while in_order_successor.left_child:
                in_order_successor = in_order_successor.left_child
            node.value = in_order_successor.value
            # now there are two nodes with the same value. when self.delete() called,       \
            # as a default value None, the search_element() method will start looking       \
            # by the root node. every time this will end up in the first occurence of the   \
            # same value. to avoid this, we can start from node.right_child but we already  \
            # have access to the real in_order_successor, so the function below in fact     \
            # will take O(1) time.
            self.delete_node(in_order_successor.value, in_order_successor)

    def find_min(self, node=None, return_value=False):
        self._check_empty()
        if node is None:
            current_node = self.root
        else:
            current_node = self.search_element(node)
        while current_node.left_child:
            current_node = current_node.left_child
        if return_value is True:
            return current_node.value
        return current_node

    def find_max(self, node=None, return_value=False):
        self._check_empty()
        if node is None:
            current_node = self.root
        else:
            current_node = self.search_element(node)
        while current_node.right_child:
            current_node = current_node.right_child
        if return_value is True:
            return current_node.value
        return current_node
    