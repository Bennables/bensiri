import random
cp_score = 0
your_score = 0
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
        return "a"
    elif p1 == 2 and p2 == 3:
        print("You Lose")
        return "a"
    elif p1 == 3 and p2 == 1:
        print("You Lose")
        return "a"
    elif p1 == 1 and p2 == 3:
        print("You Win")
        return "b"
    elif p1 == 2 and p2 == 1:
        print("You Win")
        return "b"
    elif p1 == 3 and p2 == 2:
        print("You Win")
        return "b"
    else:
        print("Please choose a number")
        return "c"
        

def scores(fx):
    if fx == "a":
        global cp_score
        cp_score = cp_score + 1
        return cp_score
    if fx == "b":
        global your_score
        your_score = your_score + 1
        return your_score
    if fx == "c": 
        print("Invalid Choice")
        return

def continuing(wins):
    continuee = int(input("Do you want to play again? 1. Yes 2. No"))
    if continuee == 1:
        return True
    else:
        print("Thanks for playing!")
        print(wins)
        return False

def main():
    Play = True
    rounds = 0
    your_wins = 0
    while Play == True:
        rounds = rounds+1
        print(rounds)
        CP = int(opponent())
        you = int(your_choice())
        CP_choice(CP)
        winner = game_code(CP,you)
        scores(winner)
        your_wins = your_score/rounds
        Play = continuing(your_wins)
main()