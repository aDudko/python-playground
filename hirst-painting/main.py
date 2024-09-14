###This code will not work in repl.it as there is no access to the colorgram package here.###
##pip install colorgram.py##
import colorgram
import turtle
import random

def extract_colors(img_source):
    rgbs = []
    colors = colorgram.extract(img_source, 30)
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        color_tuple = (r, g, b)
        rgbs.append(color_tuple)
    return rgbs
rgb_colors = extract_colors('image.jpg')

def set_tim_in_next_line(tim):
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)

def draw_paint():
    for dot_count in range(1, number_of_dots + 1):
        tim.dot(20, random.choice(rgb_colors))
        tim.forward(50)
        if dot_count % 10 == 0: set_tim_in_next_line(tim)

turtle.colormode(255)
tim = turtle.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

draw_paint()
turtle.Screen().exitonclick()