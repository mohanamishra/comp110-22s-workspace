"""EX01 - Chardle - A ctue step toward Wordle."""

__author__ = "730391985"

word: str = input("Enter a 5-character word: ")
if len(word) != 5:
    print("Error: Word must contain 5 characters")
    exit()

letter: str = input("Enter a single character: ")
if len(letter) != 1:
    print("Error: Character must be a single character.")
    exit()

frequency: int = 0

print("Searching for " + letter + " in " + word)

if letter == word[0]:
    print(letter + " found at index 0")
    frequency = frequency + 1
if letter == word[1]:
    print(letter + " found at index 1")
    frequency = frequency + 1
if letter == word[2]:
    print(letter + " found at index 2")
    frequency = frequency + 1
if letter == word[3]:
    print(letter + " found at index 3")
    frequency = frequency + 1
if letter == word[4]:
    print(letter + " found at index 4")
    frequency = frequency + 1

if frequency == 0:
    print("No instances of " + letter + " found in " + word)
else:
    if frequency == 1:
        print(str(frequency) + " instance of " + letter + " found in " + word)
    else:
        print(str(frequency) + " instances of " + letter + " found in " + word)