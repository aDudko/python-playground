import turtle as tim
from random import choice, randint

tim.shape("turtle")
tim.hideturtle()

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color = (r, g, b)
    return color

# def dash_and_dash_line():
#     for _ in range(10):
#         tim.forward(10)
#         tim.penup()
#         tim.forward(10)
#         tim.pendown()
# dash_and_dash_line()

# def drawing_different_shapes():
#     count_corner = 3
#     tim.colormode(255)
#     for _ in range(3, 11):
#         tim.color(random_color())
#         grad = 360 / count_corner
#         iter_corner = 1
#         while iter_corner * grad <= 360:
#             tim.right(grad)
#             tim.forward(50)
#             iter_corner += 1
#         count_corner += 1
# drawing_different_shapes()

# https://en.wikipedia.org/wiki/Random_walk
def random_walk():
    tim.speed(10)
    tim.pensize(15)
    tim.colormode(255)
    directions = [0, 90, 180, 270]
    for _ in range(250):
        tim.color(random_color())
        tim.forward(30)
        tim.setheading(choice(directions))
random_walk()

# def draw_spirograph(size_of_gap):
#     tim.speed("fastest")
#     tim.colormode(255)
#     for _ in range(int(360 / size_of_gap) + 1):
#         tim.color(random_color())
#         tim.circle(100)
#         tim.setheading(tim.heading() - size_of_gap)
# draw_spirograph(5)

screen = tim.Screen()
screen.exitonclick()