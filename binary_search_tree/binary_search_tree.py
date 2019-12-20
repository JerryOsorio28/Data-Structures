import sys
sys.path.append('./queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return f'{self.value}'

    # Insert the given value into the tree
    def insert(self, value):

        #if value is less than self.value(root), make new tree node if empty, else keep going (recursion)
        if value < self.value and self.left is None:
            new_node = BinarySearchTree(value)
            self.left = new_node
        elif value < self.value and self.left is not None:
            self.left.insert(value)
        # if value is greater than self.value(root), make a new tree node if empty, else keep going(recursion)
        elif value >= self.value and self.right is None:
            new_node = BinarySearchTree(value)
            self.right = new_node
        elif value >= self.value and self.right is not None:
            self.right.insert(value)
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
    #If the target == self.value, return it
    #else go left/right based on smaller or bigger
        if target is self.value:
            return True
        elif target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        elif target >= self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)


    # Return the maximum value found in the tree
    def get_max(self):
    #check always if next to the right side of the node there's another one, if not, return it (always go right)
        if self.right is not None:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.left is not None:
            self.left.for_each(cb)
        if self.right is not None:
            self.right.for_each(cb)
    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        #when node == None, return it. 
        if node is None:
            return
        #checks if there's a node on the left, if so...
        if self.left is not None:
            #run's recursive function again
            self.left.in_order_print(node)
        print(self.value)
        #checks if there's a node on the right, if so... 
        if self.right is not None:
            #run's recursive function again
            self.right.in_order_print(node)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):

        new_stack = Stack()
        

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
