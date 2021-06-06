import turtle

ball_speed = 40
left_player_score = 0
right_player_score = 0

# screen
screen = turtle.Screen()
screen.title("Pong Game")
screen.setup(width=1200, height=700)

# left paddle
left_paddle = turtle.Turtle()
left_paddle.hideturtle()
left_paddle.speed(15)
left_paddle.shape('square')
left_paddle.shapesize(stretch_wid=5, stretch_len=1)
left_paddle.color('black')
left_paddle.penup()
left_paddle.goto(-510, 0)
left_paddle.showturtle()
left_paddle.speed(1)

# right paddle
right_paddle = turtle.Turtle()
right_paddle.hideturtle()
right_paddle.speed(15)
right_paddle.shape('square')
right_paddle.shapesize(stretch_wid=5, stretch_len=1)
right_paddle.color('black')
right_paddle.penup()
right_paddle.goto(510, 0)
right_paddle.showturtle()
right_paddle.speed(1)

# ball
ball = turtle.Turtle()
ball.speed(ball_speed)
ball.shape('circle')
ball.shapesize(stretch_wid=0.5, stretch_len=0.5)
ball.color('red')
ball.penup()
ball.dx = -5            # x moving
ball.dy = 5            # y moving

# score board
score_board = turtle.Turtle()
score_board.speed(0)
score_board.hideturtle()
score_board.color('red')
score_board.penup()
score_board.goto(0, 300)
score_board.write("LEFT PLAYER : {}                          RIGHT PLAYER : {}".format
                  (left_player_score, right_player_score),
                  align="center", font=("Comic Sans", 20, "normal"))

# functions
def left_up():
    if (left_paddle.ycor() < 290):
        y = left_paddle.ycor()
        y += 20
        left_paddle.sety(y)

def left_down():
    if (left_paddle.ycor() > -290):
        y = left_paddle.ycor()
        y -= 20
        left_paddle.sety(y)

def right_up():
    if (right_paddle.ycor() < 290):
        y = right_paddle.ycor()
        y += 20
        right_paddle.sety(y)

def right_down():
    if (right_paddle.ycor() > -290):
        y = right_paddle.ycor()
        y -= 20
        right_paddle.sety(y)

# keyboard
screen.listen()
screen.onkeypress(left_up, "w")
screen.onkeypress(left_down, "s")
screen.onkeypress(right_up, "Up")
screen.onkeypress(right_down, "Down")

# game loop
while True:
    screen.update()

    # ball moves
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # boarders and scores
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -345:
        ball.sety(-345)
        ball.dy *= -1

    if ball.xcor() < -600:
        ball.goto(0,0)
        ball.dx *= -1
        ball.dy *= -1
        right_player_score += 1
        score_board.clear()
        score_board.write("LEFT PLAYER : {}                          RIGHT PLAYER : {}".format
                          (left_player_score, right_player_score),
                          align="center", font=("Comic Sans", 20, "normal"))

    if ball.xcor() > 600:
        ball.goto(0, 0)
        ball.dx *= -1
        ball.dy *= -1
        left_player_score += 1
        score_board.clear()
        score_board.write("LEFT PLAYER : {}                          RIGHT PLAYER : {}".format
                          (left_player_score, right_player_score),
                          align="center", font=("Comic Sans", 20, "normal"))

    # collisions
    if (ball.xcor() < -490 and ball.xcor() > -500) and\
            (ball.ycor() > left_paddle.ycor() - 50 and ball.ycor() < left_paddle.ycor() + 50):
        ball.dx *= -1

    if (ball.xcor() > 490 and ball.xcor() < 500) and\
            (ball.ycor() > right_paddle.ycor() - 50 and ball.ycor() < right_paddle.ycor() + 50):
        ball.dx *= -1
