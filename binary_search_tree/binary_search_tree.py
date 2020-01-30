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
        # we check if there is anything on the right side of the current node, if it is not, we return the current node..
        # else, we call the function recursively on the current's right node.
        return self.value if self.right == None else self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # The 'CB' means all the methods you can use within the Binary Search Tree class.
        cb(self.value)
        # so whenever the right side of our current node is NOT empty...
        if self.right:
            # we call our for each function recursively with any other method within our class.
            self.right.for_each(cb)
        # we would also need to check the same thing for the left side as well.
        if self.left:
            self.left.for_each(cb)


    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # For depth-first problems, we need to use a Stack.
        # Rules of a stack is FILO
        # first we need to check if there is anything on the left side of the current node
        if node.left:
            #if there is, we want to call the function recursively on that node
            node.left.in_order_print(node.left)
        # we want to print the current node
        print(node)
        if node.right:
            #if there is, we want to call the function recursively on that node
            node.right.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # For depth-first problems, we need to use a queue.
        # Rules of a queue is FILO
        # Make the queue
        queue = Queue()
        # we add the root to the queue
        queue.enqueue(node)
        # while there is values in the queue
        while queue.size > 0:
            # we dequeue the root out of the queue ans save it in temp
            temp = queue.dequeue()
            # we check if there is anything on the left side of the current node, if there is...
            if temp.left:
                # add to the queue
                queue.enqueue(temp.left)
            # we check if there is anything on the right side of the current node, if there is...
            if temp.right:
                # add to the queue
                queue.enqueue(temp.right)
            # we print the current node
            print(temp)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # For depth-first problems, we need to use a Stack.
        # Rules of a Stack is FILO
        # Make the stack
        stack = Stack()
        # we add the root to the stack
        stack.push(node)
        # while there is values in the stack
        while stack.size > 0:
            # we pop the root out of the stack ans save it in temp
            temp = stack.pop()
            # we print the current node
            print(temp)
            # we check if there is anything on the left side of the current node, if there is...
            if temp.left:
                # add to the stack
                stack.push(temp.left)
            # we check if there is anything on the right side of the current node, if there is...
            if temp.right:
                # add to the stack
                stack.push(temp.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        if node is None:
            return
        print(node)
        # we check if left of node, if there is a node...
        if node.left:
            # before we move left, we print the current node
            # we call recursion in that node..
            node.left.pre_order_dft(node.left)
        # we check if right of node, if there is a node...
        if node.right: 
            # we call recursion in that node..
            node.right.pre_order_dft(node.right)
        

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

if __name__ == '__main__':
    bst = BinarySearchTree(1)
    bst.insert(8)
    bst.insert(5)
    bst.insert(7)
    bst.insert(6)
    bst.insert(3)
    bst.insert(4)
    bst.insert(2)
    bst.pre_order_dft(bst)