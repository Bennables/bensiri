number = 15
x=True

while x==True:
    guess= input("Guess A Number: ")
    if guess == "stop":
        break
    elif int(guess) == number:
        print("you got it right")
        x=False
    elif int(guess) > number:
        print("you are too high")
    elif int(guess) < number:
        print("you are too low")