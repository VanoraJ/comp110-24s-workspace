"""EX08: Turtle Project - Sunset on the sea."""
 
__author__ = "730653557"

import turtle
from turtle import Turtle, colormode, done
import math


def separate_frame(my_turtle: Turtle, x: float, y: float, degree: int, length: int) -> None:
    """Function: Separating the frame for the ocean part and the sky part."""
    """Requirement 1: Drawing function #1 with at least 3 parameters: turtle, x, and y."""
    my_turtle.penup()
    my_turtle.goto(x, y)
    my_turtle.setheading(degree)
    my_turtle.pendown()
    my_turtle.forward(length)


def ocean(my_turtle: Turtle, x: float, y: float, degree: int, length: int, width: int) -> None:
    """Function: Outlining the ocean and fill in color."""
    """Requirement 1: Drawing function #2 with at least 3 parameters: turtle, x, and y."""
    my_turtle.color(136, 195, 177)

    """Requirement 5: Filling color of the shapes (and various other shapes later on)."""
    my_turtle.penup()
    my_turtle.goto(x, y)
    my_turtle.setheading(degree)
    my_turtle.pendown()
    my_turtle.begin_fill()
    for i in range(0, 2):
        my_turtle.forward(length)
        my_turtle.right(90)
        my_turtle.forward(width)
        my_turtle.right(90)
    my_turtle.end_fill()


def semicircle(my_turtle: Turtle, radius: int, angel_degree: int) -> None:
    """Function: drawing small semicircles as a building component of the ocean waves."""
    """Requirement 8: Above and Beyond - the use of the function circle to draw circle and semicircles."""
    my_turtle.color(237, 220, 179)
    
    my_turtle.begin_fill()
    my_turtle.setheading(50)
    my_turtle.circle(radius, angel_degree)
    my_turtle.setheading(180.0)
    angel_radian: float = math.radians(angel_degree)
    traveled_length: float = 2 * radius * math.sin(angel_radian / 2)
    my_turtle.forward(traveled_length)
    my_turtle.end_fill()


def create_waves(my_turtle: Turtle, number: int, radius: int, angel_degree: int) -> None:
    """Function: Connecting the semicircles together while leaving a line at the end so it looks likes sea waves moving."""
    angel_radian: float = math.radians(angel_degree)
    traveled_length: float = 2 * radius * math.sin(angel_radian / 2)
    
    """Requirement 3: Recursive definition of a looping function."""
    if number == 0:
        return None
    else:
        semicircle(my_turtle, radius, angel_degree)

        my_turtle.penup()
        my_turtle.setheading(0)
        my_turtle.forward(traveled_length)
        my_turtle.pendown()
        my_turtle.setheading(50)

        create_waves(my_turtle, number - 1, radius, angel_degree)


def drawing_waves(my_turtle: Turtle, x: float, y: float, number: int, radius: int, angel_degree: int) -> None:
    """Fucntion: completed drawing wave function that is using the create_wave while knowing where and how many to draw."""
    """Requirement 1: Drawing function #3 with at least 3 parameters: turtle, x, and y."""
    """Requirement 7: Above and Beyond - This is the completed wave function that allows me to draw waves at the place I want."""

    my_turtle.penup()
    my_turtle.goto(x, y)
    my_turtle.pendown()
    create_waves(my_turtle, number, radius, angel_degree)


def sky(my_turtle: Turtle, x: float, y: float, degree: int, length: int, width: int) -> None:
    """Function: Outlining and filling the color for the sky."""
    """Requirement 1: Drawing function #4 with at least 3 parameters: turtle, x, and y."""
    my_turtle.color(189, 208, 180)

    my_turtle.penup()
    my_turtle.goto(x, y)
    my_turtle.setheading(degree)
    my_turtle.pendown()
    my_turtle.begin_fill()
    for i in range(0, 2):
        my_turtle.forward(length)
        my_turtle.left(90)
        my_turtle.forward(width)
        my_turtle.left(90)
    my_turtle.end_fill()


def mountain(my_turtle: Turtle, x: float, y: float, degree: int, peak_x: float, peak_y: float, base_x: float, base_y: float) -> None:  
    """Function: Drawing triangles as mountains at the background."""
    """Requirement 1: Drawing function #5 with at least 3 parameters: turtle, x, and y."""  
    """Requirement 7: Above and Beyond - breaking down complex functions and nesting functions."""
    my_turtle.penup()
    my_turtle.goto(x, y)
    my_turtle.setheading(degree)
    my_turtle.pendown() 

    my_turtle.begin_fill()
    my_turtle.goto(peak_x, peak_y)
    my_turtle.goto(base_x, base_y)
    my_turtle.goto(x, y)
    my_turtle.end_fill()


def mountain_ridges(my_turtle: Turtle) -> None:
    """Function: Connecting mountains together as the background using the defined mountain function."""
    """Requirement 2: Calling the function mountain more than twice."""
    """Requirement 5: Changing marker color and filling color."""
    """Requirement 7: Above and Beyond - breaking down complex functions and nesting functions."""
    my_turtle.pencolor(50, 121, 161)
    my_turtle.fillcolor(5, 58, 88)
    mountain(my_turtle, -300.0, -80.0, -45, 200.0, 300.0, 700.0, -80.0)
    my_turtle.pencolor(243, 177, 190)
    my_turtle.fillcolor(225, 120, 140)
    mountain(my_turtle, -400.0, -80.0, -45, -100.0, 200.0, 200.0, -80.0)
    my_turtle.pencolor(255, 179, 147)
    my_turtle.fillcolor(255, 128, 67)
    mountain(my_turtle, -100.0, -80.0, -45, 150.0, 150.0, 400.0, -80.0)


def sun(my_turtle: Turtle, radius: float, origin_x: float, origin_y: float) -> None:
    """Function: Drawing a circle as the sun on the top left."""
    """Requirement 1: Drawing function #6 with at least 3 parameters: turtle, x, and y."""
    my_turtle.color(230, 69, 86)
    
    my_turtle.penup()
    my_turtle.goto(origin_x, origin_y)
    my_turtle.goto(origin_x, origin_y - radius)
    my_turtle.setheading(0.0)
    my_turtle.pendown()
    my_turtle.begin_fill()
    my_turtle.circle(radius)
    my_turtle.end_fill()


def fixed_boat_base(my_turtle: Turtle) -> None:
    """Function: drawing a fixed isosceles trapezoid as the base of the boat."""
    """Requirement 7: Above and Beyond - breaking down complex functions and nesting functions."""
    my_turtle.setheading(0.0)
    my_turtle.forward(120)
    my_turtle.setheading(180)
    my_turtle.left(56.31)
    my_turtle.forward(36.056)
    my_turtle.setheading(180)
    my_turtle.forward(80)
    my_turtle.right(56.31)
    my_turtle.forward(36.056)


def boat_small_sail(my_turtle: Turtle, base_length: float, height: float) -> None:
    """Function: drawing a right angle triangle as the smaller sail part of the boat."""
    """Requirement 7: Above and Beyond - breaking down complex functions and nesting functions."""
    hypotenuse = math.sqrt(base_length ** 2 + height ** 2)
    angle = math.degrees(math.atan(height / base_length))

    my_turtle.setheading(0)  
    my_turtle.forward(base_length)  
    my_turtle.left(90)  
    my_turtle.forward(height)  
    my_turtle.left(90 + angle)
    my_turtle.forward(hypotenuse)


def boat_big_sail(my_turtle: Turtle, base_length: float, height: float) -> None:
    """Function: drawing a right angle triangle as the larger sail part of the boat."""
    """Requirement 7: Above and Beyond - breaking down complex functions and nesting functions."""
    hypotenuse = math.sqrt(base_length ** 2 + height ** 2)
    angle = math.degrees(math.atan(height / base_length)) 

    my_turtle.setheading(180)  
    my_turtle.forward(base_length)  
    my_turtle.right(90)  
    my_turtle.forward(height)  
    my_turtle.right(90 + angle)
    my_turtle.forward(hypotenuse)


def boat_flag(my_turtle: Turtle, base_length: float, height: float) -> None:
    """Function: drawing a right angle triangle as the flag part of the boat."""
    """Requirement 7: Above and Beyond - breaking down complex functions and nesting functions."""
    hypotenuse = math.sqrt(base_length ** 2 + height ** 2)
    angle = math.degrees(math.atan(height / base_length)) 

    my_turtle.setheading(-90)  
    my_turtle.forward(height)  
    my_turtle.left(90)  
    my_turtle.forward(base_length)  
    my_turtle.left(180 - angle)
    my_turtle.forward(hypotenuse) 


def boat(my_turtle: Turtle, start_x: float, start_y: float) -> None:
    """Function: combining all parts of the boat."""
    """Requirement 1: Drawing function #7 with at least 3 parameters: turtle, x, and y."""   
    """Requirement 7: Above and Beyond - This is the completed function of drawing a boat, which is relying on all the samll functions defined above."""
    my_turtle.penup()
    my_turtle.goto(start_x, start_y)
    my_turtle.setheading(0.0)
    my_turtle.pendown()
    my_turtle.begin_fill()
    fixed_boat_base(my_turtle)
    my_turtle.end_fill()

    my_turtle.penup()
    my_turtle.goto(100, -110)
    my_turtle.setheading(0.0)
    my_turtle.color(222, 246, 251)
    my_turtle.pendown()
    my_turtle.begin_fill()
    boat_small_sail(my_turtle, 50, 100) 
    my_turtle.end_fill()

    my_turtle.penup()
    my_turtle.goto(220, -110)
    my_turtle.setheading(180)
    my_turtle.pendown()
    my_turtle.begin_fill()
    boat_big_sail(my_turtle, 60, 130)
    my_turtle.end_fill()

    my_turtle.penup()
    my_turtle.goto(160, 50)
    my_turtle.setheading(-90)
    my_turtle.color(230, 69, 86)
    my_turtle.pendown()
    my_turtle.begin_fill()
    boat_flag(my_turtle, 40, 20)
    my_turtle.end_fill()


def main() -> None:
    """Requirement 2: Defining the function main to construct Turtle and run all defined functions."""
    a_turtle: Turtle = Turtle()
    colormode(255)
    """Requirement 8: Above and Beyond - the use of the function setup to set the size of the screen/canvas."""
    turtle.setup(width=600, height=900)
    separate_frame(a_turtle, -300.0, -80.0, 0, 600)
    ocean(a_turtle, -300.0, -80.0, 0, 600, 400)
    """Requirement 3: Calling the drawing_waves function twice"""
    drawing_waves(a_turtle, -250.0, -225.0, 2, -100, 100)
    drawing_waves(a_turtle, -130.0, -350.0, 3, -100, 100)
    sky(a_turtle, -300.0, -80.0, 0, 600, 500)
    mountain_ridges(a_turtle)
    sun(a_turtle, 90, -170, 300)
    boat(a_turtle, 100, -120)
    a_turtle.hideturtle()


if __name__ == "__main__":
    main()
    done()