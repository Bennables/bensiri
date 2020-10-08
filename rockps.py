continu = True
while continu == True:

    p1 = int(input("1. Rock, 2. Paper, or 3. Scissors"))
    p2 = int(input("1. Rock, 2. Paper, or 3. Scissors"))
    if p1 == p2:
        print("draw")
    elif p1 == 1 and p2 == 2:
        print("p2 wins")
    elif p1 == 2 and p2 == 3:
        print("p2 wins")
    elif p1 == 3 and p2 == 1:
        print("p2 wins")
    elif p1 == 1 and p2 == 3:
        print("p1 wins")
    elif p1 == 2 and p2 == 1:
        print("p1 wins")
    else:
        print("p1 wins")

    again = int(input("Play again? 1. Yes, 2. No"))
    if again == 1:
        continu = True
    else: 
        continu = False
        print("thanks for playing.")