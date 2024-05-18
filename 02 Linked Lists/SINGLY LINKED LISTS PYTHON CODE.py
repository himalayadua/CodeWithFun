class ListNode:

    # self is a reference to the instance of the class
    # used to access the attributes and methods of the object within the class

    # __init__ is a special method in Python classes, also known as the constructor. 
    # It is automatically called when an object is created from the class. 
    # The purpose of __init__ is to initialize the object's attributes and perform any necessary setup.
    def __init__(self, val):
        self.val = val
        self.next = None

# Implementation for Singly Linked List
class LinkedList:
    def __init__(self):
        # Init the list with a 'dummy' node which makes 
        # removing a node from the beginning of list easier.
        self.head = ListNode(-1)
        self.tail = self.head
    
    def insertEnd(self, val):
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def remove(self, index):
        i = 0
        curr = self.head
        while i < index and curr:
            i += 1
            curr = curr.next
        
        # Remove the node ahead of curr
        if curr:
            curr.next = curr.next.next

    def print(self):
        curr = self.head.next
        while curr:
            print(curr.val, ' -> ')
            curr = curr.next
        print()