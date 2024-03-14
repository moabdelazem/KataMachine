# Content: Function that takes a list of integers and returns True if there are any duplicates in the list, and False if there are not.
def containDups(nums: List[int]) -> bool:
    numMap = {}

    for i in nums:
        if i in numMap:
            return True
        else:
            numMap[i] = 1

    # Other solution
    # return len(nums) != len(set(nums)) 