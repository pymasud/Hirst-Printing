
import turtle as t
import random

color_list = [(225, 223, 224), (199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (222, 224, 227),
              (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138),
              (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151),
              (141, 171, 155), (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203)]

tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")
tim.setheading(225)
tim.up()
tim.hideturtle()
tim.forward(300)
tim.setheading(0)


def jump():
    for i in range(0, 10):
        color = random.choice(color_list)
        tim.dot(20, color)
        tim.forward(50)


def turn():
    tim.backward(50)
    tim.left(90)
    tim.forward(50)
    tim.left(90)
    tim.forward(450)
    tim.right(180)


def draw():
    for i in range(10):
        jump()
        turn()


draw()

myscreen = t.Screen()
myscreen.exitonclick()


