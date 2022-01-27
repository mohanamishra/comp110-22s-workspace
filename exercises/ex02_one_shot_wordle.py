"""EX02 - One shot wordle."""

__author__ = "730391985"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

secret: str = "python"
guess: str = input("What is your " + str(len(secret)) + "-letter guess? ")

i: int = 0
emoji: str = ""

while len(guess) != len(secret):  # if guess is not correct length
    guess = input("That was not " + str(len(secret)) + " letters! Try again: ")

while i < len(secret): 
    if guess[i] == secret[i]:
        emoji += GREEN_BOX
    else:  # checks for yellow or white box
        exists_elsewhere: bool = False
        alt_idx: int = 0
        while not exists_elsewhere and alt_idx < len(secret):
            if guess[i] == secret[alt_idx]:
                exists_elsewhere = True
            else:
                alt_index = alt_idx + 1

        if exists_elsewhere:
            emoji += YELLOW_BOX
        else:
            emoji += WHITE_BOX

    i += 1

print(emoji)

if guess != secret:
    print("Not quite. Play again soon!")
    exit()

if guess == secret:
    print("Woo! You got it!")
    exit()
