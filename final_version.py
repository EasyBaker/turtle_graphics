from turtle import *
import random

bob = Turtle()
ben = Turtle()
bartosz = Turtle()
bartoleme = Turtle()
extra = Turtle()

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
    annie.color("violet")

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
    setup(500, 500)
    Screen()
    title("Turtle Keys")
    move = billbob
    showturtle()
    billbob.color("pink")
    billbob.penup()
    billbob.goto(100, 250)
    billbob.pendown()
    def up():
        billbob.fd(45)

    def left():
        billbob.lt(45)

    def right():
        billbob.rt(45)

    def back():
        billbob.bk(45)

    def quitTurtles():
        billbob.bye()

    def changeColor1():
        billbob.color("red")

    def changeColor2():
        billbob.color("orange")

    def changeColor3():
        billbob.color("yellow")

    def changeColor4():
        billbob.color("green")

    def changeColor5():
        billbob.color("blue")

    def changeColor6():
        billbob.color("indigo")

    def changeColor7():
        billbob.color("violet")

    onkey(up, "Up")
    onkey(left, "Left")
    onkey(right, "Right")
    onkey(back, "Down")
    onkey(quitTurtles, "Escape")
    onkey(changeColor1, "F1")
    onkey(changeColor2, "F2")
    onkey(changeColor3, "F3")
    onkey(changeColor4, "F4")
    onkey(changeColor5, "F5")
    onkey(changeColor6, "F6")
    onkey(changeColor7, "F7")

    listen()
    mainloop()


