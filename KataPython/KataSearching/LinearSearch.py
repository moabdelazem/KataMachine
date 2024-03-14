# Linear Search Algorithm
# Time Complexity: O(n)

"""linearSearch(x, arr) -> int
x: int
arr: list of int
return: int
return the index of x in arr if x is in arr, otherwise return -1
"""
def linearSearch(x, arr):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1