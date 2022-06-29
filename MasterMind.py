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


num = int(input("What is the amount of digits in the code?\n"))
inpcode = []
inpguess = []
for i in range(num):
    inp = input("Please enter a single digit for spot #" + str(i + 1) + " in the secret code\n")
    inpcode.append(inp)

for i in range(num):
    inp = input("Please enter a single digit for spot #" + str(i + 1) + " in the guess\n")
    inpguess.append(inp)

print(mastermind(inpcode, inpguess))

