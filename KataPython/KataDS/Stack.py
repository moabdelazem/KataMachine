""""
Linked List Node
Create a Node class that takes an integer value and a next pointer.
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

"""Stack
Create a Stack class with a head
"""
class Stack:
    def __init__(self):
        self.headNode = None
    
    """pushTo(data)
    Push a new node with the given data onto the stack.
    """
    def pushTo(self, data):
        newNode = Node(data)
        newNode.next = self.headNode
        self.headNode = newNode

    """popFrom()
    Pop the node from the top of the stack and return its data.
    """
    def popFrom(self):
        if self.headNode is None:
            return None
        poppedNode = self.headNode
        self.headNode = self.headNode.next
        return poppedNode.data

    """peek()
    Return the data of the node at the top of the stack.
    """
    def peek(self):
        if self.headNode is None:
            return None
        return self.headNode.data

    """isEmpty()
    Return True if the stack is empty, False otherwise.
    """
    def isEmpty(self):
        return self.headNode is None
    
    """printStack()
    Print the stack.
    """
    def printStack(self):
        currentNode = self.headNode
        while currentNode is not None:
            print(currentNode.data, end=" ")
            currentNode = currentNode.next
        print(None)
    