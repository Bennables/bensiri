import random
def opponent():
    #1 = compost 2=recycle 3=trash
    x = random.randint(1,3)
    return x

def your_choice():
    you = int(input("Do you want to 1. Compost, 2. Recycle or 3. Trash: "))
    return you

def CP_choice(cpu):
    if cpu == 1:
        print("CP chose compost")
    if cpu == 2:
        print("CP chose recycle")
    if cpu == 3:
        print("CP chose trash")

def game_code(p1,p2):
    if p1 == p2:
        print("draw")
    elif p1 == 1 and p2 == 2:
        print("You Lose")
    elif p1 == 2 and p2 == 3:
        print("You Lose")
    elif p1 == 3 and p2 == 1:
        print("You Lose")
    elif p1 == 1 and p2 == 3:
        print("You Win")
    elif p1 == 2 and p2 == 1:
        print("You Win")
    elif p1 == 3 and p2 == 2:
        print("You Win")
    else:
        print("Please choose a number")
    
def streaks():

def continuing():
    continuee = int(input("Do you want to play again? 1. Yes 2. No"))
    if continuee == 1:
        return True
    else:
        return False

    
def main():
    Play = True
    your_score = 0
    cp_score = 0
    while Play == True:
        CP = int(opponent())
        you = int(your_choice())
        CP_choice(CP)
        game_code(CP,you)
        Play = continuing()
main()