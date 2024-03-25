""""
Linked List Node
Create a Node class that takes an integer value and a next pointer.
"""
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next 

"""LinkedList
Create a LinkedList class with a headNode and methods to insert a node at the head of the list and at the end of the list.
"""
class LinkedList:
    def __init__(self):
        self.headNode = None

    """InsetNode(data)
    Insert a new node with the given data at the head of the list.
    """
    def insertNode(self, data):
            newNode = Node(data)
            newNode.next = self.headNode
            self.headNode = newNode

    """InsertLastNode(data)
    Insert a new node with the given data at the end of the list.
    """
    def insertLastNode(self, data):
        newNode = Node(data)
        if self.headNode is None:
            self.headNode = newNode
            return
        
        currentNode = self.headNode
        while currentNode.next is not None:
            currentNode = currentNode.next

        currentNode.next = newNode

    """findNode(data)
    Find a node with the given data in the list. Return True if found, False otherwise.
    """
    def findNode(self, nodeData):
        currentNode = self.headNode
        while currentNode is not None:
            if currentNode.data == nodeData:
                return currentNode 
            currentNode = currentNode.next
        return None

    """findNodeParent(data)
    Find the parent of a node with the given data in the list. Return the parent node if found, None otherwise.
    """
    def findNodeParent(self, data):
        currentNode = self.headNode
        while currentNode is not None:
            if currentNode.next.data == data:
                return currentNode
            currentNode = currentNode.next
        return None
    
    """deleteNode(data)
    Delete a node with the given data from the list.
    """
    def deleteNode(self, data):
        if self.headNode is None:
            return
        if self.headNode.data == data:
            self.headNode = self.headNode.next
            return
        prevNode = self.findNodeParent(data)
        if prevNode is None:
            return
        prevNode.next = prevNode.next.next

    
    """insertAfterNode(prevNode, data)
    Insert a new node with the given data after the given node.
    """
    def insertAfterNode(self, prevNode, data):
        currentNode = self.findNode(prevNode)
        if currentNode is None:
            return
        newNode = Node(data)
        newNode.next = currentNode.next
        currentNode.next = newNode

    """PrintList()
    Print the list.
    Warning: This method is for testing purposes only. It will not be included in the tests.
    """
    def printList(self):
        currentNode = self.headNode
        while currentNode is not None:
            print(currentNode.data, end=" -> ")
            currentNode = currentNode.next
        print("None")
    
    """getListLength()
    Return the length of the list.
    """
    def getListLength(self):
        currentNode = self.headNode
        length = 0
        while currentNode is not None:
            length += 1
            currentNode = currentNode.next
        return length
