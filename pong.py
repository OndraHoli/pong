

import turtle
wn = turtle.Screen()
wn.title("pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# score
score_a = 0
score_b = 0

# palka 1

palka_a = turtle.Turtle()
palka_a.speed(0)
palka_a.shape("square")
palka_a.color("white")
palka_a.shapesize(stretch_wid=5, stretch_len=1)
palka_a.penup()
palka_a.goto(-350, 0)

# palka 2

palka_b = turtle.Turtle()
palka_b.speed(0)
palka_b.shape("square")
palka_b.color("white")
palka_b.shapesize(stretch_wid=5, stretch_len=1)
palka_b.penup()
palka_b.goto(350, 0)

# micek

micek = turtle.Turtle()
micek.speed(0)
micek.shape("square")
micek.color("white")
micek.penup()
micek.goto(0, 0)

micek.dx = 0.2
micek.dy = 0.2

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Hráč A :0 Hráč B: 0",align= "center",font=("Courier",24,"normal"))

# funkce

def palka_a_up():
    y = palka_a.ycor()
    y += 20
    palka_a.sety(y)

def palka_a_down():
    y = palka_a.ycor()
    y -= 20
    palka_a.sety(y)

def palka_b_down():
    y = palka_b.ycor()
    y -= 20
    palka_b.sety(y)

def palka_b_up():
    y = palka_b.ycor()
    y += 20
    palka_b.sety(y)

# klavesnice bind

wn.listen()
wn.onkeypress(palka_a_up,"w")
wn.onkeypress(palka_a_down,"s")
wn.onkeypress(palka_b_up, "Up")
wn.onkeypress(palka_b_down,"Down")

while True:
    wn.update()

    # pohyb micku
    micek.setx(micek.xcor() + micek.dx)
    micek.sety(micek.ycor() + micek.dy)

    # kolize s okrajem
    if micek.ycor() > 290:
        micek.sety(290)
        micek.dy *= -1

    if micek.ycor() < -290:
        micek.sety(-290)
        micek.dy *= -1

    if micek.xcor() > 390:
        micek.goto(0,0)
        micek.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if micek.xcor() < -390:
        micek.goto(0,0)
        micek.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # palka kolize

    if (micek.xcor() > 340 and micek.xcor() < 350) and (micek.ycor() < palka_b.ycor() + 40 and micek.ycor() > palka_b.ycor() - 40):
        micek.setx(340)
        micek.dx *= -1

    if (micek.xcor() < -340 and micek.xcor() > -350) and (micek.ycor() < palka_a.ycor() + 40 and micek.ycor() > palka_a.ycor() - 40):
        micek.setx(-340)
        micek.dx *= -1












