import  turtle

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
    if player.distance(coin) < 25:
        coin.hideturtle()

screen.listen()
screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")


screen.mainloop()