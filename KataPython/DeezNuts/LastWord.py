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




