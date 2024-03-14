# Is Anagram?
def isAnagram(test, original):
    return sorted(test.lower()) == sorted(original.lower())