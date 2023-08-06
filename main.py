import turtle
import time
import random
SCORE_Y = turtle.window_height() * 0.45
TIME_Y = turtle.window_height() * 0.4
counter = 0

turtle_screen = turtle.Screen()
turtle_screen.screensize(500, 500)
turtle_screen.title("Kaplumbağa Yakalama")
turtle_instance = turtle.Turtle(shape="turtle", visible=True)
turtle_instance.left(90)
turtle_instance.penup()


def score_update(x, y):
    global counter
    instance3.clear()
    instance3.setx(0)
    tur_x = turtle_instance.xcor()
    tur_y = turtle_instance.ycor()
    click_state = (x < tur_x - 7 or x > tur_x + 7) or (y < tur_y - 7 or y > tur_y + 15)
    if not click_state:
        counter += 1
        instance3.write(f"Score : {counter}", move=True, font=text_font)
    else:
        instance3.write(f"Score : {counter}", move=True, font=text_font)


text_font = ("Times New Roman", 16, "")

instance3 = turtle.Turtle()
instance3.color("black")
instance3.hideturtle()
instance3.penup()
instance3.goto(0, SCORE_Y)
instance3.write("Score", move=True, font=text_font)

timer_instance = turtle.Turtle()
timer_instance.color("black")
timer_instance.hideturtle()
timer_instance.penup()
timer_instance.goto(0, TIME_Y)
timer_instance.write("Time", move=True, font=text_font)


text = "Game Over"
second: int = 5

turtle_screen.onclick(score_update)


def turtle_random_move():
    global second
    turtle_x = random.randint(-200, 200)
    turtle_y = random.randint(-200, 200)
    turtle_instance.hideturtle()
    turtle_instance.goto(turtle_x, turtle_y)
    turtle_instance.showturtle()
    if(second >= 0):
        turtle_screen.ontimer(turtle_random_move, 2000)
    else:
        turtle_instance.hideturtle()


turtle_random_move()


def countdown_timer():
    global second
    timer_instance.clear()
    timer_instance.setx(0)
    timer_instance.write(f"Time : {second}", font=text_font)
    second -= 1
    if(second >= 0):
        turtle_screen.ontimer(countdown_timer, 1000)
    else:
        timer_instance.clear()
        timer_instance.setx(0)
        timer_instance.write(f"{text}", font=text_font)


countdown_timer()


turtle_screen.mainloop()