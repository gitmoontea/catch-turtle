import turtle
import time
import random

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
    print(f"x coord : {x}\ny coord : {y}")
    print("ss::", turtle_instance.xcor(), "--", turtle_instance.ycor())
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
instance3.goto(0,300)
instance3.write("Score", move=True, font=text_font)

instance2 = turtle.Turtle()
instance2.color("black")
instance2.hideturtle()
instance2.penup()
instance2.goto(0, 260)
instance2.write("Time", move=True, font=text_font)


text = "Game Over"
second: int = 20

turtle_screen.onclick(score_update)


def turtle_random_move():
    turtle_x = random.randint(-200, 200)
    turtle_y = random.randint(-200, 200)
    turtle_instance.hideturtle()
    turtle_instance.goto(turtle_x, turtle_y)
    turtle_instance.showturtle()



while second >= 0:
    instance2.clear()
    instance2.setx(0)
    instance2.write(f"Time : {second}", font=text_font)
    time.sleep(1)
    second -= 1
    turtle_random_move()

instance2.clear()
instance2.setx(0)
instance2.write(f"{text}", font=text_font)

turtle_instance.hideturtle()


turtle_screen.mainloop()