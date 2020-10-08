#activity1
y=0
a=0
b=0
for sume in range(1,21):
    y = y+sume
print(y)
for summ in range(1,51):
    a = a+summ
print (a)
for smmm in range (1,101):
    b = b+smmm
print(b)

tur = True
while tur == True:
    one = int(input("Gimme Number"))
    two = int(input("Gimme Number"))
    tre = int(input("Gimme Number"))
    fou = int(input("Gimme Number"))
    if  one>two and one>tre and one>fou:
        print (one)
        answer = input("Do you want to go again? 1. Yes 2. No")
        if answer == 2:
            tur == True
        else:
            tur == False
    elif two>tre and two>one and two>fou:
        print(two)
        answer = input("Do you want to go again? 1. Yes 2. No")
        if answer == 2:
            tur == True
        else:
            tur == False
    elif tre>one and tre>two and tre>fou:
        print (tre)
        answer = input("Do you want to go again? 1. Yes 2. No")
        if answer == 2:
            tur == True
        else:
            tur == False
    else:
        print(fou)
        answer = input("Do you want to go again? 1. Yes 2. No")
        if answer == 1:
            tur == True
        else:
            tur == False
