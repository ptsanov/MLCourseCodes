import math

def guessTheNum (first, last):
    tries = 1
    while first <= last:
        center_value = first + ((last - first) // 2)
        ans = input('Is it your number {}?\n[y/n] '. format(center_value))
        if ans in ["Y", "y"]:
            return print ("Congrats! I guessed from {} try!". format(tries))
            break
        elif ans in ["N", "n"]:
            ans = input('Is it bigger than {}?\n[y/n] '. format(center_value))
            if ans in ["Y", "y"]:
                first = center_value + 1
                tries += 1
            elif ans in ["N", "n"]:
                last = center_value - 1
                tries += 1
            else:
                print("Wrong input! Try again!")
        else:
            print("Wrong input! Try again!")
    return print ("You have mistake! Check your answers!")

print ("Welcome to the 'Guess the number' game!\nYou can use 'Y' or 'y' for YES and 'N' or 'n' NO answers!")
first = int(input("Enter the Start of the interval: "))
last = int(input("Enter the End of the interval: "))
guesses = math.ceil(math.log2(last))
print ("Think of a number between {} - {} ! I will guess it for maximum {} guesses!". format(first, last, guesses))
print(guessTheNum(first, last))