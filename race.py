import turtle
import random
import time
import sys

p1wins = 0
p2wins = 0

plays = int(input("how many races would you like to see?"))

for i in range(plays):
    a = 0
    b = 0
    ben = turtle.Turtle()
    binn = turtle.Turtle()
    lines = turtle.Turtle()

    ben.shape("turtle")
    ben.penup()
    binn.penup()
    lines.speed(200)
    lines.penup()
    lines.setposition(-275,-300)
    lines.left(90)
    lines.pendown()
    lines.forward(600)
    lines.penup()
    lines.home()
    lines.right(90)
    lines.setposition(275,300)
    lines.pendown()
    lines.forward(600)

    ben.penup()
    binn.penup()
    ben.setposition(-275,100)
    binn.setposition(-275,-100)
    ben.pendown()
    binn.pendown()
    ben.speed(3)
    binn.speed(3)
    ben.color("red")
    binn.color("blue")

    first = random.randint(0,2)

    if first%2 = 0:
        x = True
        while x == True:

        dist1 = random.randint(0,10)
        dist2 = random.randint(0,10)
        ben.forward(dist1)
        binn.forward(dist2)
        a = a+dist1
        b = b+dist2

        start = time.process_time()

        if a>=550:
            ben.penup()
            ben.home()
            ben.pendown()
            ben.color("black")
            ben.write(arg = "Player 1 wins!", align="center", font=('Arial', 25))
            ben.penup()
            ben.setposition(-275,-300)
            ben.pendown()
            binn.penup()
            binn.setposition(-275,-300)
            binn.pendown()
            end = time.process_time()
            x=False
            p1wins = p1wins+1

        elif b>=550:
            binn.penup()
            binn.home()
            binn.pendown()
            binn.color("black")
            binn.write(arg = "Player 2 wins!", align="center", font=('Arial', 25))
            binn.penup()
            binn.setposition(-275,-300)
            binn.pendown()
            ben.penup()
            ben.setposition(-275,-300)
            ben.pendown()
            end = time.process_time()
            x=False
            p2wins = p2wins+1
        elif b == 550 and a == 550:
            binn.penup()
            binn.home()
            binn.pendown()
            binn.color("black")
            binn.write(arg = "Tie", align="center", font=('Arial', 25,))
            binn.penup()
            binn.setposition(-275,-300)
            binn.pendown()
            ben.penup()
            ben.setposition(-275,-300)
            ben.pendown()
            end = time.process_time()
            x=False
    elif first%2 == 1:

    
        

    
    time.sleep (4)    
    turtle.clearscreen()


lines.penup()
lines.home()
lines.pendown()
lines.write(arg = f'Player 1 won {p1wins} time(s)', align="center", font=('Arial', 25, ))
lines.penup()
lines.home()
lines.right(90)
lines.forward(30)
lines.left(90)
lines.pendown()
lines.write(arg = f'Player 2 won {p2wins} time(s)', align="center", font=('Arial', 25, ))
time.sleep(3)

    
    

