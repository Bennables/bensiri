import random
def opponent():
    #1 = compost 2=recycle 3=trash
    x = random.randint(1,3)
    print (x)
    return x

def your_choice():
    you = int(input("Do you want to 1. Compost, 2. Recycle or 3. Trash: "))
    return you

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

    
def main():
    CP = int(opponent())
    you = int(your_choice())
    game_code(CP,you)
main()