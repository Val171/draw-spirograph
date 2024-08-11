from random import choice, randint
from turtle import Turtle as t, Screen
import turtle
turtle.colormode(255)

tim = t()
tim.speed("fastest")
tim.pensize((3))

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color = (r, g, b)
    return color


def draw_spirograph(shift):

    for i in range(int(360 / shift)):
        tim.circle(100, 360, 200)
        tim.color(random_color())
        tim.setheading(tim.heading() + shift)

draw_spirograph(5)









screen = Screen()
screen.exitonclick()
