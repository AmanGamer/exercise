n = 18

number_of_guesses=1
print("You will get only 8 chance to wirite naswer:")
while(number_of_guesses<=8):
    guess_number = int(input("\nGuess the number"))
    if guess_number<18:
            print("you chosse small number take big number:")
    elif guess_number>18:
            print("you choose big number take small number:")
    else:
        print("\nyou won")
        print("you are the winner , you win in ", number_of_guesses, "chances.")
        break
    print(8-number_of_guesses, "number of guesses left")
    number_of_guesses = number_of_guesses+1
        
    if (number_of_guesses>8):
        print("game over")
        print("Press y to try again and n to close")
        n1 = input()
        if n1==y:
            continue
        else:
            break
