import sys
import turtle


# Drawing Windw For Game
windw = turtle.Screen()
windw.cv._rootwindow.resizable(True, True)
windw.title("Ping Pong Game")
windw.bgcolor("white")
windw.setup(width=800, height=600)
windw.tracer(0)

#### drowind tool game ###
# First Racket
racket_1 = turtle.Turtle()
racket_1.speed(0)
racket_1.shape("square")
racket_1.shapesize(stretch_len=.4, stretch_wid=5)
racket_1.color("blue")
racket_1.penup()
racket_1.goto(370, 0)

# Second Racket
racket_2 = turtle.Turtle()
racket_2.speed(0)
racket_2.shape("square")
racket_2.shapesize(stretch_len=.4, stretch_wid=5)
racket_2.color("red")
racket_2.penup()
racket_2.goto(-370, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("black")
ball.penup()
ball.goto(0, 0)
ball.dx = .22
ball.dy = .22

# Score
score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)
score.color('#D3D3D3', '#a0c8f0')
score.penup()
score.hideturtle()
score.goto(0, 0)
score.write("0  |  0" , align="center" , font=("ubuntu",100 ,"normal"))


#### functions to app ####
# fun move to racket 1
def racket_1_up():      # Up
    if racket_1.ycor() != 300:
        y = racket_1.ycor()
        y += 60
        racket_1.sety(y)

def racket_1_down():    # Down
    if racket_1.ycor() != -300 :
        y = racket_1.ycor()
        y -= 60
        racket_1.sety(y)


def racket_1_on():      # Left
    if racket_1.xcor() > 100:
        x = racket_1.xcor()
        x -= 30
        racket_1.setx(x)

def racket_1_out():      # Right
    if racket_1.xcor() < 370:
        x = racket_1.xcor()
        x += 30
        racket_1.setx(x)


# fun move to racket 2

def racket_2_up():
    if racket_2.ycor() != 300:
        y = racket_2.ycor()
        y += 60
        racket_2.sety(y)

# fun down to racket 2
def racket_2_down():
    if racket_2.ycor() != -300:
        y = racket_2.ycor()
        y -= 60
        racket_2.sety(y)

def racket_2_on():      # Left
    if racket_2.xcor() < -100:
        x = racket_2.xcor()
        x += 30
        racket_2.setx(x)

def racket_2_out():      # Right
    if racket_2.xcor() > -370:
        x = racket_2.xcor()
        x -= 30
        racket_2.setx(x)


#### keyboard control ####

windw.listen() #listen keyboard press
windw.onkeypress(racket_1_up, "Up")
windw.onkeypress(racket_1_down, "Down")
windw.onkeypress(racket_1_on, "Left")
windw.onkeypress(racket_1_out, "Right")
windw.onkeypress(racket_2_up, "w")
windw.onkeypress(racket_2_down, "s")
windw.onkeypress(racket_2_on, "d")
windw.onkeypress(racket_2_out, "a")


# main loop window
while True:
    windw.update()

    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    ### set bolder limit ###
    # The horizontal plane to ball
    if ball.ycor() >290:
        ball.sety(290)
        ball.dy *=  -1

    if ball.ycor() <-290:
        ball.sety(-290)
        ball.dy *=  -1

    # The vertical plane to ball
    if ball.xcor() >390 : #ball out right border
        ball.goto(0, 0)
        ball.dx *= -1
        score1 += 1
        score.clear()
        score.write("{}  |  {}".format(score1, score2) , align="center", font=("ubuntu", 100, "normal"))

    if ball.xcor() <-390 : # ball out left border
        ball.goto(0, 0)
        ball.dx *= -1
        score2 += 1
        score.clear()
        score.write("{}  |  {}".format(score1, score2), align="center", font=("ubuntu", 100, "normal"))

    # collision ball and racket
    if (ball.xcor() > racket_1.xcor() -10  and ball.xcor() < racket_1.xcor() +10 ) and (ball.ycor() < racket_1.ycor() + 40 and ball.ycor() > racket_1.ycor() -40):
        ball.setx(racket_1.xcor() -10)
        ball.dx *= -1

    if (ball.xcor() < racket_2.xcor() +10 and ball.xcor() > racket_2.xcor() -10 ) and (ball.ycor() < racket_2.ycor() + 40 and ball.ycor() > racket_2.ycor() -40):
        ball.setx(racket_2.xcor() +10)
        ball.dx *= -1
# End while loop