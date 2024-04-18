import turtle

screen = turtle.Screen()
screen.bgcolor("light blue")
screen.title("shrinking square")

turtle_instance = turtle.Turtle()
turtle_instance.color("red")

def shrinkingsquare(size):
    for i in range(4):
        turtle_instance.forward(size)
        turtle_instance.left(90)
        size = size - 5

shrinkingsquare(150)
shrinkingsquare(130)
shrinkingsquare(110)
shrinkingsquare(90)
shrinkingsquare(70)
shrinkingsquare(50)
shrinkingsquare(30)
shrinkingsquare(10)



turtle.done()






