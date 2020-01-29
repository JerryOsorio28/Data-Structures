import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack

stack = Stack()
queue = Queue()


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def __repr__(self):
        # return f"{self.value}"
        return f"""{self.value} {self.left} {self.right}"""

    # Insert the given value into the tree
    def insert(self, value):
        # we need to create a node (or a BST)
        bst = BinarySearchTree(value)
        # if the new node is greater or equal than the current node..
        if bst.value >= self.value:
            # if it is, we check if there is a node already on the right side..
            if self.right is None:
                # if there is not, we place the new node there.
                self.right = bst
                # if there is we move to the right of the node and call the function again.
            else:
                return self.right.insert(bst.value)
        # else if the new value is less than the current node..
        else:
            # we check if there the left side of current node is empty, if it is..
            if self.left is None:
                # we make the current left side our new node.
                self.left = bst
            # if it is not empty, we want to call the function on the exisiting node on the left side.
            else:
                return self.left.insert(bst.value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        pass

    # Return the maximum value found in the tree
    def get_max(self):
        pass

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        pass

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

if __name__ == '__main__':
    bst = BinarySearchTree(5)
    bst.insert(2)
    bst.insert(3)
    bst.insert(7)
    bst.insert(6)