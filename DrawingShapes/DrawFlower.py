import turtle


def draw_square(some_turtle):
    start_point = -45
    for i in range(4):
        some_turtle.right(start_point)
        some_turtle.forward(50)
        if(start_point > 100):
            start_point = -45
        start_point = start_point + 90
    some_turtle.fillcolor("red")

def draw_art():
    # we will draw a square
    window = turtle.Screen()
    window.bgcolor("white")
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("black")
    brad.speed(0)
    for i in range(36):
        draw_square(brad)
        brad.right(10)
    brad.right(90)
    brad.forward(200)
    window.exitonclick()

draw_art()
