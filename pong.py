import turtle, sys

#Set up the window
window = turtle.Screen()

window.title('Epic Games Eat Your Heart Out')
window.bgcolor('black')
window.setup(width=800, height=600)
window.tracer(0)


#Set up object movement

def leftUp():
    y = redPaddle.ycor()
    y += 20
    redPaddle.sety(y)

def rightUp():
    y = bluePaddle.ycor()
    y += 20
    bluePaddle.sety(y)

def leftDn():
    y = redPaddle.ycor()
    y -= 20
    redPaddle.sety(y)

def rightDn():
    y = bluePaddle.ycor()
    y -= 20
    bluePaddle.sety(y)


redPaddle = turtle.Turtle()

redPaddle.speed(0)
redPaddle.shape('square')
redPaddle.shapesize(stretch_wid=5, stretch_len=1)
redPaddle.color('red')
redPaddle.penup()
redPaddle.goto(-350, 0)


bluePaddle = turtle.Turtle()

bluePaddle.speed(0)
bluePaddle.shape('square')
bluePaddle.shapesize(stretch_wid=5, stretch_len=1)
bluePaddle.color('blue')
bluePaddle.penup()
bluePaddle.goto(350, 0)


ball = turtle.Turtle()

ball.speed()
ball.shape('circle')
ball.color('white')
ball.penup()
ball.goto(0, 0)
ball.dx = .15
ball.dy = .15


#Score
redScore = 0
blueScore = 0

pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write('Red Player: 0 \t\t Blue Player: 0', align='center', font=('Courier', 20, 'normal'))

#Game Controols

window.listen()
window.onkeypress(leftUp, 'w')
window.onkeypress(rightUp, 'Up')
window.onkeypress(leftDn, 's')
window.onkeypress(rightDn, 'Down')


while True:
    window.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border checks
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        redScore += 1
        ball.dx *= -1
        pen.clear()
        pen.write(f'Red Player: {redScore} \t\t Blue Player: {blueScore}', align='center', font=('Courier', 20, 'normal'))
    
    if ball.xcor() < -390:
        ball.goto(0, 0)
        blueScore += 1
        ball.dx *= -1
        pen.clear()
        pen.write(f'Red Player: {redScore} \t\t Blue Player: {blueScore}', align='center', font=('Courier', 20, 'normal'))


    #Check for paddle
    if 340 < ball.xcor() < 342 and bluePaddle.ycor() - 50 < ball.ycor() < bluePaddle.ycor() + 50:
        ball.setx(340)
        ball.dx *= -1


    if -342 < ball.xcor() < -340 and redPaddle.ycor() - 50 < ball.ycor() < redPaddle.ycor() + 50:
        ball.setx(-340)
        ball.dx *= -1

sys.exit()