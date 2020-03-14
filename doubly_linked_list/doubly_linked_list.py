"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next
    
    def __repr__(self):
        return f'{self.value}'

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def __repr__(self):
        return f'{self.head}, {self.tail}'

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        #Creates a new node
        new_node = ListNode(value) 
        #Increases length by one when adding a node
        self.length += 1 
        #Checks if there is a node that represents the head or tail (if the DLL is empty)
        if not self.head and not self.tail: 
            #Set's the head to be the new node
            self.head = new_node 
            #Set's the tail to be the new node
            self.tail = new_node 
        # If there is existing nodes in the DLL...
        else:
            # Set's the new node's next node to reference to the current head
            new_node.next = self.head 
            # Set's the current head's previous to refer to the new node added
            self.head.prev = new_node
            # Set's the new node to be the new head
            self.head = new_node
        

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        # grabs value before deleting it to return it
        value = self.head.value
        # invokes the delete method to delete the head
        self.delete(self.head)
        return value



    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        #Creates a new node
        new_node = ListNode(value) 
        #Increases length by one when adding a node
        self.length += 1 
        #Checks if there is a node that represents the head or tail (if the DLL is empty)
        if not self.head and not self.tail:
            #Set's the head to be the new node
            self.head = new_node 
            #Set's the tail to be the new node
            self.tail = new_node 
        # If there is existing nodes in the DLL...
        else:
            # Set's the new node's next node to reference to the current tail
            new_node.prev = self.tail 
            # Set's the current tail's previous to refer to the new node added
            self.tail.next = new_node
            # Set's the new node to be the new tail
            self.tail = new_node

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        # grabs current value of tail to be able to return it
        value = self.tail.value
        # invokes the delete method to delete the tail
        self.delete(self.tail)
        return value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        # grabs the value of the node that we want to replace the head with
        value = node.value
        # invokes delete method to remove current head
        self.delete(node)
        # invoke add to head method to move the current node value to be the head
        self.add_to_head(value)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        # grabs the value of the node that we want to replace the tail with
        value = node.value
        # invokes delete method to remove current tail
        self.delete(node)
        # invoke add to tail method to move the current node value to be the tail
        self.add_to_tail(value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        if not self.head and not self.tail:
            return
        # shortens the length of our DLL by 1
        self.length -= 1
        # checks if there is only 1 node in our DLL and set's it to be None
        if self.head is self.tail:
            self.head = None
            self.tail = None
        # checks if there is a head, if there is, it assigns the the head's next to be the new head and removes it
        elif self.head is node:
            self.head = node.next
            node.delete()
        # checks if there is a tail, if there is, it assigns the the tail's next to be the new tail and removes it 
        elif self.tail is node:
            self.tail = node.prev
            node.delete()
        else:
            node.delete() 

        
    """Returns the highest value currently in the list"""
    def get_max(self):
        # if there is no head,return None.
        if self.head is None:
            return None
        # sets the max value to be the currents head's value 
        max_value = self.head.value
        # sets current to be the head
        current = self.head
        # while current is the head
        while current:
            # checks if currents value is greater than the max value
            if current.value > max_value:
                # if it is, then the current value will be the new max value
                max_value = current.value
            # and set's the current to be current's next... thing it as looping through it :)
            current = current.next
        return max_value

# node_list = DoublyLinkedList()
# node_list.add_to_head(10)
# node_list.add_to_head(3)
# node_list.add_to_head(6)
# node_list.add_to_head(21)
# node_list.add_to_head(8)
# node_list.add_to_head(7)
# print('newly created node_list', node_list)
# print('length', node_list)
# print('Node', ListNode(7))