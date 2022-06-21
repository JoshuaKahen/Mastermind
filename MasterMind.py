# Test cases


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

    # This for-loop checks for black pins by comparing the two spots at the same time
    # This for-loop then removes those pins from the index of the array in the hashmap/dictionary
    for i in range(len(code)):
        if guess[i] == code[i]:
            black = black + 1
            counter.get(code[i]).remove(i)

    # This for-loop checks for white pins by checking if the digit is in the hashmap/dictionary and making sure
    # that the current index in the guess and code are not the same
    # It then adds the length of the array from the hashmap/dictionary based on the digit to the overall count
    for i in range(len(code)):
        if (counter.get(guess[i]) is not None) and (guess[i] != code[i]):
            white = white + len(counter.get(guess[i]))

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
