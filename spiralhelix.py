import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("spiral helix")

turtle_instance = turtle.Turtle()
turtle_instance.color("red")
turtle.speed(0)
turtle_colors = ["purple", "blue", "green", "yellow", "red", "orange"]

for i in range(15):
    turtle_instance.color(turtle_colors[i % 6])
    turtle_instance.circle(10 * i)
    turtle_instance.circle(-10 * i)
    turtle_instance.left(i)


turtle.mainloop()
#turtle.done()


