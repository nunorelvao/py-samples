import turtle
import winsound
import asyncio

class MyPaddle(turtle.Turtle):
     def glow(self,x,y):
         self.fillcolor("grey")         
     def unglow(self,x,y):
         self.fillcolor("white")

class MyBall(turtle.Turtle):
     def glow(self,x,y):
         self.fillcolor("grey")
     def unglow(self,x,y):
         self.fillcolor("white")

wn = turtle.Screen()
wn.title("Pong by @NunoRelvao")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#Paddle A
paddle_a = MyPaddle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.onclick(paddle_a.glow) 
paddle_a.onrelease(paddle_a.unglow) 
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)
paddle_a._delay(1000)

#Paddle B
paddle_b = MyPaddle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.onclick(paddle_b.glow) 
paddle_b.onrelease(paddle_b.unglow) 
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

#Ball
ball = MyBall()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.onclick(ball.glow) 
ball.onrelease(ball.unglow) 
ball.penup()
ball.goto(0, 0)
ball.dx = 0.07
ball.dy = 0.07


#Functions to move paddle a
def paddle_a_up():
    y = paddle_a.ycor()
    #print ("Y: " + str(y) + " Height: " + str(wn.window_height()))
    if y < ((wn.window_height() / 2) - 60):        
        y += 20
        paddle_a.sety(y)       
    else:
        paddle_a.sety(wn.window_height() / 2 - 52)
    
def paddle_a_down():    
    y = paddle_a.ycor()
    #print ("Y: " + str(y) + " Height: " + str(wn.window_height()))
    if y > -((wn.window_height() / 2) - 60):        
        y -= 20
        paddle_a.sety(y)
        
    else:
        paddle_a.sety(-(wn.window_height() / 2) + 59)
    
#Functions to move paddle b
def paddle_b_up():
    y = paddle_b.ycor()
    #print ("Y: " + str(y) + " Height: " + str(wn.window_height()))
    if y < ((wn.window_height() / 2) - 60):
        y += 20
        paddle_b.sety(y)       
    else:
        paddle_b.sety(wn.window_height() / 2 - 52)

def paddle_b_down():
    y = paddle_b.ycor()
    #print ("Y: " + str(y) + " Height: " + str(wn.window_height()))
    if y > -((wn.window_height() / 2) - 60):
        y -= 20
        paddle_b.sety(y) 
    else:
        paddle_b.sety(-(wn.window_height() / 2) + 59)



#listen events
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


# Pen for score
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("PlayerA: 0       PlayerB: 0", align="center", font=("Console", 24, "bold"))

def unglow_all():
    ball.unglow(0,0)
    paddle_a.unglow(0,0)
    paddle_b.unglow(0,0)

def play_sound():
    winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

async def play_sound_bounce():   
    winsound.Beep(5000, 50)

async def play_sound_lost():
    winsound.Beep(3000, 100)
    # winsound.Beep(1000, 100)


def main():    
    wn.update()

    # Scores
    scoreA = 0
    scoreB = 0

    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    #border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        wn.ontimer(asyncio.run(play_sound_bounce()), 30)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        wn.ontimer(asyncio.run(play_sound_bounce()), 30)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        scoreA += 1
        pen.clear()
        pen.write("PlayerA: {}       PlayerB: {}".format(scoreA, scoreB), align="center", font=("Console", 24, "bold"))
        wn.ontimer(asyncio.run(play_sound_lost()), 30)

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        scoreB += 1
        pen.clear()
        pen.write("PlayerA: {}       PlayerB: {}".format(scoreA, scoreB), align="center", font=("Console", 24, "bold"))
        wn.ontimer(asyncio.run(play_sound_lost()), 30)
        

    #Paddle a and ball colisions
    if ball.xcor() < -330 and ball.xcor() < -340 and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        play_sound()
        paddle_a.glow(0,0)
        ball.glow(0,0)
        ball.setx(-330)
        ball.dx *= -1
        wn.ontimer(unglow_all, 200)

    #Paddle b and ball colisions
    if ball.xcor() > 330 and ball.xcor() < 340 and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        play_sound()
        paddle_b.glow(0,0)
        ball.glow(0,0)
        ball.setx(330)
        ball.dx *= -1
        wn.ontimer(unglow_all, 200)

while True:
    main()