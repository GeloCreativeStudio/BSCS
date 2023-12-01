# 1. Create an empty list named 'letters'
letters = []

# 2. Append all small letter vowels in order
vowels = ["a", "e", "i", "o", "u"]
letters.extend(vowels)

# 3. Add a capital consonant after the third vowel
letters.insert(3, "B")  # Example capital consonant B

# 4. Print the position of the last vowel
print(
    "Position of the last vowel:", len(letters) - 1
)  # Vowels were last, so position is length - 1

# 5. Arrange the list so that the capital consonant is at the end of the list
letters.append(letters.pop(3))

# 6. Print the value that is in the 5th position
print("Value in the 5th position:", letters[4])

# 7. Create another list named 'alphanum' with integers 6, 7, 8, 9, and 0 as the elements
alphanum = [6, 7, 8, 9, 0]

# 8. Append the values of every odd indices of 'letters' into 'alphanum'
alphanum.extend(letters[1::2])  # Get every odd index (1, 3, 5, ...)

# 9. Print all the list
print("letters:", letters)
print("alphanum:", alphanum)
