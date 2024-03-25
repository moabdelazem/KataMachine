# Some Problem Solving
def lastWordLength(s: str) -> int:
    return len(s.split()[-1])

def plusOne(numbersList : list[int]) -> list[int]:
    myStringOfNumbers = ""
    for i in numbersList:
        stringNumber = str(i)
        myStringOfNumbers += stringNumber
    
    mainList = int(myStringOfNumbers) + 1

    numsList = []
    for i in str(mainList):
        numsList.append(int(i))

    return numsList


def searchInsertPosition(nums: list[int], target: int) -> int:
    if target in nums:
        return nums.index(target)
    else:
        nums.append(target)
        nums.sort()
        return nums.index(target) 


def addBinary(a: str, b: str) -> str:
    return bin(int(a, 2) + int(b, 2))[2:]