import  turtle
import random


screen = turtle.Screen()
screen.setup(800, 600)
screen.bgcolor("pink")
screen.title("черепашка")


player = turtle.Turtle()
player.shape("turtle")
player.color("green")
player.penup()
player.shapesize(3)


coin = turtle.Turtle()
coin.shape("circle")
coin.color("gold")
coin.penup()
coin.goto(150, 100)
coin.shapesize(2)

score_text = turtle.Turtle()
score_text.hideturtle()
score_text.penup()
score_text.color("black")
score_text.goto(-350, 250)
score_text.write("Очки: 0", font=("Arial", 24, "normal"))

score = 0



def up():
    player.setheading(90)
    player.forward(20)
    check_coin()

def down():
    player.setheading(270)
    player.forward(20)
    check_coin()

def left():
    player.setheading(180)
    player.forward(20)
    check_coin()

def right():
    player.setheading(0)
    player.forward(20)
    check_coin()


def check_coin():
    global score

    if player.distance(coin) < 25:
        coin.hideturtle()
        score = score + 1
        coin.goto(random.randint(-300,300),random.randint(-200,200))
        score_text.clear()
        score_text.write("Очки: " + str(score), font=("Arial", 24, "normal"))

screen.listen()
screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")


screen.mainloop()