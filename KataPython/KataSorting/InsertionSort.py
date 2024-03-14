# Insertion Sort Algorithm
""" 
    Pseudocode:
    1. Iterate from arr[1] to arr[n] over the array.
    2. Compare the current element (key) to its predecessor.
    3. If the key element is smaller than its predecessor, compare it to the elements before.
    Move the greater elements one position up to make space for the swapped element.

    1- x = [], key = 0
    2- read x
    3- for i =1 forward i < x.length
        3.1- key = x[i]
        3.2- for j = i - 1 backward j >= 0
        3.3- if key < x[j] then x[j+1] = x[j]
    4- x[j + 1] = key
"""
"""InsertionSort
Time Complexity: O(n^2)
"""
def insertionSort(arr):
    for i in range(1, len(arr)):
        key  = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key