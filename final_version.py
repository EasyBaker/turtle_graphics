from turtle import *
from random import randint
import random
import turtle

setup( width = 1375, height = 775, startx = None, starty = None)
screen = turtle.Screen()
bob = Turtle()
ben = Turtle()
bartosz = Turtle()
bartoleme = Turtle()
extra = Turtle()
screen.bgcolor("black")
colormode(255)

def draw_star(x, y, points, line, fill, theone):

    theone.speed(1000000)
    theone.penup()
    theone.goto(x, y)
    theone.pendown()

    theone.turn = 180 - (360 / points)

    theone.color(line, fill)

    theone.begin_fill()
    for i in range(points):
        theone.forward(200)
        theone.left(170)
    theone.end_fill()



while True:
    star_end = True
    while star_end:
        draw_star(100, 0, 36, "white", "black", bob)
        draw_star(0, 100, 36, "white", "black", ben)
        draw_star(-100, 0, 36, "white", "black", bartosz)
        draw_star(0, -100, 36, "white", "black", bartoleme)
        draw_star(0, 0, 36, "spring green", "cyan", extra)
        draw_star(100, 100, 36, "violet", "purple", bob)
        draw_star(100, -100, 36, "violet", "purple", ben)
        draw_star(-100, -100, 36, "violet", "purple", bartosz)
        draw_star(-100, 100, 36, "violet", "purple", bartoleme)
        star_end = False
    break

version = input("Would you like to control a turtle, or would you like to watch 3 random turtles walk around? Enter 'random' or 'controlled'.....")
if version == "random":
    annie = Turtle()
    anders = Turtle()
    saleem = Turtle()
    pizarro = Turtle()
    holla = Turtle()
    hump = Turtle()
    hermit = Turtle()
    crab = Turtle()
    bunny = Turtle()

    all_turtles = (annie, anders, saleem, pizarro, holla, hump, hermit, crab, bunny)
    annie.penup()
    anders.penup()
    saleem.penup()
    pizarro.penup()
    holla.penup()
    hump.penup()
    hermit.penup()
    crab.penup()
    bunny.penup()
    annie.goto(100, 10)
    anders.goto(100, 10)
    saleem.goto(100, 10)
    pizarro.goto(100, 10)
    holla.goto(100, 10)
    hump.goto(100, 10)
    hermit.goto(100, 10)
    crab.goto(100, 10)
    bunny.goto(100, 10)
    annie.pendown()
    anders.pendown()
    saleem.pendown()
    pizarro.pendown()
    holla.pendown()
    hump.pendown()
    hermit.pendown()
    crab.pendown()
    bunny.pendown()

    annie.pensize(10)
    anders.pensize(10)
    saleem.pensize(10)
    pizarro.pensize(10)
    holla.pensize(10)
    hump.pensize(10)
    hermit.pensize(10)
    crab.pensize(10)
    bunny.pensize(10)

    annie.shape("turtle")
    annie.pencolor("violet")

    anders.shape("turtle")
    anders.color("purple")

    saleem.shape("turtle")
    saleem.color("violet")

    pizarro.shape("turtle")
    pizarro.color("purple")

    holla.shape("turtle")
    holla.color("violet")

    hump.shape("turtle")
    hump.color("violet")

    hermit.shape("turtle")
    hermit.color("purple")

    crab.shape("turtle")
    crab.color("purple")

    bunny.color("cyan")

    
    ben.forward(10)
    bob.left(90)
    bob.forward(10)
    bartosz.left(180)
    bartosz.forward(10)
    bartoleme.left(270)
    bartoleme.forward(10)
    holla.left(45)
    holla.forward(10)
    hump.left(135)
    hump.forward(10)
    hermit.right(45)
    hermit.forward(10)
    crab.right(135)
    crab.forward(10)

    while True:
        for t in all_turtles:
            rand_dir = random.randint(-30, 30)
            rand_dist = random.randint(5, 10)

            t.right(rand_dir)
            t.forward(rand_dist)

elif version == "controlled":
    billbob = Turtle()
    benten = Turtle()
    setup(500, 500)
    Screen()
    title("Turtle Keys")
    move = billbob
    showturtle()
    billbob.color("pink")
    billbob.penup()
    billbob.goto(100, 250)
    billbob.pendown()
    billbob.width(10)

    def up():
        billbob.fd(45)

    def left():
        billbob.lt(45)

    def right():
        billbob.rt(45)

    def back():
        billbob.bk(45)

    def changeColor1():
        billbob.color(255, 0, 0)
        
    def changeColor2():
        billbob.color(	255, 140, 0)

    def changeColor3():
        billbob.color(255, 255, 0)

    def changeColor4():
        billbob.color(127, 255, 0)

    def changeColor5():
        billbob.color(0, 0, 255)

    def changeColor6():
        billbob.color(138, 43, 226)

    def changeColor7():
        billbob.color(153, 50, 204)

    def changeColor8():
        billbob.color(0, 255, 255)

    def changeColor9():
        billbob.color(	255, 20, 147)

    def changeColor10():
        billbob.color(	176, 224, 230)

    def changeColor11():
        billbob.color(205, 201, 201)

    def changeColor12():
        billbob.color(49, 79, 79)

    def draw_square():
        billbob.color("red")
        billbob.forward(100)
        billbob.right(90)
        billbob.forward(100)
        billbob.back(100)
        billbob.left(90)
        billbob.back(200)
        billbob.left(90)
        billbob.forward(100)
        billbob.back(100)
        billbob.right(90)
        billbob.forward(100)
        billbob.left(90)
        billbob.forward(100)
        billbob.right(90)
        billbob.forward(100)
        billbob.back(100)
        billbob.right(90)
        billbob.forward(200)
        billbob.right(90)
        billbob.forward(100)

    def draw_star():
        x = 1
        billbob.width(1)
        billbob.speed(9000)
        while x < 200:
            r = randint(0,255)
            g = randint(0,255)
            b = randint(0,255)

            colormode(255)

            pencolor(r,g,b)

            billbob.color(r, g, b)
            billbob.fd(50 + x)
            billbob.rt(90.911)

            x = x+1
            
    def draw_twirly_wirly():
          billbob.width(1)
          billbob.pencolor("white")
          x = 0
          billbob.penup()

          billbob.rt(45)
          billbob.fd(90)
          billbob.rt(135)

          billbob.pendown()
          billbob.speed(9000)
          while x < 120:
                billbob.fd(200)     
                billbob.rt(61)
                billbob.fd(200)
                billbob.rt(61)
                billbob.fd(200)
                billbob.rt(61)
                billbob.fd(200)
                billbob.rt(61)
                billbob.fd(200)
                billbob.rt(61)
                billbob.fd(200)
                billbob.rt(61)

                billbob.rt(11.1111)

                x = x + 1

    onkey(up, "Up")
    onkey(left, "Left")
    onkey(right, "Right")
    onkey(back, "Down")
    onkey(changeColor1, "F1")
    onkey(changeColor2, "F2")
    onkey(changeColor3, "F3")
    onkey(changeColor4, "F4")
    onkey(changeColor5, "F5")
    onkey(changeColor6, "F6")
    onkey(changeColor7, "F7")
    onkey(changeColor8, "F8")
    onkey(changeColor9, "F9")
    onkey(changeColor10, "F10")
    onkey(changeColor11, "F11")
    onkey(changeColor12, "F12")
    onkey(draw_square, "Tab")
    onkey(draw_star, "Delete")
    onkey(draw_twirly_wirly, "Insert")
    listen()
    mainloop()


