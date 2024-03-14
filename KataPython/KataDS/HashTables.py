# Actually I'm Not Gonna Right Entire HashTable Class, I'm Just Gonna Use Dict in Python
# But I'm Gonna Write Some Functions That Are Used In HashTables

# HashTable is a data structure that stores key-value pairs. It uses a hash function to compute an index into an array of buckets or slots, from which the desired value can be found.
# The hash function will take a key and return an index in the hash table. The hash table will store the value at that index.

moviesRatings = {
    "Interstellar": 9.8,
    "Inception": 9.7,
    "The Dark Knight": 9.6,
    "The Prestige": 9.5
}

print(moviesRatings["Interstellar"]) # 9.8

#  Iterate Over The HashTable
for movie in moviesRatings:
    print(movie, moviesRatings[movie])

#  Get All The Keys
print(moviesRatings.keys())

# Iterate Over The Keys
for movie in moviesRatings.keys():
    print(movie)

# Check If A Key Exists
print("Interstellar" in moviesRatings) # True
print("Tenet" in moviesRatings) # False

# Count Chars In A String
def countChar(word : str):
    charCount = {}
    for i in word:
        if i in charCount:
            charCount[i] += 1
        else:
            charCount[i] = 1
    return charCount

# print(countChar("Interstellar"))

PhoneBook = {
    "Alice": {
        "name": "Alice Smith",
        "phone number": "123-456-7890",
        "email": "alice.smith@example.com"
    },
    "Bob": {
        "name": "Bob Jones",
        "phone number": "987-654-3210",
        "email": "bob.jones@example.com"
    }
}

for item in PhoneBook:
    print(item)
    for internalItem in item:
        print(internalItem)