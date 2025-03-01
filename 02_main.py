n = 25
number_of_guesses = 1

print("You have 9 chances to guess a right number")

while(number_of_guesses <= 9):
    guess = int(input("Guess a number \n"))
    if(guess < n):
        print("Choose high number")
    elif(guess > n):
        print("Choose low number")
    else:
        print("Congrats you won")
        print("You take number of guesses to guess right number",number_of_guesses)
        break
    print("Number of guesses left ",9 - number_of_guesses)
    number_of_guesses = number_of_guesses + 1

if(number_of_guesses > 9):
    print("You loose Try Again !")

