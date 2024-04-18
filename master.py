import turtle

screen = turtle.Screen()
screen.bgcolor("light blue")
screen.title("python turtle")

#square
'''
turtle_instance = turtle.Turtle()
turtle_instance.forward(150)
turtle_instance.left(90)
turtle_instance.forward(150)
turtle_instance.left(90)
turtle_instance.forward(150)
turtle_instance.left(90)
turtle_instance.forward(150)
'''
'''
turtle_instance = turtle.Turtle()
for i in range(4):
    turtle_instance.forward(100)
    turtle_instance.left(90)
'''

#star
'''
turtle_instance = turtle.Turtle()
for i in range(5):
    turtle_instance.right(144)
    turtle_instance.forward(250)
'''
#polygon
turtle_instance = turtle.Turtle()
kenarsayisi = 8
cevresi = 360 / kenarsayisi
uzunluk = 100
for i in range(kenarsayisi):
    turtle_instance.forward(uzunluk)
    turtle_instance.right(cevresi)



turtle.done()
