# from KataDS.LinkedList import LinkedList
# from KataDS.Stack import Stack
from KataSearching.LinearSearch import linearSearch
from KataSearching.BinarySearch import binarySearch 
from KataSorting.InsertionSort import insertionSort
# # Create a LinkedList
# ll = LinkedList()
# ll.insertNode(1)
# ll.insertNode(2)
# ll.insertNode(3)
# ll.insertLastNode(4)
# ll.insertLastNode(5)

# ll.printList()

# ll.deleteNode(3)
# ll.deleteNode(5)
# ll.deleteNode(1)
# ll.printList()

# ll.insertAfterNode(2, 6)
# ll.insertAfterNode(4, 7)
# ll.insertAfterNode(6, 8)

# ll.printList()

# # Test Stack
# s = Stack()
# s.pushTo(1)
# s.pushTo(2)
# s.pushTo(3)
# s.pushTo(4)
# s.pushTo(5)

# s.printStack()

# s.popFrom()
# s.printStack()


# Test Linear Search
arr = [1, 2, 3, 4, 5]
x = 3
print(linearSearch(x, arr)) # 2

# Test Binary Search
arr = [1, 2, 3, 4, 5]
x = 3
print(binarySearch(x, arr)) # 2

unsortedArr = [9, 5, 4, 1]
insertionSort(unsortedArr)
print(unsortedArr)