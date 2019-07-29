# Cows and Bulls exercise
#
# Create 4-digit string, user enters 4-digit number
# - Cow = right digit right place
# - Bull = right digit wrong place
# Display cows and bulls per guess until match

import random
import string

digit_length = 4

# 0 = No Match
# 1 = Bull
# 2 = Cow
def is_cow_or_bull(digit, position, digits):
    #print("digit = %s, position = %d, digits=%s" % (digit, position, str(digits)))
    if digits[position] == digit:
        return 2
    if digit in digits:
        return 1
    return 0



# Return list of 4 digits entered by users
def enter_guess():
    while True:
        try:
            guess = input("Enter %d-digit number: " % digit_length)
        except Exception:
            # Any exceptions, including EOF
            exit(0)
        if guess == "?":
            print("Digits=%s"%str(digits))
            continue
        if not guess:
            exit(0)
        if not guess.isdigit():
            print("Must be all digits.")
            continue
        guess_list = [digit for digit in guess]
        if len(guess_list) != digit_length:
            print("Must be %d digits" % digit_length)
            continue
        return guess_list

    
if __name__ == "__main__":
    digits = random.sample(string.digits, digit_length)
    while True:
        guess = enter_guess()
        results = [0,0,0]
        index = 0
        for x in guess:
            r = is_cow_or_bull(x,index,digits)
            results[r] += 1
            index += 1

        print("Cows = %d, Bulls = %d" % (results[1], results[2]))    

        if (results[2] == digit_length):
            # All Bulls => game over!
            print("**** You guessed it - Congratulations! ****")
            exit(0)


