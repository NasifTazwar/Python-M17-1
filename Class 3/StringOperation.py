# Input a word
phrase = str(input("Enter a phrase: "))

# Reverse String
# using step value as -1 to iterate in reverse
revPhrase = phrase[::-1]
phrase = revPhrase

print("Reverse of Given Phrase is:")
print(phrase)

# Convert to uppercase
upperPhrase = phrase.upper()
print("Uppercase of Given Phrase is:")
print(upperPhrase)

# Convert to lowercase
lowerPhrase = phrase.lower()
print("Lowercase of Given Phrase is:")
print(lowerPhrase)

# Find the length of the string
length = len(phrase)
print("Length of Given Phrase is:")
print(length)

# Replace spaces with hyphens
replacedPhrase = phrase.replace(" ", "-")
print("Phrase with spaces replaced by hyphens is:")
print(replacedPhrase)
