# Binary Search Algorithm
# Time Complexity: O(log n)

"""binarySearch(x, arr) -> int
x: int
arr: list of int
return: int
return the index of x in arr if x is in arr, otherwise return -1
"""

def binarySearch(x, arr):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid