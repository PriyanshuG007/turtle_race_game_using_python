from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Place your bet", prompt="choose a color of turtle:")

red_turtle = Turtle(shape="turtle")
red_turtle.penup()
red_turtle.color("red")
red_turtle.setposition(x=-230, y=0)

blue_turtle = Turtle(shape="turtle")
blue_turtle.penup()
blue_turtle.color("blue")
blue_turtle.setposition(x=-230, y=50)

green_turtle = Turtle(shape="turtle")
green_turtle.penup()
green_turtle.color("green")
green_turtle.setposition(x=-230, y=-50)

pink_turtle = Turtle(shape="turtle")
pink_turtle.penup()
pink_turtle.color("pink")
pink_turtle.setposition(x=-230, y=100)

yellow_turtle = Turtle(shape="turtle")
yellow_turtle.penup()
yellow_turtle.color("yellow")
yellow_turtle.setposition(x=-230, y=-100)

purple_turtle = Turtle(shape="turtle")
purple_turtle.penup()
purple_turtle.color("purple")
purple_turtle.setposition(x=-230, y=150)

orange_turtle = Turtle(shape="turtle")
orange_turtle.penup()
orange_turtle.color("orange")
orange_turtle.setposition(x=-230, y=-150)

all_turtles = [red_turtle, blue_turtle, green_turtle, pink_turtle, yellow_turtle, purple_turtle, orange_turtle]

race_is_on = None
if user_bet is not None:
    race_is_on = True

while race_is_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            race_is_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"you've won, the {winning_color} is the winning color")
            else:
                print(f"you've lost, the {winning_color} is the winning color")

        random_distance = random.randint(1, 10)
        turtle.forward(random_distance)

screen.exitonclick()
