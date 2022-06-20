
code1 = ['F', 'A', 'I', 'R']
guess1 = ['F', 'R', 'R', 'F']

code2 = ['F', 'A', 'I', 'R']
guess2 = ['R', 'I', 'A', 'F']

code3 = ['A', 'F', 'I', 'F']
guess3 = ['F', 'A', 'A', 'F']

code4 = ['F', 'F', 'F', 'F']
guess4 = ['F', 'A', 'A', 'A']

code5 = ['A', 'F', 'F', 'F']
guess5 = ['F', 'A', 'A', 'A']


# Best case Time Complexity: O(n) since the definition is in a for loop and the best case is that it is a black pin
# Worst case Time Complexity: O(n^3) since the definition has the potential of going through a loop within a dictionary
# and then within another loop

def mastermind(code, guess):
    black = 0
    white = 0

    # This for-loop creates a hashmap/dictionary which will be used in checking for white pins
    counter = {}
    for i in range(len(code)):
        if counter.get(code[i]) is not None:
            counter.get(code[i]).append(i)
        else:
            counter[code[i]] = [i]

    # This for-loop simply checks for black pins by comparing the two spots at the same time
    for i in range(len(code)):
        if guess[i] == code[i]:
            black = black + 1

        # Because this is using an elif statement, it will not count any of the white pins alongside a black pin
        # This checks if there are any white pins by looking into the dictionary for the current digit
        # If the current digit exists in the dictionary then it will use that digit's array from the dictionary and
        # start to compare the digits of the code and the guess based on the indexes from the array
        # in order to make sure the program does not count any black pins as white pins if the current array's
        # index for both the code and the guess match
        elif counter.get(guess[i]) is not None:
            spare = counter.get(guess[i])
            for j in spare:
                if code[j] != guess[j]:
                    white = white + 1

    return black, white


print(mastermind(code1, guess1))
# (1, 2)
print(mastermind(code2, guess2))
# (0, 4)
print(mastermind(code3, guess3))
# (1, 3)
print(mastermind(code4, guess4))
# (1, 0)
print(mastermind(code5, guess5))
# (0, 6)
