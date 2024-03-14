""""
Linked List Node
Create a Node class that takes an integer value and a next pointer.
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.frontNode = None
        self.rearNode = None

    """enqueue(data)
    Enqueue a new node with the given data.
    """
    def enqueue(self, data):
        newNode = Node(data)
        if self.frontNode is None:
            self.frontNode = newNode
            self.rearNode = newNode
        else:
            self.rearNode.next = newNode
            self.rearNode = newNode

    """dequeue()
    Dequeue the node from the front of the queue and return its data.
    """
    def dequeue(self):
        if self.frontNode is None:
            return None
        dequeuedNode = self.frontNode
        self.frontNode = self.frontNode.next
        return dequeuedNode.data
    
    """peek()
    Return the data of the node at the front of the queue.
    """
    def peek(self):
        if self.frontNode is None:
            return None
        return self.frontNode.data

    """isEmpty()
    Return True if the queue is empty, False otherwise.
    """
    def isEmpty(self):
        return self.frontNode is None
    
    """printQueue()
    Print the queue.
    """
    def printQueue(self):
        currentNode = self.frontNode
        while currentNode is not None:
            print(currentNode.data, end=" ")
            currentNode = currentNode.next
        print(None)