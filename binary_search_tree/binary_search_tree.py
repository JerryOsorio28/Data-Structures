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
        return f"{self.value}"

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
        # we check if the target is equal to the current value if it is...
        if target == self.value:
            # we return
            return True
        # we check if the target value is greater than the current value, if it is...
        if target > self.value:
            # we check if there is anything on the right side of the current value..
            if self.right is None:
            # if there is not, we need to return an error saying there is no value equal to target
                return False
            # if there is, we call the function recursively on the right node of the current value
            else:
                return self.right.contains(target)
        # if it is less than the current value
        else:
            # we check if there is anything on the left side of the current value...
            if self.left is None:
                # if there is not, we need to return an error saying there is no value equal to target
                return False
            # if there is, we call the function recursively on the left node of the current value
            else:
                return self.left.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # we check if there is anything on the right side of the current node, if it is not...
        if self.right is None:
            # we return the current node
            return self.value
        # else, we call the function recursively on the current's right node.
        else:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # The 'CB' means all the methods you can use within the Binary Search Tree class.
        cb(self.value)
        # so whenever the right side of our current node is NOT empty...
        if self.right is not None:
            # we call our for each function recursively with any other method within our class.
            self.right.for_each(cb)
        # we would also need to check the same thing for the left side as well.
        if self.left is not None:
            self.left.for_each(cb)


    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass
        # For depth-first problems, we need to use a Stack.
        # Rules of a queue is FILO
        # first we need to check if there is anything on the left side of the current node, if there isn't...
            # we check if there is anything on the right side of the current node, if there isn't...
                # we need to call the function on the previous n
            # if there is..
                # we want to print the current node
                # we want to call the function recursively on that node
        # if there is something on the left side...
                # we want to print the current node
                # we want to call the function recursively on that node
        

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # For breadth-first problems, we need to use a Queue.
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # For depth-first problems, we need to use a Stack.
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
    bst = BinarySearchTree(4)
    bst.insert(2)
    bst.insert(3)
    bst.insert(7)
    bst.insert(6)
    print(bst)
    bst.in_order_print(bst)