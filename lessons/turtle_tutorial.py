from turtle import Turtle, colormode, done
leo: Turtle = Turtle()
colormode(255)


"""Exercise One: Draw a square"""
leo.forward(30)
leo.right(90)
leo.forward(30)
leo.right(90)
leo.forward(30)
leo.right(90)
leo.forward(30)


"""Exercise Two: Draw a triangle with a loop"""
leo.color("blue")  # Set color
leo.color(99, 204, 250)  # Set color with RGB
leo.pencolor("pink")  # Only set pen color
leo.fillcolor(32, 67, 93)  # Only set fill color
leo.color("green", "yellow")  # Set both pen and fill color

leo.pencolor(255, 173, 214)  # Only set pen color
leo.fillcolor(80, 242, 229)  # Only set fill color

leo.speed(50)

leo.penup()
leo.goto(45, 40)
leo.pendown()

leo.begin_fill()
i: int = 0
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i = i + 1
leo.end_fill()

leo.hideturtle()


"""Part 3: Mini-Project."""
bob: Turtle = Turtle()
bob.color(54, 170, 161)

bob.penup()
bob.goto(45, 40)
bob.pendown()
bob.left(90) #Turn back to face the correct direction

bob.speed(100)

side_length: int = 300

i: int = 0
while (i < 100):
    side_length = side_length * 0.97
    bob.forward(side_length)
    bob.left(121)
    i = i + 1

done()